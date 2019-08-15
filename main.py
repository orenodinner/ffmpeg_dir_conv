import os
import shutil
import sys
from tqdm import tqdm
import glob
import re
from tkinter import filedialog
import string
import psutil
import subprocess

dir = 'F:/'
fld = filedialog.askdirectory(initialdir = dir) 



if os.path.exists(fld) == True:
    print("Path_Ok")
def  fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for Afile in files:
            yield os.path.join(root, Afile)


text_path = "encoding.txt"
print("GURUGURU")
for i, Zfile in enumerate( tqdm(fild_all_files(fld))):
    if os.path.isfile(Zfile):
        print(i)
        print(Zfile)
        with open(text_path, mode='a') as f:
            dos_file = Zfile.replace("/" , "\\" )
            f.write(dos_file + "\n")
            py_file = Zfile.replace("\\","/")
            b_name = os.path.basename(py_file)
            ffmpeg_name = str(os.path.splitext(b_name)[0])
            with open(py_file + ".cmd", mode='w') as f:
                f.write("cd /d %~dp0" + "\n")
                f.write("ffmpeg -i " + dos_file +" -c:v libx265 -c:a copy "+ "F:\VP9\\" + ffmpeg_name +".mp4"+"\n")
                f.write("del /q " + dos_file +"\n" )
                f.write("cd\n")
                f.write("pause\n")
            cpu_percent = psutil.cpu_percent(interval=20)
            print(cpu_percent,end="")
            while cpu_percent > 80:
                cpu_percent = psutil.cpu_percent(interval=100)
                print(cpu_percent,end="")
            subprocess.Popen("start "+dos_file+ ".cmd" ,shell=True)
            print("next")

        print(dos_file)