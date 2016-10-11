#!/usr/bin/env python

import scene_default
import scene_explosion
import scene_replicate
import scene_generator
import opc

# Create OPC client
opc = opc.Client('127.0.0.1:7890')

# Create a default scene 
scene = scene_default.SceneDefault(opc)
scene.fps = 20
scene.pulse_interval = 5
scene.color = [87, 200, 255]
scene.tail_alpha = [0.6, 0.4, 0.2]
scene_generator.generate(scene)


# Create a replication scene
# scene = scene_replicate.SceneReplicate(opc)
# scene.fps = 20
# scene.pulse_interval = 80
# scene.color = [87, 200, 255]
# scene.tail_alpha = [0.6, 0.4, 0.2]
# scene_generator.generate(scene)

# Create a explosion scene
# scene = scene_explosion.SceneExplosion(opc)
# scene.fps = 20
# scene.pulse_interval = 5
# scene.color = [87, 200, 255]
# scene.tail_alpha = [0.6, 0.4, 0.2]
# scene_generator.generate(scene)

# Run
scene.start()
