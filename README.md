<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="S.T.A.L.K.E.R. Save Editor"/>
</p>

<p align="center">
  <a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor"><img src="https://img.shields.io/badge/SOURCE-OPEN%20SOURCE-F2C037?style=for-the-badge&logo=github&logoColor=000"/></a>
  <a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/releases/latest"><img src="https://img.shields.io/badge/DOWNLOAD-LATEST%20RELEASE-30363D?style=for-the-badge&logo=github"/></a>
  <a href="https://stalker-save-editor.pages.dev"><img src="https://img.shields.io/badge/RUN-BROWSER%20BUILD-4CC9FF?style=for-the-badge&logo=webassembly&logoColor=000"/></a>
</p>

> **A cross-platform save editor and game toolkit for the full S.T.A.L.K.E.R. series.**  
> The rule is simple: **if the project cannot prove how to rewrite a structure safely, it stays read-only.**

<table>
<tr>
<td align="center"><b>7</b><br/><sub>save formats</sub></td>
<td align="center"><b>.NET 10</b><br/><sub>shared core</sub></td>
<td align="center"><b>Desktop</b><br/><sub>Avalonia 11</sub></td>
<td align="center"><b>Browser</b><br/><sub>WebAssembly</sub></td>
<td align="center"><b>CLI</b><br/><sub>NativeAOT</sub></td>
<td align="center"><b>15</b><br/><sub>UI languages</sub></td>
</tr>
</table>

## The editor

<p align="center">
  <img src="https://raw.githubusercontent.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/main/docs/images/frontend-followup/inventory-1920.png" width="100%" alt="S.T.A.L.K.E.R. Save Editor inventory screen"/>
</p>

<table>
<tr>
<td width="33%" valign="top"><b>🗂 Library & inspection</b><br/><sub>Find saves across Steam, Proton, GOG and disc installs. Read metadata, game slot screenshots, world state and compare saves/backups.</sub></td>
<td width="33%" valign="top"><b>🎒 Inventory & stashes</b><br/><sub>Edit money, stacks, condition, placement and upgrades; add/remove catalogue items; work with stashes, factions and safe level changer points.</sub></td>
<td width="33%" valign="top"><b>☁️ Steam boundary</b><br/><sub>Compare local/cloud saves, download or explicitly upload, inspect and toggle achievements. Cloud writes are never silently retried.</sub></td>
</tr>
<tr>
<td valign="top"><b>🩺 Doctors & diagnostics</b><br/><sub>Game Doctor, Save Doctor and Crash Analyzer inspect installs, saves, quest rules, logs, ownership hashes and unknown states without guessing.</sub></td>
<td valign="top"><b>🛠 Game Fixes & Toolkit</b><br/><sub>Source-tracked fix catalogue, guarded presets, transactional install/remove, snapshots, profiles, config editing and rollback ownership.</sub></td>
<td valign="top"><b>🎮 Companion</b><br/><sub>In-game tooling for the trilogy plus experimental S.T.A.L.K.E.R. 2 companion: teleport, weather, live actions and item tooling through explicit protocols.</sub></td>
</tr>
</table>

## Supported zone

| Game | Read | Write | Extra tooling |
|---|:---:|:---:|---|
| **Shadow of Chernobyl 1.0004 / 1.0006** | ✅ | ✅ | Companion · Game Fixes · Doctors |
| **Clear Sky 1.5.10** | ✅ | ✅ | Companion · Game Fixes · Doctors |
| **Call of Pripyat 1.6.02** | ✅ | ✅ | Companion · Game Fixes · Doctors |
| **Enhanced Editions — SoC / CS / CoP** | ✅ | capability-gated | Game Fixes · Doctors |
| **S.T.A.L.K.E.R. 2: Heart of Chornobyl** | ✅ | capability-gated | Doctors · experimental companion |

<sub>Detection is based on file content rather than path assumptions. Unsupported/unknown structures remain visible but are not made writable.</sub>

## Compare & inspect

<p align="center">
  <img src="https://raw.githubusercontent.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/main/docs/images/frontend-followup/compare-1920.png" width="100%" alt="Save compare screen"/>
</p>

<table>
<tr>
<td width="25%" valign="top"><b>Library</b><br/><sub>all discovered saves, newest first</sub></td>
<td width="25%" valign="top"><b>Overview</b><br/><sub>money · health · rank · reputation · date</sub></td>
<td width="25%" valign="top"><b>Timeline</b><br/><sub>real mtime ordering and adjacent comparison</sub></td>
<td width="25%" valign="top"><b>Encyclopedia</b><br/><sub>installed-game catalogue with item actions</sub></td>
</tr>
</table>

## Safe writes

<p align="center"><img src="./assets/readme-safe-write.svg" width="100%" alt="Safe write pipeline"/></p>

<table>
<tr>
<td width="33%" valign="top"><b>Fail closed</b><br/><sub>Unknown or ambiguous fields stay opaque/read-only instead of receiving guessed meanings.</sub></td>
<td width="33%" valign="top"><b>Backup first</b><br/><sub>The original is preserved outside the save folder before any supported mutation is committed.</sub></td>
<td width="33%" valign="top"><b>Verify after write</b><br/><sub>The result is parsed again and round-trip validated before the operation is treated as successful.</sub></td>
</tr>
</table>

## Architecture

<p align="center"><img src="./assets/readme-architecture.svg" width="100%" alt="Architecture"/></p>

<table>
<tr>
<td width="33%" valign="top"><b>Shared core</b><br/><sub>Formats, capabilities, editing, backups, catalogues and patching live in one reusable .NET layer.</sub></td>
<td width="33%" valign="top"><b>Explicit boundaries</b><br/><sub>Steam, updater and companion concerns do not leak into the save-format core.</sub></td>
<td width="33%" valign="top"><b>Same logic, several surfaces</b><br/><sub>Desktop, browser and CLI reuse the same format/editing model instead of reimplementing rules.</sub></td>
</tr>
</table>

## Verification

<p align="center"><img src="./assets/readme-verification.svg" width="100%" alt="Verification model"/></p>

<table>
<tr>
<td width="50%" valign="top">
<b>Writable capability is evidence-driven.</b><br/><br/>
L1–L3 cover synthetic round-trips, headless/UI checks and packaged-runtime validation. L4–L5 require actual retail-game acceptance and end-to-end Steam/game evidence.
</td>
<td width="50%" valign="top">
<b>Installed-game mutation is guarded separately.</b><br/><br/>
Game Fixes and Toolkit actions use target/build gates, ownership hashes, transactional writes, snapshots and rollback state. Unknown loose files stay unknown.
</td>
</tr>
</table>

## Get it

<table>
<tr>
<td width="33%" align="center"><b>Source</b><br/><a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor">github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor</a></td>
<td width="33%" align="center"><b>Desktop builds</b><br/><a href="https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/releases/latest">Windows · Linux · macOS</a></td>
<td width="33%" align="center"><b>Browser build</b><br/><a href="https://stalker-save-editor.pages.dev">stalker-save-editor.pages.dev</a></td>
</tr>
</table>

<details>
<summary><b>Documentation</b></summary>

- [Architecture](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/ARCHITECTURE.md)
- [Project state / roadmap](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/roadmap/STATE.md)
- [Reliability levels](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/roadmap/RL-reliability.md)
- [Companion](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/COMPANION.md)
- [Companion protocol](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/MOD_COMPANION_PROTOCOL.md)
- [Game Fixes](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/GAME_FIXES.md)
- [Game / Save Doctor & Crash Analyzer](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/GAME_DOCTOR.md)
- [Profiles / snapshots / rollback](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/PROFILES.md)
- [Packaging](https://github.com/Dmitriy-DE/S.T.A.L.K.E.R.-Save-Editor/blob/main/docs/PACKAGING.md)

</details>

<p align="center"><sub>S.T.A.L.K.E.R. is a trademark of its respective owner. Independent community project; not affiliated with or endorsed by GSC Game World.</sub></p>