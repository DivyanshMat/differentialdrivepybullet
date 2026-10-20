#drop a cube to know if physics work
import time
import pybullet as p
import pybullet_data

# start simulator
p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# turn on gravity: 9.81 m/s2 pointing down the z axis 
p.setGravity(0, 0, -9.81)

# load the floor and a small cube 1 metre above it.
p.loadURDF("plane.urdf")
p.loadURDF("cube_small.urdf", [0, 0, 1])

# 5. Run the physics.
print("Simulation running. Close the window to quit.")
while p.isConnected():
    p.stepSimulation()
    time.sleep(1.0 / 240.0)
