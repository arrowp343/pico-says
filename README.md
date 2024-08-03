# <s>Simon</s> Pico Says

![testenv](https://raw.githubusercontent.com/arrowp343/pico-says/main/pictures/testenv.jpeg)

## What is this?

This is a project, I started as a christmas gift for my niece. It's a Raspberry Pi Pico, some LEDs, Buttons, a Buzzerand about 15 hours of coding and debugging (so far).

Most people will remember this game, maybe as toy from the childhood or some sort of a minigame in another video game. The goal is to memorize the random sequence of colors flashed at the beginning of a round and then input the same sequence without a mistake.

Here is a prototype of how the game should look like, when it's done:

![prototype](https://raw.githubusercontent.com/arrowp343/pico-says/main/pictures/prototype.JPEG)

And here is how far I have gotten so far:


[![youtube_link](https://img.youtube.com/vi/F5fe8uTFr4M/0.jpg)](https://youtu.be/F5fe8uTFr4M?si=KiheSRbV42N51B9u)

https://www.youtube.com/watch?v=F5fe8uTFr4M

As soon as I am finished coding, I will soldier all the components to a circuit board and make it as children-safe as possible (she is 4). But there are still some ideas I want to implement.

## Done:

- [x] Make it work
- [x] dimmed LEDs so my eyes won't burn 

## Doing:




## To be Done:
- [ ] implement difficulty switch
- [ ] add resistors before 7segment-display and party-leds to dim them
- [ ] add some more melodies to play, after you won / lost the game
- [ ] add some animations to leds and / or 7segment display
- [ ] draw a circuit plan for show off


# How to use it

First, if you want to reproduce it exactly how I made it (of course you can leave some elements like the buzzer or party-leds out, if you don't need / want them), you will need the following components: 

- 1x breadboard and some jumper wires
- 1x Raspberry Pi Pico (W is not necessary)
- 4x different color LEDs
- 4x buttons (best case with colors fitting to the leds)
- 2x party LEDs
- 1x 7segment-display
- 1x switch
- some resistors (I made it without resistors so far)

![early_testenv](https://raw.githubusercontent.com/arrowp343/pico-says/main/pictures/early_testenv.jpeg)

A detailed circuit plan is in schedule. But until then, maybe these instructions could be helpful:
Basically you need to connect all negative sides of the LEDs, the ground pin of the 7segment-display and one side of the button to the ground pin of the Raspberry Pi Pico. Each other pins are connected to a seperate gpio pin of the Pico.

You will most likely have to adjust the pin mapping in hardware/gpio_config.py and hardware/buzzer.py to tell the game, which pin is connected to which component.

After the hardware comes the software transfare. All you need to do, is flash your Pico (if you use it for the first time, otherwise you can just delete all the files on it). There is a very nice [quick start guide for the pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0) from the Raspberry Pi Foundation itself, which I can highly recommend. You don't have to do the whole guide. Follow the instructions until you manage to make the onboard LED on the pico blink. Then you'll know, you can put code on the Pico and execute it.

Last step is, to download the source code and upload it to the Pico. If you use Thonny, go to **View -> Files** to make the file browser visible. Then browse to your download folder and right-click on each file in the sourcecode folder and click **-> Upload to /**. If you did everything right, the */main.py* should be in the root directory of the Pico.

With this setup you should be able to disconnect the Pico from your pc and plug it into a battery pack for example and play it.

Feel free to contact me, if you stuck somewhere. If you made it work, I'd be pleased to see how you did it. 

