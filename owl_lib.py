import os

#this function extracts tablet's name
def name():
		name = os.popen("xsetwacom --list devices | grep 'stylus'").read()
		return  '\"' + "".join(name.partition('stylus')[0:2]) + '\"'

#this function resets tablet's area and returns full area coordinates
def area():
	os.popen("xsetwacom --set " + name() + " ResetArea")
	area = os.popen("xsetwacom --get " + name() + " Area").read().split()
	return list(map(int, area))

#this funtion gets user's monitor's resolution
def res():
	res = os.popen("(xrandr | grep '*') | awk '{print $1}'").read().split()[0].split('x')
	return list(map(int, res))

#this function sets tablet's area given four parameters
def set_area(a, b, c, d):
	area = " Area {} {} {} {}".format(round(a), round(b), round(c), round(d))
	return os.popen("xsetwacom set " + name() + area)

#this function rotates the tablet area
def rotate(flipped):
	if 'y' in flipped:
		return os.popen("xsetwacom set " + name() + ' Rotate \"half\"')
	elif 'n' in flipped:
		return os.popen("xsetwacom set " + name() + ' Rotate \"none\"')

#this function disables smoothing
def no_smoothing():
	os.popen("xsetwacom set " + name() + " RawSample \"1\"")
	os.popen("xsetwacom set " + name() + " Suppress \"0\"")

