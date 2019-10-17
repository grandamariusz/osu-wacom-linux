# osu-wacom-linux
Wacom area setting utility for osu!.

This little script calculates and sets tablet's area for Wacom tablets automatically, given four parameters.

It disables any smoothing by default.


Example use: `python owl.py 50 75 75 n`

Help: `python owl.py -h` or `python owl.py --help`

# requirements
Make sure to install `xf86-input-wacom` and `xorg-xrandr` before running the script

Arch Linux:
`sudo pacman -S xf86-input-wacom xorg-xrandr`

# parameters
- Area percentage: from 0 to 100 (accepts floats)
- Area's placement on the X axis: from 0 to 100 (accepts floats)
- Area's placement on the Y axis: from 0 to 100 (accepts floats)
- Left-handed mode (tablet rotated 180 degrees): y / n

# how to execute the script
Clone the script into your home directory:

`git clone https://github.com/smokepenguin/osu-wacom-linux`

Finally, run the script using: 

`cd ./osu-wacom-linux`

`python owl.py <parameters here>`

If you want to run it during your favourite windows manager's boot, check ArchWiki

Have fun!
