'''
Grayscale images
'''

from PIL import Image
import os

# Set read and save path 
r_path = r"C:\Users\DELL\Desktop\valPics"
s_path = r"C:\Users\DELL\Desktop\valPics_gray"

# Read images from r_path, convert them to grayscale and save them to s_path
for filename in os.listdir(r_path):
    img = Image.open(os.path.join(r_path,filename))
    gray = img.convert('L')
    gray.save(os.path.join(s_path,filename))
    

