#Load a Husky wheeled robot in PyBullet and drive it: straight, curve, spin.
#v2: fixed camera (no per-step camera calls, which are slow on macOS) 

import math
import time
import pybullet as p
import pybullet_data

# world setup
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.loadURDF("plane.urdf")

# robot loads as it is 0.2 meters above the ground
husky = p.loadURDF("husky/husky.urdf", [0, 0, 0.2])

# divide the joints into two, left and right
left_wheels = []
right_wheels = []
print("\nJoints in the Husky:")
for j in range(p.getNumJoints(husky)):
    name = p.getJointInfo(husky, j)[1].decode()
    print(f"  joint {j}: {name}")
    if "wheel" in name and "left" in name:
        left_wheels.append(j)
    elif "wheel" in name and "right" in name:
        right_wheels.append(j)

print("\nLeft wheel joints :", left_wheels)
print("Right wheel joints:", right_wheels)
if not left_wheels or not right_wheels:
    raise SystemExit("Could not find wheel joints - check the joint list above.")

# a "camera" that allows to view the whole area
p.resetDebugVisualizerCamera(cameraDistance=12, cameraYaw=0,
                             cameraPitch=-60, cameraTargetPosition=[3, 0, 0])


def drive(left_speed, right_speed, seconds, label):
    """Set wheel speeds (rad/s) and run the physics for `seconds`."""
    print(f"\n{label}: left={left_speed}, right={right_speed}, {seconds}s", flush=True)
    for j in left_wheels:
        p.setJointMotorControl2(husky, j, p.VELOCITY_CONTROL,
                                targetVelocity=left_speed, force=1000)
    for j in right_wheels:
        p.setJointMotorControl2(husky, j, p.VELOCITY_CONTROL,
                                targetVelocity=right_speed, force=1000)

    for _ in range(int(seconds * 240)):
        if not p.isConnected():
            raise SystemExit("\nThe simulator window was closed - stopping.")
        p.stepSimulation()
        time.sleep(1.0 / 240.0)

    pos, orn = p.getBasePositionAndOrientation(husky)
    heading = math.degrees(p.getEulerFromQuaternion(orn)[2])
    print(f"   -> position x={pos[0]:.2f} m, y={pos[1]:.2f} m, heading={heading:.0f} deg",
          flush=True)


# it has a given path so that path and its sequence
print("\nDon't close the window until Terminal prints 'Done'. Takes ~15 seconds.")
drive(0, 0, 1.5, "Settle onto the floor")
drive(10, 10, 4, "1) Drive straight")
drive(6, 10, 5, "2) Curve to the left")
drive(-8, 8, 3, "3) Spin on the spot")
drive(0, 0, 1, "4) Stop")

print("\nDone. Close the window to quit.")
while p.isConnected():
    p.stepSimulation()
    time.sleep(1.0 / 240.0)