---
title: "Arnold Changelog v4.2.14.3"
date: 2017-09-25T22:28:37.307213+00:00
---

<div class="uisymbols uinohelp" id="main">

<div class="milestone" id="content">
<h1>Milestone 4.2.14</h1>


<div class="description trac-content">
<h2 id="Enhancements">Enhancements</h2>
<ul><li><strong>Improved SSS</strong>: Subsurface scattering has been modified to leak less light into areas where it shouldn't and properly contribute to indirect light. This improves results around the nose or mouth in typical head models for example. Previously SSS was ignored for secondary GI bounces or contributing to more bounces than specified with <tt>GI_diffuse_depth</tt>. (#4174, #2978, #4648)
</li><li><strong>Better defaults in <tt>standard</tt> shader</strong>: The empirical SSS profile and GGX microfacet specular distribution are now used by default. (#5317)
</li><li><strong>Automatic reloading of procedurals</strong>: When a procedural geometry node's <tt>dso</tt> or <tt>data</tt> parameters are modified during an interactive session, the procedural will now be automatically reloaded, and the old contents cleared, avoiding the need for manually destroying and creating a new procedural. (#5190)
</li><li><strong>Faster rendering of few buckets</strong>: Rendering a small image will now scale to all available CPU cores regardless of bucket size. (#4647)
</li><li><strong>Maximum number of threads</strong>: The maximum number of threads has been increased from 128 to 256. (#5349)
</li><li><strong>Updated OIIO to 1.5.24</strong>: This new version comes with some optimizations and bug fixes. (#5139)
</li></ul><h2 id="APIadditions">API additions</h2>
<ul><li><strong><tt>AiSetLicenseString()</tt></strong>: Added a new API function for setting up a license string enclosed within angle brackets, which is the <tt>LICENSE</tt> line in a node-locked license file. Client code could now use this function and forget about setting up any environment variables, such as <tt>solidangle_LICENSE</tt>. (#5259)
<pre class="wiki"><code>AiSetLicenseString(&quot;&lt;LICENSE solidangle arnold YYYYMMDD 10-Jun-2016 uncounted hostid=... _ck=... sig=...&gt;&quot;);
</code></pre></li><li><strong>Python bindings for texture API</strong>: The Python API now exposes the following functions in <tt>ai_texture.py</tt> (#5293):
<ul><li><tt>AiTextureGetResolution()</tt>
</li><li><tt>AiTextureGetNumChannels()</tt>
</li><li><tt>AiTextureGetChannelName()</tt>
</li><li><tt>AiTextureGetFormat()</tt>
</li><li><tt>AiTextureGetBitDepth()</tt>
</li><li><tt>AiTextureGetMatrices()</tt>
</li><li><tt>AiTextureInvalidate()</tt>
</li></ul></li></ul><h2 id="Incompatiblechanges">Incompatible changes</h2>
<ul><li><strong>Disabled RLM broadcasting</strong>: We have disabled RLM broadcasting, which removes the two-second connection timeout delay due to the RLM client attempting to broadcast to find a license server in the LAN. From now on, the RLM license server must always be specified using the <tt>solidangle_LICENSE</tt> environment variable, even if it's <tt>localhost</tt>. (#4535)
</li><li><strong>Removed <tt>AiLicense{Set|Get}Attempts()</tt> and <tt>AiLicense{Set|Get}AttemptDelay()</tt></strong>: We have removed the &quot;retry&quot; RLM license request ability. (#2893)
</li></ul><h2 id="Bugfixes">Bug fixes</h2>
<p>
</p><div xmlns="http://www.w3.org/1999/xhtml">
<table class="listing tickets">
<thead>
<tr class="trac-columns">
<th class="id">
Ticket
</th><th class="summary">
Summary
</th><th class="component">
Component
</th><th class="owner">
Owner
</th><th class="priority asc">
Priority
</th><th class="version">
Version
</th><th class="time">
Created
</th>
</tr>
</thead>
<tbody>
<tr class="even prio2">
<td class="id">#5327</td>
<td class="summary">
Windows signal handlers not cooperating with parent process
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      critical
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/27/16 20:24:01">2 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4647</td>
<td class="summary">
Inefficient use of CPU threads when using a low number of buckets
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/23/15 12:32:06">16 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4648</td>
<td class="summary">
SSS not respecting diffuse GI depth correctly
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      thiago
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/23/15 23:23:57">16 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5084</td>
<td class="summary">
Fix sampling regression introduced in recent sampling refactoring
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      iliyan
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="02/04/16 12:30:25">6 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5157</td>
<td class="summary">
Multilayer EXR should properly output INT AOVs when other types are present
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/08/16 18:36:51">5 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5165</td>
<td class="summary">
Hang when repeatedly adding and removing nodes
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      thiago
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/10/16 18:11:26">5 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5167</td>
<td class="summary">
Crash when destroying a scene with cloned quad lights
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/11/16 13:36:18">5 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5170</td>
<td class="summary">
Crash when destroying a procedural used by the procedural cache
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/14/16 13:33:55">5 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5173</td>
<td class="summary">
Crash with volumes when light volume_samples is zero
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/15/16 16:48:40">5 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5179</td>
<td class="summary">
Deep driver: fix uninitialized variables
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/16/16 15:40:27">5 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5184</td>
<td class="summary">
Destroying any cached procedural will invalidate all copies
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/17/16 16:00:33">5 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5191</td>
<td class="summary">
EXR driver: autocrop corrupts the image when HALF AOVs are present
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/18/16 18:40:58">5 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5192</td>
<td class="summary">
Deep driver: uniform treatment of layer attributes
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/18/16 19:19:53">5 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5193</td>
<td class="summary">
Hang when destroying and re-creating procedurals with cache enabled
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/18/16 20:24:20">5 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5201</td>
<td class="summary">
Procedurals containing only shaders are not destroyed correctly
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/23/16 16:03:56">5 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5216</td>
<td class="summary">
Empirical SSS profile rendering incorrectly with low radius
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/31/16 15:06:44">4 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5217</td>
<td class="summary">
Matte object AOV filtering wrong with deep EXR
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="03/31/16 23:27:56">4 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5227</td>
<td class="summary">
poorly scaling codepath in catclark subdivision
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      alan
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/06/16 14:45:39">4 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5228</td>
<td class="summary">
SSE4.2 not always correctly detected
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      alan
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/06/16 19:00:14">4 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5233</td>
<td class="summary">
alHair transmission component incorrect
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/11/16 13:50:44">4 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5234</td>
<td class="summary">
Expand environment variables for volume.dso
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/11/16 15:20:42">4 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5239</td>
<td class="summary">
Metadata files don't allow 'RGB' as attribute or metadata name
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/12/16 17:53:18">4 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5240</td>
<td class="summary">
Deep driver: Surface samples should merge when inside a volume
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/14/16 07:19:51">4 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5248</td>
<td class="summary">
Invalid scene bounds with min_pixel_width in free mode
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/20/16 18:27:51">4 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5256</td>
<td class="summary">
Proc inheritance not respected for bump shaders
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      mike
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/22/16 18:52:58">4 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5260</td>
<td class="summary">
Spot light gobo texture blurred too much in volumes
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="04/27/16 18:31:57">3 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5274</td>
<td class="summary">
Mesh lights within procedurals are not correctly transformed
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/03/16 10:46:20">3 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5280</td>
<td class="summary">
Windows-only texture lookup crash for constant-valued .tx images
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      alan
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/04/16 15:10:33">3 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5301</td>
<td class="summary">
AiTextureAccess crash with multiple Arnold sessions
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/17/16 14:50:12">3 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5303</td>
<td class="summary">
Crash when saving TIFF if resolution is not a multiple of tile size
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      oiio
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/18/16 16:19:22">3 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5304</td>
<td class="summary">
refraction_opacity should track through multiple refractions
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      mike
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/19/16 00:05:32">3 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5308</td>
<td class="summary">
Wrong varying and indexed interpolation for integer user data types
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      fred
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/20/16 14:38:50">3 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5319</td>
<td class="summary">
Stray info messages at lower log verbosity
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      marcos
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/26/16 00:10:38">2 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5320</td>
<td class="summary">
Rare failed assert in LightRadiance() with atmospheric scattering
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      iliyan
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/26/16 00:53:02">2 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5329</td>
<td class="summary">
Deep AOV sample iterator losing mixed atmosphere and surface samples
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/30/16 13:33:41">2 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5332</td>
<td class="summary">
Atmosphere RGBA AOV missing from deep EXR files
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/31/16 20:25:46">2 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#5337</td>
<td class="summary">
server log entries because maketx tries to access nonexistent RPATH
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      oiio
                    </td>
<td class="owner">
                      
                      
                      
                      
                      oscar
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="06/02/16 16:18:40">2 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5341</td>
<td class="summary">
Override nodes applied to instances not working correctly
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="06/03/16 15:27:42">2 months</span>
</td>
</tr>
<tr class="even prio4">
<td class="id">#5302</td>
<td class="summary">
Fixed some wrong geometry stats after destroying scene nodes
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      minor
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="05/18/16 11:15:46">3 months</span>
</td>
</tr>
<tr class="odd prio4">
<td class="id">#5358</td>
<td class="summary">
Do not output warning for zero scaled transforms
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      thiago
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      minor
                    </td>
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="06/13/16 11:46:11">8 weeks</span>
</td>
</tr>
</tbody>
</table>
</div><p>
</p><div xmlns="http://www.w3.org/1999/xhtml">
<table class="listing tickets">
<thead>
<tr class="trac-columns">
<th class="id">
Ticket
</th><th class="summary">
Summary
</th><th class="keywords">
Keywords
</th><th class="component">
Component
</th><th class="owner">
Owner
</th><th class="priority asc">
Priority
</th><th class="milestone">
Milestone
</th>
</tr>
</thead>
<tbody>
<tr class="even prio3">
<td class="id">#5329</td>
<td class="summary">
Deep AOV sample iterator losing mixed atmosphere and surface samples
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      psyop, 4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      brecht
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
4.2.14
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5367</td>
<td class="summary">
Subdivs: bad limit surface near vertices connected to both boundaries and creases
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      ARC, 4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3">
<td class="id">#5368</td>
<td class="summary">
Subdivs: creased vertices are not correctly handled for UVs or indexed user data
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5377</td>
<td class="summary">
Fix memory leak and overhead due to samplers
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3">
<td class="id">#5383</td>
<td class="summary">
delay in opening kick window
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      kick
                    </td>
<td class="owner">
                      
                      
                      
                      
                      thiago
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5391</td>
<td class="summary">
Render checkpointing incorrectly computes channel offsets
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      nitrogen, 4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3">
<td class="id">#5396</td>
<td class="summary">
Drivers with append ON should not touch completed files
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5402</td>
<td class="summary">
Deep driver: use smaller minimum alpha value for samples
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.1 mikros
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3">
<td class="id">#5403</td>
<td class="summary">
lights and ginstances incorrectly only use the first matrix transform key when curved_motionblur is disabled
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.1
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      thiago
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
</tbody>
</table>
</div><p>
</p><div xmlns="http://www.w3.org/1999/xhtml">
<table class="listing tickets">
<thead>
<tr class="trac-columns">
<th class="id">
Ticket
</th><th class="summary">
Summary
</th><th class="keywords">
Keywords
</th><th class="component">
Component
</th><th class="owner">
Owner
</th><th class="priority asc">
Priority
</th><th class="milestone">
Milestone
</th>
</tr>
</thead>
<tbody>
<tr class="even prio3">
<td class="id">#5414</td>
<td class="summary">
Rare crash in Linux when Arnold is dynamically loaded
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      imageengine, 4.2.14.2
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      thiago
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5417</td>
<td class="summary">
node update is very slow when there are many nodes
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.2
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3">
<td class="id">#5420</td>
<td class="summary">
Remove incorrect texel offset from persp_camera.uv_remap
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.2
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5425</td>
<td class="summary">
Subdiv: adaptive mode should work with orthographic cameras
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.2
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3">
<td class="id">#5427</td>
<td class="summary">
Subdiv: adaptive mode not working with very small subdiv_adaptive_error
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.2
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3">
<td class="id">#5430</td>
<td class="summary">
Corrupted output for high resolution EXR with many AOVs in scanline mode
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      ILM, 4.2.14.2
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
</tbody>
</table>
</div><p>
</p><div xmlns="http://www.w3.org/1999/xhtml">
<table class="listing tickets">
<thead>
<tr class="trac-columns">
<th class="id">
Ticket
</th><th class="summary">
Summary
</th><th class="keywords">
Keywords
</th><th class="component">
Component
</th><th class="owner">
Owner
</th><th class="priority asc">
Priority
</th><th class="milestone">
Milestone
</th>
</tr>
</thead>
<tbody>
<tr class="even prio3" style="color:red">
<td class="id">#5189</td>
<td class="summary">
Fix assorted memory leaks
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.3
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      oscar
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3" style="color:red">
<td class="id">#5418</td>
<td class="summary">
parallel node init/update performance regression
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.3
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3" style="color:red">
<td class="id">#5432</td>
<td class="summary">
Displacing meshes with high valence vertices (&gt; 256) can crash
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.3
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3" style="color:red">
<td class="id">#5450</td>
<td class="summary">
Crash when setting parameters on a disabled procedural
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.3
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio3" style="color:red">
<td class="id">#5457</td>
<td class="summary">
Mesh light not evaluating UDIMs properly
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.3
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      ramon
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="odd prio3" style="color:red">
<td class="id">#5458</td>
<td class="summary">
Fix minor memory leaks
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.3
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      oscar
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      major
                    </td>
<td class="milestone">
5.0
</td>
</tr>
<tr class="even prio4" style="color:red">
<td class="id">#5433</td>
<td class="summary">
minor bug fixes
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.14.3
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      thiago
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      minor
                    </td>
<td class="milestone">
5.0
</td>
</tr>
</tbody>
</table>
</div><p>
</p>
</div>
<div id="attachments">
</div>


</div>

</div>