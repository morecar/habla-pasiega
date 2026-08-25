# Tesis de 1967: importación provisional

Esta carpeta contiene la extracción de la capa OCR de
`PennyRJ_1967redux.pdf`, facilitado por Ralph J. Penny.

El OCR no es texto canónico. Contiene errores graves en diacríticos,
transcripción fonética, formas pasiegas, nombres propios, guiones y estructura
de página. Se conserva separado de `el-habla-pasiega.tex` para evitar que esos
errores entren silenciosamente en la edición.

## Regeneración

Desde la raíz del repositorio:

```sh
python3 scripts/extract_thesis_ocr.py \
  /ruta/a/PennyRJ_1967redux.pdf \
  sources/thesis-1967/ocr
```

`ocr/manifest.csv` relaciona cada página del PDF con su archivo de texto y su
estado de revisión. `printed_page_guess` es solamente una conjetura automática
y debe cotejarse visualmente.

## Estados previstos

- `ocr-unverified`: extracción automática sin revisar.
- `thesis-verified`: cotejada visualmente con la tesis escaneada.
- `book-verified`: cotejada también con la edición impresa de 1969.

