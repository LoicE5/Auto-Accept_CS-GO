#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pynput
import time
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard = KeyboardController()
mouse = MouseController()

acceptPos = (947,596)

def main():
    print('Initializing...')
    for i in range(3):
        print(str(i+1))
        time.sleep(1)
    mouse.position = acceptPos

    while(True):

        if(mouse.position != acceptPos):
            print('Waiting 5 seconds')
            for i in range(5):
                print(str(i+1))
                time.sleep(1)
            mouse.position = acceptPos
        else:
            mouse.click(Button.left, 1)
            print('Click !')
            time.sleep(1)

main()