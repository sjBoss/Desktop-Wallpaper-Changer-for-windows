import os
import ctypes
import shutil
import threading
import os
import random


def thre():
   global x
   location = open("C:\\dist\\location.txt")
   loc_string = location.read()
   
   image_list = os.listdir(loc_string)
   x = random.randint(0,len(image_list)-1)
   image = image_list[x]
   SPI_SETDESKTOPWALLPAPER=20
   ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0,loc_string+"\\" + image, 3)

def change_image():
   THREAD = threading.Thread(target = thre)
   THREAD.start()

change_image()
