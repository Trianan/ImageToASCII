from PIL import Image
from datetime import datetime
import random

print('''
                                                                                    
                    . $ $ $ $ $ $ $   . $         . $   . $ $ $ $ $ $ $                    
                    . $ $ $ $ $ $ $   . $ $     . $ $   . $ $ $ $ $ $ $                    
                          . $         . $ $ $ $ $ $ $   . $                                
                          . $         . $ . $ $ $ . $   . $       . $ $                    
                          . $         . $   . $   . $   . $       . $ $                    
                          . $         . $   . $   . $   . $         . $                    
                    . $ $ $ $ $ $ $   . $   . $   . $   . $ $ $ $ $ $ $                    
                    . $ $ $ $ $ $ $   . $   . $   . $   . $ $ $ $ $ $ $                    
                                                                                           
                            . $ $ $ $ $ $ $   . $ $ $ $ $ $ $                              
                            . $ $ $ $ $ $ $   . $ $ $ $ $ $ $                              
                                  . $         . $         . $                              
                                  . $         . $         . $                              
                                  . $         . $         . $                              
                                  . $         . $         . $                              
                                  . $         . $ $ $ $ $ $ $                              
                                  . $         . $ $ $ $ $ $ $                              
                                                                                           
  . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $  
  . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $  
  . $         . $   . $               . $                     . $               . $        
  . $         . $   . $ $ $ $ $ $ $   . $                     . $               . $        
  . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $                     . $               . $        
  . $ $ $ $ $ $ $               . $   . $                     . $               . $        
  . $         . $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $  
  . $         . $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $   . $ $ $ $ $ $ $  

''')
print('\nImageToASCII: Version alpha_0.2\n')

while True:

    img_file = input('Enter filepath of image (q to quit): ')
    if img_file == 'q':
        break
    
    img_loaded = False
    try:
        img = Image.open(img_file)
        img_loaded = True
    except:
        print('Could not load image from given filepath.')

    if img_loaded:
        gray_img = img.convert("L")
        width, height = gray_img.size

        pixels = [[0 for column in range(width)] for row in range(height)]
        for row in range(height):
            for column in range(width):
                pixels[row][column] = gray_img.getpixel((column, row))
        for line in pixels:
            print(line)

        ascii_img = []
        chars = "$@%&#*\\{?-+<!:^. "[::-1] # Reverse string
        for line in pixels:
            ascii_line = []
            for value in line:
                last_i, char_i = -1, 0
                for i in range(15, 256, 15):
                    if value > last_i and value <= i:
                        ascii_line.append(chars[char_i])
                    else:
                        char_i += 1
                    last_i = i
            ascii_img.append(ascii_line)

        spacing = int(input('Enter the number of spaces between characters: '))
        with open(f'./output/{img_file.split("\\")[-1]}_ASCII_{random.randint(0,100)}.txt', 'a') as output_file:
            for line in ascii_img:
                line_str = (' '*spacing).join(line)
                print(line_str)
                output_file.write(line_str + '\n')
    
    run_again = input('Convert another image? (y/n): ')
    if run_again == 'n':
        break

print('Quitting ImageToASCII...')