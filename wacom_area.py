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
	area = " Area {} {} {} {}".format(int(a), int(b), int(c), int(d))
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

try:
	#user input
	percent  = float(input('Tablet area percent (0-100): '))
	flipped  = input("Area flipped? (y/n): ").lower().strip()
	offset_x = float(input('Offset in X axis percent (0-100): '))
	offset_y = float(input('Offset in Y axis percent (0-100): '))

except: 
	print('\n' + 'Check if you\'ve entered values correctly' + '\n')

finally:
	try:
		#creates lists with retrieved data
		area_arr = area()
		res_arr  = res()

		#calculations
		x_coor = area_arr[2] * (percent/100)
		y_coor = x_coor * res_arr[1] / res_arr[0]

	except:
		print('\n' + "An error ocurred. Check if your tablet is connected.")
		print("Otherwise, check if you have xorg-xrandr and xf86-input-wacom installed" + '\n')

	finally:
		#offset calculations
		x_off  = (area_arr[2] - x_coor) * (offset_x/100)
		y_off  = (area_arr[3] - y_coor) * (offset_y/100)

 		rotate(flipped)
		no_smoothing()
		set_area(0 + x_off, 0 + y_off, x_coor + x_off, y_coor + y_off)
