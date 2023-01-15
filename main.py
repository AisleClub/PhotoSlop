#            $$\                  $$\                         $$\       $$\                     
#            $$ |                 $$ |                        $$ |      $$ |                    
#   $$$$$$\  $$$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$\ $$$$$$$\  $$ | $$$$$$\   $$$$$$\  
#  $$  __$$\ $$  __$$\ $$  __$$\\_$$  _|  $$  __$$\ $$  _____|$$  __$$\ $$ |$$  __$$\ $$  __$$\ 
#  $$ /  $$ |$$ |  $$ |$$ /  $$ | $$ |    $$ /  $$ |\$$$$$$\  $$ |  $$ |$$ |$$ /  $$ |$$ /  $$ |
#  $$ |  $$ |$$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ | \____$$\ $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |
#  $$$$$$$  |$$ |  $$ |\$$$$$$  | \$$$$  |\$$$$$$  |$$$$$$$  |$$ |  $$ |$$ |\$$$$$$  |$$$$$$$  |
#  $$  ____/ \__|  \__| \______/   \____/  \______/ \_______/ \__|  \__|\__| \______/ $$  ____/ 
#  $$ |                                                                               $$ |      
#  $$ |                                                                               $$ |      
#  \__|                                                                               \__|
# 
#

from PIL import Image, ImageFilter
import os
import random
import time
import winsound
directory = os.getcwd()
files = []

for file in os.listdir(): 
  if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.svg') :
    files.append(file)

for i in files : 
  print(str(int((files.index(i)/len(files))*100)) + "%")
  
  img = Image.open(i)

  # Blurring the image
  im1 = img.filter(ImageFilter.GaussianBlur(20))

  os.remove(i)
  
# Shows the image in image viewer
  pos = i.find(".")
  i = i[0:pos]
  name = str(i)
  im1.save(name+'.png', "PNG")

print("100%")
print("  ")
print("          $$\                  $$\                         $$\       $$\                   $$\     $$\ ")
print("          $$ |                 $$ |                        $$ |      $$ |                  $  |    $$ |")
print(" $$$$$$\  $$$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$\ $$$$$$$\  $$ | $$$$$$\   $$$$$$\\_/$$$$$$$ |")
print("$$  __$$\ $$  __$$\ $$  __$$\\_$$  _|  $$  __$$\ $$  _____|$$  __$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$ |")
print("$$ /  $$ |$$ |  $$ |$$ /  $$ | $$ |    $$ /  $$ |\$$$$$$\  $$ |  $$ |$$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |")
print("$$ |  $$ |$$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ | \____$$\ $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |")
print("$$$$$$$  |$$ |  $$ |\$$$$$$  | \$$$$  |\$$$$$$  |$$$$$$$  |$$ |  $$ |$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$ |")
print("$$  ____/ \__|  \__| \______/   \____/  \______/ \_______/ \__|  \__|\__| \______/ $$  ____/  \_______|")
print("$$ |                                                                               $$ |                ")
print("$$ |                                                                               $$ |                ")
print("\__|                                                                               \__|                ")
print("                                                                                                       ")


for filename in os.listdir(directory): 
  if filename.endswith(".png"):
      frequency = random.randint(500, 8000)  
      # random frequency between 300 and 3000 Hz
      duration = random.randint(100, 6000)  
      # random duration between 100 and 1000 ms
      time.sleep(2)
      os.startfile(filename)
      winsound.Beep(frequency, duration)
