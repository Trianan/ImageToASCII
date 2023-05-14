from PIL import Image
from datetime import datetime

print('ImageToASCII: Version alpha_0.1')
img_file = input('Enter filepath of image: ')

# Load the image
img = Image.open(img_file)

# Convert the image to grayscale
gray_img = img.convert("L")

# Get the width and height of the image
width, height = gray_img.size

# Create a 2D list to store the lightness values of each pixel
pixels = [[0 for y in range(height)] for x in range(width)]

# Loop through each pixel and store its lightness value in the list
for x in range(width):
    for y in range(height):
        pixels[x][y] = gray_img.getpixel((x, y))

# Print the list of lightness values
for line in pixels:
    print(line)

converted_img = []
chars = "$@%&#*\{?-+<!:^. "[::-1] # Reverse string
for line in pixels:
    converted_line = []
    for value in line:
        last_i, char_i = -1, 0
        for i in range(15, 256, 15):
            if value > last_i and value <= i:
                converted_line.append(chars[char_i])
            else:
                char_i += 1
            last_i = i
    converted_img.append(converted_line)

with open(f'./output_{datetime.now()}.txt', 'a') as output_file:
    for line in converted_img:
        line_str = '  '.join(line)
        print(line_str)
        output_file.write(line_str + '\n')