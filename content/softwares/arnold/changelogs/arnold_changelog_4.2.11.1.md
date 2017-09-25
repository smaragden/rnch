---
title: "Arnold Changelog v4.2.11.1"
date: 2017-09-25T22:28:37.441538+00:00
---

<div class="uisymbols uinohelp" id="main">

<div class="milestone" id="content">
<h1>Milestone 4.2.11</h1>


<div class="description trac-content">
<h2 id="Enhancements">Enhancements</h2>
<ul><li><strong>Russian Roulette</strong>: The <tt>standard</tt> and <tt>lambert</tt> shaders now use Russian Roulette termination to more efficiently render with high GI depth. For AA samples 5 or higher the increase in noise is typically very small. Indoor scenes with high GI depth will benefit the most, but also scenes with lots of glass and high refraction/reflection depth. In such scenes we have measured between 1.5x and 5x faster renders. (#4901)
</li><li><strong>Global shader override</strong>: It is now possible to override the shader for all objects in the scene by specifying an existing shader in the new global option <tt>shader_override</tt>. (#4909)
</li><li><strong>Search paths</strong>: The procedural and shader search paths can now use both <tt>:</tt> and <tt>;</tt> characters as separators for multiple paths, on all platforms. Texture search paths already supported this. (#4897)
</li><li><strong>Custom attributes in deep EXR</strong>: Just like the regular EXR driver, the deep EXR driver now also supports custom metadata/attributes via the new parameter <tt>driver_deepexr.custom_attributes</tt>. (#4915)
</li><li><strong>Render options and stats in EXR metadata</strong>: Several global render options, such as sample settings and ray depths, are now stored in the image file as EXR metadata. We also store a few render stats, such as date, used memory, number of polygons and curve segments. These EXR attributes use a path-like metadata layout, e.g. &quot;arnold/options/AA_samples&quot;, &quot;arnold/stats/memory/peak&quot;, or &quot;arnold/host/hw&quot;. We might add a few extra attributes in future releases, and perhaps rename some existing attributes based on customer feedback. (#4849, #4860)
</li><li><strong>Env var expansion in procedural nodes</strong>: The <tt>procedural.dso</tt> parameter now supports expansion of environment variables delimited by square brackets, similar to the env var expansion in searchpaths in the <tt>options</tt> node. (#4937)
</li><li><strong>Removed size limit on node and metadata names</strong>: Node names, node entry names, and metadata item names no longer have any size limitations. (#4932)
</li><li><strong>Report memory for smooth derivs</strong>: The memory usage summary for polymeshes now includes a separate line to account for <tt>subdiv_smooth_derivs</tt> storage. (#4925)
</li><li><strong>Upgraded OIIO to 1.5.20</strong>: We have upgraded the OpenImageIO library used for reading texture maps from 1.5.15 to 1.5.20. There have been many changes between these two versions, including many little bug fixes and optimizations. (#4739, #4735, #4855, #4864)
</li></ul><h2 id="APIadditions">API additions</h2>
<ul><li><strong><tt>AtString</tt> version of <tt>AiNodeEntryGetName()</tt></strong>: Added an alternate version of <tt>AiNodeEntryGetName()</tt> called <tt>AiNodeEntryGetNameAtString()</tt> that returns an <tt>AtString</tt> name instead of a <tt>char*</tt> name. (#4917)
</li></ul><h2 id="Incompatiblechanges">Incompatible changes</h2>
<ul><li><strong>Renamed sss and volume sampling options</strong>: The global options <tt>volume_indirect_samples</tt> and <tt>sss_bssrdf_samples</tt> have been renamed to <tt>GI_volume_samples</tt> and <tt>GI_sss_samples</tt> respectively, for consistency with the other existing sampling options (<tt>GI_diffuse_samples</tt> etc). The old names will still work, as we have added them as deprecated synonyms, but will result in warnings in the log files. We recommend that any client code (such as proprietary DCC plugins) is changed to use the new names. (#4940)
</li><li><strong>Default sss samples</strong>: The default value of the newly renamed <tt>GI_sss_samples</tt> option has been changed from 0 to 2. Although rare, this will change the look of old scenes that contain SSS objects but where the SSS samples setting was left at its default of 0. (#4940)
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
<td class="id">#4886</td>
<td class="summary">
render crash on a scene with lots of ginstance
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
<td class="version">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2
                    </td>
<td class="time">
<span title="09/25/15 12:57:18">8 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#3196</td>
<td class="summary">
Wrong scene creation time stats for interactive rendering
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
                      
                      
                      
                      
                      
                      
                      
                      
                      4.0
                    </td>
<td class="time">
<span title="12/04/12 15:28:01">3 years</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#3981</td>
<td class="summary">
Clamp negative fresnel values to zero in standard shader
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
                      
                      
                      
                      
                      
                      
                      
                      
                      4.1
                    </td>
<td class="time">
<span title="03/05/14 12:47:47">21 months</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4735</td>
<td class="summary">
Invalid alpha channel for image textures without alpha in indirect bounces
</td>
<td class="component">
                      
                      
                      
                      
                      
                      
                      
                      
                      oiio
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
<span title="06/10/15 12:41:45">5 months</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4897</td>
<td class="summary">
Search path splitting inconsistent between parameters and platforms
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
<span title="10/02/15 14:20:53">7 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4908</td>
<td class="summary">
texture flush happens a frame too late in linux and OS X
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
<span title="10/07/15 03:15:32">6 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4910</td>
<td class="summary">
AiMicrofacetBTDFIntegrate rendering with wrong IOR
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
<span title="10/08/15 13:05:51">6 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4911</td>
<td class="summary">
Rare numerical precision artifacts causing noisy bumpmapping
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
<span title="10/08/15 17:02:44">6 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4914</td>
<td class="summary">
UDIM tile selection needs to handle bad barycentric coordinates
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
<span title="10/09/15 20:08:08">6 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4918</td>
<td class="summary">
Incorrect render with matte surfaces behind volumes
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
<span title="10/14/15 18:29:30">5 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4921</td>
<td class="summary">
Deep EXR: preserve float or RGB ID values when tolerance is zero
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
<span title="10/15/15 17:21:00">5 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4924</td>
<td class="summary">
Hostname missing in the logs on some Linux distributions
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
<span title="10/19/15 14:02:34">4 weeks</span>
</td>
</tr>
<tr class="even prio3">
<td class="id">#4942</td>
<td class="summary">
Nonexisting shader path warnings for drive letters on Windows
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
<span title="10/27/15 11:16:31">3 weeks</span>
</td>
</tr>
<tr class="odd prio3">
<td class="id">#4943</td>
<td class="summary">
kick warns about gamma/dither when writing to EXR via the '-o' option
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
<span title="10/27/15 12:53:59">3 weeks</span>
</td>
</tr>
<tr class="even prio4">
<td class="id">#4898</td>
<td class="summary">
rays/pixel stat not outputting correct value when there were 0 rays/pixel
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
<span title="10/02/15 15:38:59">7 weeks</span>
</td>
</tr>
<tr class="odd prio4">
<td class="id">#4899</td>
<td class="summary">
AtString version of AiNodeLookUpUserParameter crashes
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
<span title="10/02/15 15:49:14">7 weeks</span>
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
<td class="id">#4949</td>
<td class="summary">
Crash when evaluating a link to an array element after being unlinked
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.11.1
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
4.2.12
</td>
</tr>
<tr class="odd prio3" style="color:red">
<td class="id">#4951</td>
<td class="summary">
Crash tracing camera rays from shaders
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      digic, 4.2.11.1
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
4.2.12
</td>
</tr>
<tr class="even prio3" style="color:red">
<td class="id">#4952</td>
<td class="summary">
Russian roulette skips standard shader indirect light in rare cases
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.11.1
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
4.2.12
</td>
</tr>
<tr class="odd prio3" style="color:red">
<td class="id">#4954</td>
<td class="summary">
Render metadata should have short names for maximum OpenEXR compatibility
</td>
<td class="keywords">
                      
                      
                      
                      
                      
                      
                      
                      
                      4.2.11.1
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
4.2.12
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