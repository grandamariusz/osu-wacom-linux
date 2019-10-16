# osu-linux-wacom
This is my first repository. 

This little script calculates and sets tablet's area for Wacom tablets automatically, given four parameters.
It disables any smoothing by default.

# requirements
Make sure to install `xf86-input-wacom` and `xorg-xrandr` before running the script

# parameters
- Area percentage: from 0 to 100 (accepts floats)
- Left-handed mode (tablet rotated 180 degrees): y / n
- Area's placement on the X axis: from 0 to 100 (accepts floats)
- Area's placement on the Y axis: from 0 to 100 (accepts floats)

# how to execute the script
Run the script using: 
`python wacom.py`
