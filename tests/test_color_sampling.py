import pytest
from PIL import Image

from png2svg.color_sampling import average_color


def test_average_color_returns_mean_rgb():
    """test average colour of 2 pixels"""
    image = Image.new("RGB", (2, 1))
    image.putpixel((0, 0), (100, 150, 200))
    image.putpixel((1, 0), (200, 100, 50))

    result = average_color(image, [(0, 0), (1, 0)])

    assert result == (150, 125, 125)


def test_average_color_rounds_mean_to_integers():
    """test if we manage to round to inferior integer"""
    image = Image.new("RGB", (2, 1))
    image.putpixel((0, 0), (0, 0, 0))
    image.putpixel((1, 0), (1, 1, 1))

    assert average_color(image, [(0, 0), (1, 0)]) == (0, 0, 0)


def test_average_color_rejects_empty_coordinates():
    """test if coordinates are empty"""
    image = Image.new("RGB", (1, 1))

    with pytest.raises(ValueError, match="coordinates must not be empty"):
        average_color(image, [])
