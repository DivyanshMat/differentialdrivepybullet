# Differential Drive Husky Robot Moving In Space

A small warm-up project: load a standard wheeled robot (the Clearpath Husky) into the PyBullet physics simulator and make it move in a way you can see.

# What it does

The script `driveV2.py` opens a PyBullet window, drops a Husky robot onto a floor, and drives it through four phases:

1. Drive straight (both wheel pairs at the same speed)
2. Curve to the left (right wheels faster than left)
3. Spin on the spot (left and right wheels in opposite directions)
4. Stop

After each phase it prints the robot's position and heading, so the movement is also visible in numbers, not just on screen.

# How it works

- The robot comes from a URDF file (a text description of the robot's links and joints) that ships with PyBullet.
- The script finds the four wheel joints by name and splits them into a left pair and a right pair.
- Each phase sets a target wheel speed (rad/s) with velocity control, then advances the physics in 1/240 s steps.
- This is differential drive: steering comes only from the difference between left and right wheel speeds.

# Requirements

- PyBullet

Tested on macOS 

# Run it

Leave the window open until the terminal prints `Done` (about 15 seconds), then close the window to quit.

# Files

 File | Purpose 

 driveV2.py Main script: loads the Husky and drives it 
 emptyworld.py First test: an empty world, to check the simulator works.

# Notes

- The long `No inertial data for link, using mass=1` messages in the terminal are harmless. Some small Husky parts list no mass in the URDF, so PyBullet assumes 1 kg.
- I first tried Gazebo, but the install did not complete on my Mac, so I switched to PyBullet. The core ideas are the same.
- I was going to use a robotic arm as an object, but I changed that idea into a differential drive robot.
- An earlier version of the script moved the camera on almost every step, which was slow on macOS and the window could disconnect. The final version uses one fixed camera and exits cleanly if the window is closed.

# AI assistance

This project was written with help from Claude.

## Author

Divyansh Mathur
