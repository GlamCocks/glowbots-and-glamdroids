#!/usr/bin/env python

NB_PIXELS_STRIP = 64 # number of pixels by strip
NB_PIXELS_TAIL = 3 # number of pixel for a pulse's tail

class Strip(object):

    def __init__(self, index, numberOfLeds):
        self.index = index
        self.numberOfLeds = numberOfLeds   

    def __repr__(self):
        return "Strip " + str(self.index) + "[" + str(self.numberOfLeds) + "]"


class Connection(object):

    def __init__(self, stripIndex, position):
        self.stripIndex = stripIndex
        self.position = position

    def absolute_position(self):
        return self.position + self.stripIndex * NB_PIXELS_STRIP

    def __repr__(self):
        return "Connection " + str(self.stripIndex) + "[" + str(self.position) + "] [" + str(self.absolute_position()) + "]"


class Junction(object):

    # A to B (one direction only)
    def __init__(self, fromConnection, toConnection, direction, weight):
        self.fromConnection = fromConnection
        self.toConnection = toConnection
        self.direction = direction
        self.weight = weight # min 1 - bigger number multiply chance to be selected

    def __repr__(self):
        return "Junction " + str(self.fromConnection.absolute_position()) + ">" + str(self.toConnection.absolute_position()) + "(dir. " + str(self.direction) + ")"


class Overlap(object):

    def __init__(self, topConnection, bottomConnection):
        self.topConnection = topConnection
        self.bottomConnection = bottomConnection

    def __repr__(self):
        return "Overlap " + str(self.topConnection.absolute_position()) + " over " + str(self.bottomConnection.absolute_position())


class Pulse(object):

    def __init__(self, connection):
        self.connection = connection
        self.direction = +1
        self.switched = False
        self.tail = Tail()
        self.dead = False

    def __repr__(self):
        return "Pulse (" + str(self.connection) + ") - switched:" + str(self.switched) + " dead:" + str(self.dead)

    def __cmp__(self, other):
        if hasattr(other, 'connection'):
            return self.connection.absolute_position().__cmp__(other.connection.absolute_position())


class Tail(object):

    def __init__(self):
        self.connections = []

    def add_connection(self, newConnection):
        if len(self.connections) == NB_PIXELS_TAIL:
            self.connections.pop(0)

        self.connections.append(newConnection)

    def pop_connection(self):
        if len(self.connections) > 0:
            self.connections.pop(0)
            
    def __repr__(self):
        return "Tail" 
