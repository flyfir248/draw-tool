from PIL import Image, ImageDraw

# Create a blank image
image = Image.new('RGB', (400, 400), (255, 255, 255))

# Create a draw object
draw = ImageDraw.Draw(image)

# Start a line at (100, 100)
x1, y1 = 100, 100

while True:
    # Get the next point for the line
    x2, y2 = map(int, input('Enter the next point for the line (x y): ').split())

    # Draw the line
    draw.line((x1, y1, x2, y2), fill=(0, 0, 0))

    # Update the starting point for the next line
    x1, y1 = x2, y2

    # Display the image
    image.show()