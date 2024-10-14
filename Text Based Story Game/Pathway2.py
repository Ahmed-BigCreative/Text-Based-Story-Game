from ctypes.wintypes import ULONG
from time import sleep
import random
skip = False
import sys,time
from tkinter import N


def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)



def path_2():
    sleep(2)
    print("Welcome to pathway two, you have joined the war on the side of the witches")
    sprint("3 days later...")
    sprint("You wake up and open your window")

