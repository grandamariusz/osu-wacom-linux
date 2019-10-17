import os, sys
import wacom

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
		area_arr = wacom.area()
		res_arr  = wacom.res()

		#calculations
		x_coor = area_arr[2] * (percent/100)
		y_coor = x_coor * res_arr[1] / res_arr[0]

	except:
		print('\n' + "An error ocurred. Check if your tablet is connected.")
		print("Otherwise, check if you have xrandr and xf86-input-wacom installed" + '\n')

	finally:
		#offset calculations
		x_off  = (area_arr[2] - x_coor) * (offset_x/100)
		y_off  = (area_arr[3] - y_coor) * (offset_y/100)

		wacom.no_smoothing()
		wacom.rotate(flipped)
		wacom.set_area(0 + x_off, 0 + y_off, x_coor + x_off, y_coor + y_off)
