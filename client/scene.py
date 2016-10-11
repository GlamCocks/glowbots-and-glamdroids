#!/usr/bin/env python

import structure
import color_utils
import random

class Scene(object):

    def __init__(self, client):
        self.strips = []
        self.junctions = []
        self.overlaps = []
        self.pulses = []
        self.fps = 1.0
        self.client = client
        self.color = color_utils.blue_pixel
        self.tail_alpha = [0.7, 0.5, 0.3]


    def build_pixels(self):
        pixels = []

        for i in range(structure.NB_PIXELS_STRIP * len(self.strips)):
            pixels.append(color_utils.black_pixel)

        return pixels


    def clean_pixels(self, pixels):
        for i in range(structure.NB_PIXELS_STRIP * len(self.strips)):
            pixels[i] = color_utils.black_pixel

        return pixels


    def next_physical_connection(self, connection, direction):
        strip = self.strips[connection.stripIndex]

        if connection.position + direction < strip.numberOfLeds and connection.position + direction >= 0:
            return structure.Connection(connection.stripIndex, connection.position + direction)
        elif connection.stripIndex + 1 < len(self.strips):
            return structure.Connection(connection.stripIndex + 1, 0)
        else:
            return None


    def next_strip_connection(self, connection, direction):
        strip = self.strips[connection.stripIndex]

        if connection.position + direction < strip.numberOfLeds and connection.position + direction >= 0:
            return structure.Connection(connection.stripIndex, connection.position + direction)
        else:
            return None


    def next_junctions(self, connection, direction):
        strip = self.strips[connection.stripIndex]
        valid_junctions = []

        for junction in self.junctions:
            if connection.absolute_position() == junction.fromConnection.absolute_position():
                valid_junctions.append(junction)

        return valid_junctions # returns junctions


    def next_connection_or_junction(self, connection, direction):
        valid_junctions = self.next_junctions(connection, direction)

        if len(valid_junctions) > 0: 
            # Take care of weighted choices
            weighted_valid_junctions = []

            for junction in valid_junctions:
                for i in range(junction.weight):
                    weighted_valid_junctions.append(junction)

            return random.choice(weighted_valid_junctions) # returns junction
        else:
           return self.next_strip_connection(connection, direction) # returns connection


    def visible_connection(self, connection):
        for overlap in self.overlaps:
            if overlap.bottomConnection.absolute_position() == connection.absolute_position():
                return overlap.topConnection

        return connection


    def add_pulse(self): 
        connection = structure.Connection(0, 0)
        pulse = structure.Pulse(connection)

        self.pulses.append(pulse)


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
                keep_searching = True

                while keep_searching:
                    next_item = self.next_connection_or_junction(pulse.connection, pulse.direction)

                    # Next is a simple connection
                    if isinstance(next_item, structure.Connection):
                        pulse.connection = next_item
                        keep_searching = False

                    # Next is a junction
                    elif isinstance(next_item, structure.Junction):
                        junction = next_item

                        # If the junction is on the same strip AND direction is the opposite, we skip it (no u-turn!)
                        if pulse.connection.stripIndex == junction.toConnection.stripIndex and pulse.direction != junction.direction:
                            continue

                        # If the junction leads to another strip
                        if pulse.connection.stripIndex != junction.toConnection.stripIndex:
                            pulse.direction = junction.direction
                            pulse.switched = True

                        # Done searching another valid junction
                        pulse.connection = junction.toConnection
                        keep_searching = False

                    # Next is nothing: at the end of a strip that isn't connected to another one
                    elif next_item == None:
                        keep_searching = False
                        pulse.dead = True

            newPulses.append(pulse)

        self.pulses = newPulses
