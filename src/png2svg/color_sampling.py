

def average_color(
    image,
    coordinates,
):
    """Return the average RGB color of the pixels at the given coordinates."""
    if not coordinates:
        raise ValueError("coordinates must not be empty")

    pixels = [image.getpixel((x, y)) for x, y in coordinates]

    red = sum(pixel[0] for pixel in pixels) / len(pixels) #pixel[0] = red
    green = sum(pixel[1] for pixel in pixels) / len(pixels) #pixel[1] = green
    blue = sum(pixel[2] for pixel in pixels) / len(pixels) #pixel[2] = blue

    return round(red), round(green), round(blue)
