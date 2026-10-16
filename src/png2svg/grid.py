
import math


def hexagon_centers(
    width: int,
    height: int,
    radius: float,
) -> list[tuple[float, float]]:
    """Return centers of hexagons covering a rectangular image."""
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    if radius <= 0:
        raise ValueError("radius must be positive")

    horizontal_spacing = 1.5 * radius
    vertical_spacing = math.sqrt(3) * radius
    vertical_offset = vertical_spacing / 2

    centers = []
    column = 0
    x = -radius

    while x <= width + radius:
        # Alternate columns are shifted vertically.
        y = -vertical_offset + (column % 2) * vertical_offset

        while y <= height + vertical_offset:
            centers.append((x, y))
            y += vertical_spacing

        column += 1
        x = -radius + column * horizontal_spacing

    return centers
