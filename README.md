# Auto Accept script for Counter-Strike : Global Offensive

## Introduction

Counter-Strike : Global Offensive (abbreviated **CS:GO**) is a multiplayer shooting game developped by Valve and available on Steam.

When you start an online ranked game in CS:GO, you wait for a game to be found, the matchmaking system is putting you with other players. Once the game is found, every player have twenty seconds to accept it by clicking on a big green button. If the delay is expired for at least one player, the game is canceled for all and the research continues.

However, matchmaking process can be sometimes long, and you may want to leave your computer while the matchmaking system is operating, but you fear that a game is found while you are away, making you unable to accept it and punishing your mates, and maybe getting penalties for being away from keyboard.

That's where this script comes in.

## How does it works ?

This python script will place your mouse over the screen coordinates of the big green accept button, and iterate a click every second, triggering the accept button automatically while you are away, removing any inconvenience due to an absence of acceptation.

![](https://i.imgur.com/wvUl1VK.png)

Whenever you move your mouse, the script will be paused for 5 seconds, before relocating your mouse onto the green button and continue clicking. This lets you the time to *Alt + Tab* & close the script using *Ctrl + C*.

## Prerequisites

To run this script, you will need any version of Python installed on your computer.

**[Install python](https://www.python.org/downloads/)**

You will also need the **pynput** library, that can be installed using **PIP**.

**[Install PIP](https://pip.pypa.io/en/stable/installing/)**

Then run this code snipped in any terminal :

<code>pip install pynput</code>

## Attention

This code is functional for a 1920x1080 monitor. If your monitor definition is different, I recommend you to use the **[getpos.py](https://github.com/LoicE5/GetPos)** script in order to properly locate your green button coordinates, than edit the following variable in the code.

<code>acceptPos = (947,596) # Coordinates tested for 1920x1080 monitor</code>

## Notes

If you have any questions or keys of improvement, you can reach me [here](https://www.linkedin.com/in/loic-etienne/) or directly on GitHub !