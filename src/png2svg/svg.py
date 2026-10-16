

def write_svg(
    output,
    width,
    height,
    hexagons,
):
    """Write a collection of colored hexagons to an SVG file."""
    lines = [
        (
            '<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}">'
        )
    ]

    for vertices, color in hexagons:
        points = " ".join(f"{x},{y}" for x, y in vertices)
        fill = "#{:02x}{:02x}{:02x}".format(*color)
        lines.append(f'<polygon points="{points}" fill="{fill}" />')

    lines.append("</svg>")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")