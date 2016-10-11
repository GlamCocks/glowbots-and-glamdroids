#!/usr/bin/env python

import scene
import structure
import opc
import time
import color_utils

class SceneDefault(scene.Scene):

    pulses = []
    pulse_interval = 20


    def start(self):
        pixels = self.build_pixels()

        interval_counter = 0
        start_time = time.time()

        self.add_pulse()

        while True:
            t = time.time() - start_time
            
            pixels = self.clean_pixels(pixels)

            if interval_counter >= self.pulse_interval:
                self.add_pulse()
                interval_counter = 0

            # Tail of pulses
            for pulse in self.pulses:
                # no tail
                i = len(pulse.tail.connections)

                if len(pulse.tail.connections) == 0:
                    continue

                for connection in pulse.tail.connections:
                    pixels[self.visible_connection(connection).absolute_position()] = color_utils.color_ratio(self.color, self.tail_alpha[i-1])
                    i -= 1

            for pulse in self.pulses:
                if pulse.dead == False:
                    pixels[self.visible_connection(pulse.connection).absolute_position()] = self.color

            self.client.put_pixels(pixels, channel=0)
            self.move_pulses()

            time.sleep(1.0 / self.fps)
            interval_counter += 1