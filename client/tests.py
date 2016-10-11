#!/usr/bin/env python

import scene_test
import scene_generator
import opc
import time 
import math

# Create OPC client
opc = opc.Client('127.0.0.1:7890')

# numLEDs = 50

# while True:
#     for i in range(numLEDs):
#         pixels = [ (0,0,0) ] * numLEDs
#         pixels[i] = (255, 255, 255)
#         opc.put_pixels(pixels)
#         time.sleep(0.005)

# opc = opc.Client('127.0.0.1:7890')
numLEDs = 50 * 1

t = 0

while True:
    t += 0.4
    brightness = int(min(1, 1.25 + math.sin(t)) * 255)
    frame = [ (brightness, brightness, brightness) ] * numLEDs
    opc.put_pixels(frame)
    time.sleep(0.05) 

# numStrings = 1

# string = [ (255, 255, 255) ] * 64
# for i in range(7):
#     string[10 * i] = (255, 0, 0)

# # Immediately display new frame
# pixels = string * numStrings
# opc.put_pixels(pixels)
# opc.put_pixels(pixels)

# numLEDs = 50

# black = [ (0,0,0) ] * numLEDs
# white = [ (255,255,255) ] * numLEDs

# while True:
#     opc.put_pixels(white)
#     time.sleep(0.05) 
#     opc.put_pixels(black)
#     time.sleep(0.05)


# Create a scene for tests
# scene = scene_test.SceneTest(opc)
# scene.fps = 2 # Make sure to have a low FPS if running short tests (junctions, overlaps)
# scene_generator.generate(scene)

# Junctions
    # Show the different junctions of the scene
    # Green is the origin LED and red is the destination LED
    # parameters: 
    #  - animated (Boolean): True value will display the junctions one by one, False will display all of them
# scene.show_junctions(True) 

# Overlaps
    # Show the overlaps of LEDs (2 strips above each other will hide 1 LED)
    # Green is the LED on top and red is the LED under it
    # NOTE: If you configure your 3D axes to show only x,y and if you see a red LED, it means something is wrong (wrong mapping)
    # parameters: 
    #  - animated (Boolean): True value will display the overlaps one by one, False will display all of them

# scene.show_overlaps(True) 

# Entire scene
    # Show the entire scene
    # All the LEDs of the scene are set to white
    # parameters: 
    #  - animated (Boolean): True value will turn on the LEDs one by one, False will display all of them at the same time
    #  - withOverlapped (Boolean): True value will also display the LEDs overlapped by another strip.

# scene.show_entire_scene(True, True)

# Random path
    # Generate and show a random path (based on constraints)

# scene.show_random_path()
