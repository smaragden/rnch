---
title: "Arnold Changelog v4.2.7.4"
date: 2017-09-25T22:28:37.365496+00:00
---

<div class="uisymbols uinohelp" id="main">

<div class="milestone" id="content">
<h1>Milestone 4.2.7</h1>


<div class="description trac-content">
<h2 id="Enhancements">Enhancements</h2>
<ul><li><strong>Faster cutout opacity mapping</strong>: <tt>options.enable_fast_opacity</tt> can be enabled to get faster textured mapped opacity mask renders, such as for tree leaves.  Tests with production scenes have shown up to 25x speedups.  This flag also toggles a fix for more accurate renders, where previously the object would be rendered more transparent when further away from the camera. When using this option, noise/flicker can occur on far away geometry, similar to when rendering far away high res geometry.  If this happens, it is best to use a high amount of AA samples (and correspondingly lower amount of diffuse/glossy/light samples) to reduce flickering in animation.  The fast opacity flag is enabled for anything that is connected to any RGB parameter called &quot;opacity&quot;, so custom shaders that have an RGB opacity parameter will benefit from this.  We expect that users will want to enable this mode all the time for new scenes and if no one complains, in a future release we will likely remove this flag and leave the optimizations and fixes in the &quot;fast_opacity&quot; mode always enabled. (#4696)
</li><li><strong>Multiple scattering for volumes</strong>: Indirect light in volumes now supports an arbitrary number of bounces instead of being fixed to one bounce. It is now possible to render volumes such as clouds for which multiple scattering has a large influence on their appearance. The new <tt>options.GI_volume_depth</tt> parameter sets the number of bounces, defaulting to 0. The default value of <tt>options.volume_indirect_samples</tt> has been changed to 2. (#4594, #4682)
</li><li><strong>Support for deep volume output</strong>: Volumes are now visible in deep renders, but note that older &quot;atmosphere&quot; shaders and volumetric mattes are not supported yet. Previously, volumetric samples were composited with the next surface sample. Now, in case you want to implement your own deep driver, volumetric samples are available as independent samples to raw drivers or filters.  In order to query the end of a volumetric sample you can request the new built-in <tt>float Zback</tt> AOV channel. (#4654, #4655)
</li><li><strong>Per light volume contribution</strong>: A <tt>volume</tt> contribution scaling parameter was added to lights, similar to the existing <tt>diffuse</tt> and <tt>specular</tt> parameters. (#4657)
</li><li><strong>New EXR compression modes</strong>: Four additional compression modes, <tt>b44</tt>, <tt>b44a</tt>, <tt>dwaa</tt> and <tt>dwab</tt> have been added to <tt>driver_exr.compression</tt>. <tt>b44</tt> is lossy for half data and stores 32-bit data uncompressed. <tt>b44a</tt> is an extension to <tt>b44</tt> where areas of flat color are further compressed. <tt>dwaa</tt> and <tt>dwab</tt> correspond to JPEG like compression from DreamWorks Animation. Note that <tt>dwaa</tt> and <tt>dwab</tt> require the reading program to be compatible with OpenEXR 2.2 which is not yet widespread, Nuke 9.x will not read them. (#4634, #4638)
</li><li><strong>Faster UDIMs</strong>: UDIMs accessed through the <tt>image</tt> shader node now internally use texture handles, which helps improve multi-threading performance. (#3058)
</li><li><strong>OIIO improvements</strong>: Upgraded to OIIO to 1.5.15. 16-bit textures are now stored as 16-bit in the texture cache instead of as 32-bit floats. This halves the amount of memory 16-bit textures use. (#4619, #4671)
</li><li><strong>Spaces allowed in EXR metadata names</strong>: <tt>driver_exr.custom_attributes</tt> now supports spaces in names, as in the example below. (#4631)
<pre class="wiki"><code>driver_exr
{
 name mydriver
 filename foo.exr
 custom_attributes &quot;POINT2 'Chromaticities/Red Primary' 1.0 2.0&quot;
}
</code></pre></li></ul><h2 id="APIadditions">API additions</h2>
<ul><li><strong>Per texture cache invalidation</strong>: Sometimes reloading a specific texture is needed, rather than flushing the whole texture cache. <tt>AI_API void AiTextureInvalidate(const char *filename)</tt> is a new API call that lets developers invalidate single textures. (#4698)
</li></ul><h2 id="Incompatiblechanges">Incompatible changes</h2>
<ul><li><strong>Raised minimum OS X platform to 10.8</strong>: OS X 10.7 is no longer supported. You now need at least 10.8 (Mountain Lion) to run Arnold. (#4718)
</li><li><strong>Changed <tt>texture_sss_blur</tt> default to 0</strong>: SSS bump textures using <tt>sss_use_autobump</tt> and any textures used in an <tt>sss_irradiance_shader</tt> will now render with more detail. This may lead to increased texture I/O, though we have found little to no impact in various production scenes. (#4664)
</li><li><strong><tt>polymesh.nlist</tt></strong>: Values in this array must be normalized vectors now. (#4651)
</li><li><strong>Removed per-light <tt>volume_density</tt></strong>: This was an old hack that only applied to the <tt>volume_scattering</tt> atmosphere shader, and was not supported in the more recent object-based volume API. Note that you can still link <tt>volume_scattering.density</tt> to achieve the same effect, only globally instead of per-light. (#4676)
</li><li><strong><tt>volume_indirect_samples</tt></strong>: In existing scenes with one bounce of volume indirect lighting, <tt>options.GI_volume_depth</tt> must be set to <tt>1</tt> to re-enable it.
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
<tr class="even prio3">
<td class="id">#4506</td>
<td class="summary">
Opacities for volume mattes not as expected
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
<span title="02/10/15 22:48:14">4 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4596</td>
<td class="summary">
Crash interrupting render with mesh light
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
<span title="03/31/15 09:37:29">3 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4606</td>
<td class="summary">
Crash when calling AiRendering() during AiEnd()
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
<span title="04/06/15 14:41:19">2 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4624</td>
<td class="summary">
UDIMs should work when triangles span multiple tiles
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
<span title="04/15/15 12:29:59">2 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4636</td>
<td class="summary">
interactive update of light and shadow linking fails randomly
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
<span title="04/21/15 14:32:05">8 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4644</td>
<td class="summary">
&quot;too many messages&quot; warning is output for masked out messages
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
<span title="04/22/15 20:33:58">8 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4645</td>
<td class="summary">
planar light_blocker does not properly use height_edge
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
<span title="04/22/15 23:35:20">8 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4652</td>
<td class="summary">
Procedurals not working correct with _self traceset, self_shadows and receive_shadows
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
<span title="04/27/15 09:26:42">7 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4656</td>
<td class="summary">
Overlapping curves objects in procedural sometimes missing in render
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
<span title="04/29/15 04:13:49">7 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4658</td>
<td class="summary">
Faceting artifacts with SSS and bump mapping
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
<span title="04/29/15 15:40:39">7 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4661</td>
<td class="summary">
Restore shaders (shift + i) in interactive kick not working
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
<span title="05/01/15 03:33:16">6 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4662</td>
<td class="summary">
Crash in points primitive with small radii
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
<span title="05/01/15 16:39:47">6 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4664</td>
<td class="summary">
excessive texture blur when using sss_use_autobump
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
<span title="05/04/15 18:30:38">6 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4665</td>
<td class="summary">
Statistics are not reset for each render session
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
<span title="05/05/15 11:29:29">6 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4673</td>
<td class="summary">
Remove non-working light blocker upper case X, Y, Z ramp axes
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
<span title="05/11/15 12:10:07">5 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4674</td>
<td class="summary">
INT channels do not work with deep EXR driver
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
<span title="05/11/15 15:06:24">5 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4682</td>
<td class="summary">
Volume indirect converges to wrong result due to correlated samples
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
<span title="05/14/15 10:30:17">5 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4695</td>
<td class="summary">
clamp away invalid opacity in core shaders
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
<span title="05/19/15 20:44:25">4 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4697</td>
<td class="summary">
Improve warnings for varying and indexed data on objects that don't support them
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
<span title="05/19/15 23:56:47">4 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4699</td>
<td class="summary">
UDIM textures do not work with UV sets or linked uvs
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
<span title="05/21/15 09:59:52">4 weeks</span>
</td>
</tr>
<tr class="even prio4">
<td class="id">#4630</td>
<td class="summary">
silence compiler warning in Visual Studio for AiNodeGetStrAtString
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
<span title="04/17/15 16:19:45">2 months</span>
</td>
</tr>
<tr class="odd prio4">
<td class="id">#4659</td>
<td class="summary">
Fix pedantic warnings in public API
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
<span title="04/30/15 14:57:54">7 weeks</span>
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
<td class="id">#4724</td>
<td class="summary">
Crash with volumes when the P AOV is enabled and an object is behind or inside
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.7.1
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
<td class="milestone">
4.2.8
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
<td class="id">#4725</td>
<td class="summary">
Crash when using deep volumes without an RGBA AOV
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.7.2
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
4.2.8
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
<td class="id">#4728</td>
<td class="summary">
work scheduler lifetime extension causes crash in yeti
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.7.3
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
4.2.8
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4729</td>
<td class="summary">
Rare random buckets rendering too bright
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.7.3
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
4.2.8
</td>
</tr>
<tr class="even prio3">
<td class="id">#4731</td>
<td class="summary">
Missing header info in logs
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.7.3
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
4.2.8
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
<tr class="even prio2" style="color:red">
<td class="id">#4734</td>
<td class="summary">
Crash during IPR session with Maya on Linux
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.7.4
                    </td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      arnold
                    </td>
<td class="owner">
                      
                      
                      
                      
                      angel
                      
                      
                      
                      
                    </td>
<td class="priority">
                      
                      
                      
                      
                      
                      
                      
                      
                      critical
                    </td>
<td class="milestone">
4.2.8
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