<p align="center"><img src="./assets/hero.svg" width="100%" alt="S.T.A.L.K.E.R. Save Editor"/></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Qt-41CD52?style=flat-square&logo=qt&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pyodide-FFD43B?style=flat-square&logo=python&logoColor=000"/>
  <img src="https://img.shields.io/badge/WebAssembly-654FF0?style=flat-square&logo=webassembly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Steam-000000?style=flat-square&logo=steam&logoColor=white"/>
</p>

# S.T.A.L.K.E.R. Save Editor

A tool I built because save editing gets interesting when the file stops being JSON.

**One Python core. Desktop, CLI and browser. Native boundaries where Python alone is not enough.**

<p align="center"><a href="https://stalker-save-editor.pages.dev"><b>▶ Open the browser build</b></a></p>

<p align="center"><img src="./assets/product-mockup.svg" width="100%" alt="S.T.A.L.K.E.R. Save Editor product mockup"/></p>

## <code>01 / editor_surface</code>

<p align="center"><img src="./assets/features.svg" width="100%" alt="S.T.A.L.K.E.R. Save Editor features"/></p>

## <code>02 / core_model</code>

<p align="center"><img src="./assets/core-model.svg" width="100%" alt="Binary edit model"/></p>

## <code>03 / architecture</code>

<p align="center"><img src="./assets/architecture-visual.svg" width="100%" alt="S.T.A.L.K.E.R. Save Editor architecture"/></p>

<p align="center"><img src="./assets/overview.svg" width="100%" alt="S.T.A.L.K.E.R. Save Editor overview"/></p>

## <code>04 / safe_write_pipeline</code>

<p align="center"><img src="./assets/flow-visual.svg" width="100%" alt="Safe binary editing pipeline"/></p>

> If I cannot prove how to rewrite a structure safely, the editor should refuse the edit.

## <code>05 / hard_parts</code>

| Problem | Approach |
|---|---|
| multiple container families | explicit format registry |
| unknown binary fields | opaque / read-only |
| native Steam dependency | isolated ctypes boundary |
| browser vs desktop | shared Python core through Pyodide |
| native decompression | isolated WASM/native helper |
| corruption risk | preview + framing/checksum + round-trip verification |
| distribution | PyInstaller builds + packaged diagnostics |

## <code>06 / engineering_signature</code>

<p align="center">
  <img src="./assets/engineering-signature.svg" width="100%" alt="Engineering signature"/>
</p>

## <code>07 / inspect</code>

- [Architecture](docs/ARCHITECTURE.md)
- [Binary-editing safety](docs/BINARY_SAFETY.md)
- [Sanitised parser example](examples/container-parser.py)
- [Live browser build](https://stalker-save-editor.pages.dev)

<details><summary><b>Why the implementation stays private</b></summary>

The complete parser, serializers, Steam integration, packaging setup and research notes remain in the private source repository.

</details>
