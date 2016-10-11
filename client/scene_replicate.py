#!/usr/bin/env python

import scene
import structure
import opc
import time
import color_utils

class SceneReplicate(scene.Scene):

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


    #override
    def move_pulses(self):
        newPulses = []

        for pulse in self.pulses:

            # Tail of the pulse
            if pulse.dead == False:
                pulse.tail.add_connection(pulse.connection)
            else:
                pulse.tail.pop_connection()

                if len(pulse.tail.connections) > 0:
                    newPulses.append(pulse)

                continue

            # If recently switched, force next strip connection (no u-turn!)
            if pulse.switched:                    
                pulse.connection = self.next_strip_connection(pulse.connection, pulse.direction)
                pulse.switched = False
            else:
                junctions = self.next_junctions(pulse.connection, pulse.direction)

                for junction in junctions:
                    # If the junction is on the same strip AND direction is the opposite, we skip it (no u-turn!)
                    new_pulse = structure.Pulse(junction.toConnection)
                    new_pulse.direction = junction.direction
                    new_pulse.switched = True
                    newPulses.append(new_pulse)

                if len(junctions) > 0:
                    pulse.dead = True
                else:
                    next_connection = self.next_strip_connection(pulse.connection, pulse.direction)

                    if next_connection != None:
                        pulse.connection = next_connection
                    else:
                        pulse.dead = True

            newPulses.append(pulse)

        self.pulses = newPulses