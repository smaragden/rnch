#!/bin/env python
# coding=utf8
# -*- coding: utf8 -*-

import os
from datetime import datetime, tzinfo, timedelta
from rez.packages_ import iter_packages
from HTMLParser import HTMLParser
from xml.dom import minidom
import codecs
 # create a subclass and override the handler methods

hugo_arnold_root = "/home/fredrik.brannbacka/Documents/SITES/docs/content/posts/softwares/arnold"

header = u'''---
title: "{title}"
date: {date}
draft: true
---

'''

class simple_utc(tzinfo):
    def tzname(self,**kwargs):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)


def pexists(path):
    if os.path.exists(path):
        return path

def get_package_root(variant):
    return pexists(os.path.join(variant.root, "ext"))

def get_changelog(root):
    return pexists(os.path.join(root, "Changes.html"))

def get_body(document):
    record = False
    body = u""
    with codecs.open(document, encoding='utf-8') as doc:
        for line in doc:
            if "<body>" in line:
                record = True
                continue
            if "</body>" in line:
                break
            if record:
                body += line
    return body

def write_document(path, header, content):
    print "Creating document: ", os.path.basename(path)
    try:
        os.makedirs(os.path.dirname(path))
    except:
        pass

    with codecs.open(path, encoding='utf-8', mode='w') as doc:
        doc.write(header)
        # Remove xml tag
        content = content.split(">", 1)[-1]
        doc.write(content)

def main():
    for package in iter_packages("arnold"):
        variant = package.get_variant(0)
        root = get_package_root(variant)
        if root is None:
            continue
        changelog = get_changelog(root)
        if changelog is None:
            continue
        body = get_body(changelog)
        if body is None:
            continue
        try:
            body = post_process(body)
        except Exception as e:
            print "Failed to create", type(e)
            print e

        version_root = os.path.join(hugo_arnold_root, str(package.version))
        post_path = os.path.join(version_root, "arnold_changelog_{version}.md".format(version=package.version))
        title = "Arnold Changelog v{version}".format(version=package.version)
        write_document(post_path, header.format(title=title, date=datetime.utcnow().replace(tzinfo=simple_utc()).isoformat()), body)


def post_process(html):
    doc = minidom.parseString(html.encode('utf-8'))
    for pre in doc.getElementsByTagName('pre'):
        #check if first child is <code>
        children = pre.childNodes
        if pre.childNodes[0].nodeName != "#code":
            code = doc.createElement("code")
            pre.appendChild(code)
            for child in pre.childNodes:
                #pre_child = pre.removeChild(child)
                #new_child = pre_child.clone()
                #pre_child.unlink()
                code.appendChild(child)
    return doc.toxml()
    """
    class DocHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "body":
                record = True
        def handle_endtag(self, tag):
            print "Encountered an end tag :", tag
        def handle_data(self, data):
            if tag == "body":
                record = False
    parser = DocHTMLParser()
    parser.feed(html)
    """

if __name__ == '__main__':
    main()