<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="S.T.A.L.K.E.R. Save Editor"/>
</p>

<p align="center">
  <a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor"><img src="https://img.shields.io/badge/SOURCE-OPEN%20SOURCE-F2C037?style=for-the-badge&logo=github&logoColor=000" alt="Source"/></a>
  <a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/releases/latest"><img src="https://img.shields.io/badge/LATEST-RELEASE-30363D?style=for-the-badge&logo=github" alt="Release"/></a>
  <a href="https://stalker-save-editor.pages.dev"><img src="https://img.shields.io/badge/OPEN-BROWSER%20BUILD-4CC9FF?style=for-the-badge&logo=webassembly&logoColor=000" alt="Browser"/></a>
</p>

<table>
<tr>
<td width="52%" valign="top">

### What this project is

A cross-platform save editor and game toolkit built around one rule:

> **If a structure cannot be rewritten safely, it stays read-only.**

It is not only a save editor anymore. The project now includes:

- Save Library and metadata discovery
- Inventory and stash editing
- Steam Cloud / achievements boundary
- Save Timeline and comparisons
- Game Doctor
- Save Doctor
- Crash Analyzer
- Game Fixes
- Companion tooling
- Desktop / Browser / CLI surfaces

</td>
<td width="48%" valign="top">

### Engineering profile

| Area | Implementation |
|---|---|
| Core | C# / .NET 10 |
| Desktop | Avalonia 11 |
| Browser | WebAssembly |
| CLI | NativeAOT |
| Companion | Lua 5.1 |
| Platforms | Windows · Linux · macOS |
| Save formats | 7 |
| Verification | L1 → L5 |

</td>
</tr>
</table>

<br/>

<img src="./assets/overview.svg" width="100%" alt="Supported games and formats"/>

<br/>

<table>
<tr>
<td width="50%" valign="top">

### Product surface

The editor deliberately separates **inspection**, **editing**, **diagnostics** and **installed-game mutation**.

Writable actions appear only when the capability gate for that exact target is satisfied.

</td>
<td width="50%" valign="top">

### Surfaces

Desktop, browser and CLI reuse the same format/editing core, while Steam, updater and companion functionality live behind their own boundaries.

</td>
</tr>
</table>

<img src="./assets/actual-surfaces.svg" width="100%" alt="Product surfaces"/>

<br/>

<table>
<tr>
<td width="50%" valign="top">
<img src="./assets/features.svg" width="100%" alt="Feature map"/>
</td>
<td width="50%" valign="top">

### Why this is interesting technically

- unknown fields remain opaque
- writable capabilities are evidence-gated
- backups happen before mutation
- source saves are re-hashed before write
- written saves are parsed again
- Steam Cloud writes require explicit confirmation
- game-file patching tracks ownership and rollback state
- one core drives several user-facing surfaces

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td width="46%" valign="top">

### Safe write pipeline

The project never treats “parsed successfully” as enough evidence to write.

A write path is prepared as an immutable edit plan, the source is re-read, a fresh SHA-256 is checked, the original is backed up, the change is written, then the result is parsed and verified again.

</td>
<td width="54%" valign="top">
<img src="./assets/flow-visual.svg" width="100%" alt="Safe write pipeline"/>
</td>
</tr>
</table>

<br/>

<table>
<tr>
<td width="54%" valign="top">
<img src="./assets/architecture-visual.svg" width="100%" alt="Architecture"/>
</td>
<td width="46%" valign="top">

### Architecture

The solution separates:

- Core
- shared Avalonia app layer
- Desktop
- Browser
- CLI
- Steam boundary
- Updater

Game Fixes and Companion reuse the shared patching/storage layer but keep separate manifests, validators and ownership state.

</td>
</tr>
</table>

<br/>

<img src="./assets/core-model.svg" width="100%" alt="Core model"/>

<br/>

<img src="./assets/engineering-signature.svg" width="100%" alt="Verification levels"/>

<br/>

<table>
<tr>
<td width="33%" align="center">
<b>Source</b><br/>
<a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor">Main repository</a>
</td>
<td width="33%" align="center">
<b>Builds</b><br/>
<a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/releases/latest">Latest release</a>
</td>
<td width="33%" align="center">
<b>Web</b><br/>
<a href="https://stalker-save-editor.pages.dev">Browser build</a>
</td>
</tr>
</table>

<p align="center"><sub>S.T.A.L.K.E.R. is a trademark of its respective owner. This project is an independent community tool and is not affiliated with or endorsed by GSC Game World.</sub></p>