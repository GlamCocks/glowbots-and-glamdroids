#!/usr/bin/env python

import scene
import structure
import opc
import time
import color_utils
   
class SceneTest(scene.Scene):

    # Animations for test

    def show_overlaps(self, animated): 
        pixels = self.build_pixels()

        for overlap in self.overlaps:
            if animated:
                pixels = self.clean_pixels(pixels)

            pixels[overlap.topConnection.absolute_position()] = color_utils.green_pixel
            pixels[overlap.bottomConnection.absolute_position()] = color_utils.red_pixel

            if animated:
                self.client.put_pixels(pixels, channel=0)
                time.sleep(1.0 / self.fps)

        if animated == False:
            self.client.put_pixels(pixels, channel=0)
            time.sleep(1.0 / self.fps)


    def show_junctions(self, animated):
        pixels = self.build_pixels()

        for junction in self.junctions:
            if animated:
                pixels = self.clean_pixels(pixels)

            pixels[self.visible_connection(junction.fromConnection).absolute_position()] = color_utils.green_pixel
            pixels[self.visible_connection(junction.toConnection).absolute_position()] = color_utils.red_pixel

            if animated:
                self.client.put_pixels(pixels, channel=0)
                time.sleep(1.0 / self.fps)

        if animated == False:
            self.client.put_pixels(pixels, channel=0)
            time.sleep(1.0 / self.fps)


    def show_entire_scene(self, animated, withOverlapped):
        keep_moving = True 
        currentConnection = structure.Connection(0, 0)
        pixels = self.build_pixels()
        direction = +1

        while keep_moving:

            if withOverlapped:
                pixels[currentConnection.absolute_position()] = white_pixel
            else:
                pixels[self.visible_connection(currentConnection).absolute_position()] = white_pixel

            if animated:
                self.client.put_pixels(pixels, channel=0)
                time.sleep(1.0 / self.fps)

            currentConnection = self.next_physical_connection(currentConnection, direction)

            if currentConnection == None:
                keep_moving = False

        if animated == False:
            self.client.put_pixels(pixels, channel=0)
            time.sleep(1.0 / self.fps)

        print "Entire scene: done."


    def show_random_path(self):
        pixels = self.build_pixels()

        self.add_pulse()

        time.sleep(1.0 / self.fps)

        while len(self.pulses) > 0:

            for pulse in self.pulses:
                pixels[self.visible_connection(pulse.connection).absolute_position()] = self.color
                self.client.put_pixels(pixels, channel=0)

            self.move_pulses()

            time.sleep(1.0 / self.fps)

        print "Random path: done."