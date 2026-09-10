#!/usr/bin/env python3
"""Generate the §§ 20–24 phonetic transcription control table."""

from pathlib import Path
import re


SOURCE = Path("capitulos/fonetica/01-transcripcion-y-vocales.tex")
OUTPUT = Path("docs/phonetic-control-20-24.md")


def read_group(text: str, start: int) -> tuple[str, int]:
    if text[start] != "{":
        raise ValueError(f"Expected group at offset {start}")
    depth = 0
    for index in range(start, len(text)):
        if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
            depth += 1
        elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[start + 1 : index], index + 1
    raise ValueError(f"Unclosed group at offset {start}")


def visual_reading(tex: str) -> str:
    replacements = {
        r"\rfeStressedMixedI": "ḯ",
        r"\rfeStressedMixedU": "ǘ",
        r"\rfeStressedPalatalA": "ą́",
        r"\rfeMixedI": "ï",
        r"\rfeMixedU": "ü",
        r"\rfePalatalA": "ą",
        r"\rfeRelaxedPalatal": "ę",
        r"\rfeRelaxedClosed": "ẹ",
        r"\rfeVeryPalatal": "ə",
        r"\rfeLong": ":",
    }
    result = tex
    for macro, value in replacements.items():
        result = result.replace(macro + " ", value)
        result = result.replace(macro, value)
    result = re.sub(
        r"\\rfeStress\{([^{}])\}\s?",
        lambda match: match.group(1) + "́",
        result,
    )
    result = result.replace("T", "θ").replace("S", "š").replace("N", "ŋ")
    return " ".join(result.split())


def paragraph_at(text: str, offset: int) -> str:
    markers = [
        (text.find(r"\subsection{} Los signos"), "20"),
        (text.find(r"\subsection{} En la distribución"), "21"),
        (text.find(r"\subsection{ bis}"), "21 bis"),
        (text.find(r"\subsection{} Éstas son"), "22"),
        (text.find(r"\subsection{} Hay cuatro"), "23"),
        (text.find(r"\subsection{} Tras ciertos"), "24"),
    ]
    valid = [(position, label) for position, label in markers if 0 <= position <= offset]
    return max(valid)[1] if valid else "?"


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    rows: list[tuple[str, str, str, str]] = []
    cursor = 0
    needle = r"\dialectform"
    while (position := text.find(needle, cursor)) >= 0:
        first_start = position + len(needle)
        searchable, second_start = read_group(text, first_start)
        while second_start < len(text) and text[second_start].isspace():
            second_start += 1
        typeset, cursor = read_group(text, second_start)
        rows.append(
            (paragraph_at(text, position), visual_reading(typeset), searchable, typeset)
        )

    lines = [
        "# Control de transcripción fonética: §§ 20–24",
        "",
        "Tabla regenerable para cotejar cada forma dialectal. La columna «lectura RFE» "
        "es una transliteración Unicode de control; el PDF conserva los glifos de Penny.",
        "",
        "## Inventario componible",
        "",
        "| Macro | Rasgo conservado |",
        "|---|---|",
        "| `\\rfeStress{x}` | acento de intensidad sobre la vocal |",
        "| `\\rfeLong` | cantidad larga, independiente del acento |",
        "| `\\rfeMixedI`, `\\rfeMixedU` | vocales mixtas o engoladas |",
        "| `\\rfePalatalA` | *a* palatal especial |",
        "| `\\rfeStressedMixedI`, `\\rfeStressedMixedU` | vocal mixta tónica |",
        "| `\\rfeRelaxedPalatal` | vocal final relajada palatal |",
        "| `\\rfeRelaxedClosed` | vocal final relajada muy cerrada |",
        "| `\\rfeVeryPalatal` | variante final muy palatal |",
        "",
        "## Formas etiquetadas",
        "",
        "| § | Lectura RFE control | Unicode buscable | Código TeX |",
        "|---:|---|---|---|",
    ]
    for paragraph, reading, searchable, typeset in rows:
        escaped_tex = typeset.replace("|", r"\|")
        lines.append(
            f"| {paragraph} | `{reading}` | `{searchable}` | `\\dialectform"
            f"{{{searchable}}}{{{escaped_tex}}}` |"
        )
    lines.extend(["", f"Total: **{len(rows)} formas etiquetadas**.", ""])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
