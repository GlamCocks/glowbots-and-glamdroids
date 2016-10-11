#!/usr/bin/env python

import scene
import structure
import opc
import time
import color_utils

class SceneExplosion(scene.Scene):

    pulses = []
    pulse_interval = 10


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
                if pulse.exploded:
                    pixels[self.visible_connection(pulse.connection).absolute_position()] = color_utils.white_pixel
                else:
                    pixels[self.visible_connection(pulse.connection).absolute_position()] = self.color

            self.client.put_pixels(pixels, channel=0)

            self.move_pulses()

            time.sleep(1.0 / self.fps)
            interval_counter += 1
 

    #override
    def add_pulse(self): 
        connection = structure.Connection(0, 0)
        pulse = ExplosivePulse(connection)

        self.pulses.append(pulse)


    #override
    def move_pulses(self):
        super(SceneExplosion, self).move_pulses()

        # Search for explosions!

        self.pulses = sorted(self.pulses)

        last_pulse = None
        last_position = 0

        new_pulses = []

        for pulse in self.pulses:
            # If pulse has exploded, do not re-add it (remove)
            if pulse.exploded:
                continue
            # If the two positions are == delta abs 1 AND opposite direction, explode!
            if isinstance(last_pulse, ExplosivePulse) and abs(last_position - pulse.connection.absolute_position()) <= 1 and (pulse.direction != last_pulse.direction):
                pulse.exploded = True
                last_pulse.exploded = True

            last_pulse = pulse
            last_position = pulse.connection.absolute_position()

            new_pulses.append(pulse)

        self.pulses = new_pulses



class ExplosivePulse(structure.Pulse):

    exploded = False