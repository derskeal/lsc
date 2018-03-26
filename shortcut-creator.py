#!/usr/bin/ python

import sys
import os

from tkinter import Tk
from tkinter import filedialog


shebang = str("#!/usr/bin/env xdg-open")

declarer = str("[Desktop Entry]")

AppType = str("Type=Application")
Terminal = str("Terminal=false")

ShortcutName = str("Name=") #Name of Shortcut
Exec = str("Exec=") #path to executable
Icon = str("Icon=") #path to icon
Comment = str("Comment=") #optional comment




print("Python Desktop Shortcut Creator for Kali Linux\n")
thename = str(input("Please enter the name of the application:\n"))
ShortcutName = ShortcutName+ thename
#print(ShortcutName)

print("\nPlease choose the file/binary to be executed: ")
filename = filedialog.askopenfilename()

print(filename)
Exec = Exec + filename


print("\nPlease choose an icon for the shortcut: ")
shortcutfile = filedialog.askopenfilename()
print(shortcutfile)
Icon = Icon + shortcutfile


print("\nPlease enter a comment for the shorcut(optional, press enter to skip): \n")
Comment2 = str(input())
#print(Comment2)
Comment = Comment + Comment2


# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = filedialog.askdirectory() # show an "Open" dialog box and return the path to the selected file
# print(filename)

os.chdir("/home/derskeal/Desktop/")
file = os.getcwd()+"/"+thename+".desktop"
with open(file, 'w') as f:
    f.writelines(shebang)
    f.write("\n")
    f.writelines('\n')
    f.writelines(declarer)
    f.write("\n")
    f.writelines(AppType)
    f.write("\n")
    f.writelines(Terminal)
    f.write("\n")
    f.writelines(Exec)
    f.write("\n")
    f.writelines(ShortcutName)
    f.write("\n")
    f.writelines(Icon)
    f.write("\n")
    f.writelines(Comment)

os.system("chmod 777 "+thename+".desktop")
#os.system("mv "+thename+".desktop /home/derskeal/Desktop/"+thename+".desktop")
