from pathlib import Path

from png2svg.svg import write_svg


def test_write_svg_creates_file_with_hexagon(tmp_path: Path) -> None:
    output = tmp_path / "output.svg"

    write_svg(
        output,
        width=100,
        height=100,
        hexagons=[
            ([(50, 25), (72, 37), (72, 63), (50, 75), (28, 63), (28, 37)], (255, 0, 0))
        ],
    )

    content = output.read_text(encoding="utf-8")

    assert "<svg" in content
    assert "<polygon" in content
    assert "#ff0000" in content


def test_write_svg_escapes_and_closes_svg_document(tmp_path: Path) -> None:
    output = tmp_path / "output.svg"

    write_svg(output, width=20, height=30, hexagons=[])

    content = output.read_text(encoding="utf-8")

    assert 'width="20"' in content
    assert 'height="30"' in content
    assert content.strip().endswith("</svg>")
