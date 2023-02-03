from PIL import Image
from tkinter.filedialog import *

filepath = askopenfilename()
picture = Image.open(filepath)
picture.save("Compressed.jpg", "JPEG", optimize=True, quality=30) 