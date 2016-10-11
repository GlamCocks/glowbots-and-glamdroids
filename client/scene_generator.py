#!/usr/bin/env python

import scene
import structure

# Populate scene

def generate(newScene):
    newScene.strips.append(structure.Strip(0, 64))
    newScene.strips.append(structure.Strip(1, 29))
    newScene.strips.append(structure.Strip(2, 64))
    newScene.strips.append(structure.Strip(3, 29))
    newScene.strips.append(structure.Strip(4, 64))
    newScene.strips.append(structure.Strip(5, 22))
    newScene.strips.append(structure.Strip(6, 43))
    newScene.strips.append(structure.Strip(7, 29)) 
    newScene.strips.append(structure.Strip(8, 41))
    newScene.strips.append(structure.Strip(9, 43))
    newScene.strips.append(structure.Strip(10, 64))
    newScene.strips.append(structure.Strip(11, 43))

    newScene.overlaps.append(structure.Overlap(structure.Connection(0, 50), structure.Connection(3, 13)))
    newScene.overlaps.append(structure.Overlap(structure.Connection(2, 51), structure.Connection(5, 12)))
    newScene.overlaps.append(structure.Overlap(structure.Connection(6, 12), structure.Connection(7, 16)))
    newScene.overlaps.append(structure.Overlap(structure.Connection(6, 27), structure.Connection(8, 25)))

    newScene.junctions.append(structure.Junction(structure.Connection(0, 35), structure.Connection(1, 0), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(0, 35), structure.Connection(0, 36), +1, 2))
    newScene.junctions.append(structure.Junction(structure.Connection(1, 15), structure.Connection(2, 0), +1, 2))
    newScene.junctions.append(structure.Junction(structure.Connection(1, 15), structure.Connection(1, 16), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(2, 14), structure.Connection(3, 28), -1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(2, 14), structure.Connection(2, 15), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(3, 28), structure.Connection(2, 14), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(3, 14), structure.Connection(0, 50), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(3, 14), structure.Connection(3, 13), -1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(0, 50), structure.Connection(3, 14), +1, 2))
    newScene.junctions.append(structure.Junction(structure.Connection(0, 50), structure.Connection(3, 12), -1, 4))
    newScene.junctions.append(structure.Junction(structure.Connection(0, 50), structure.Connection(0, 51), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(3, 0), structure.Connection(4, 0), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(2, 51), structure.Connection(5, 13), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(2, 51), structure.Connection(5, 11), -1, 2))
    newScene.junctions.append(structure.Junction(structure.Connection(2, 51), structure.Connection(2, 52), +1, 2))
    newScene.junctions.append(structure.Junction(structure.Connection(2, 63), structure.Connection(7, 28), -1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(4, 49), structure.Connection(7, 0), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(4, 49), structure.Connection(4, 50), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(4, 63), structure.Connection(8, 8), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(4, 63), structure.Connection(8, 8), -1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(5, 0), structure.Connection(6, 0), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(6, 12), structure.Connection(7, 15), -1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(6, 12), structure.Connection(6, 13), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(7, 16), structure.Connection(6, 13), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(7, 16), structure.Connection(7, 15), -1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(7, 0), structure.Connection(4, 49), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(8, 0), structure.Connection(9, 0), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(8, 40), structure.Connection(11, 0), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(8, 18), structure.Connection(10, 0), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(8, 18), structure.Connection(8, 19), +1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(8, 18), structure.Connection(8, 17), -1, 1))
    newScene.junctions.append(structure.Junction(structure.Connection(6, 27), structure.Connection(8, 26), +1, 2))
    newScene.junctions.append(structure.Junction(structure.Connection(6, 27), structure.Connection(8, 24), -1, 2))
    newScene.junctions.append(structure.Junction(structure.Connection(6, 27), structure.Connection(6, 28), +1, 1))

    return newScene
