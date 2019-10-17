import os, sys, argparse
import owl_lib

parser = argparse.ArgumentParser(description = 'Wacom area setting utility for osu!')
parser.add_argument("area", type = float, help = "how much of area to use in percent (0-100)")
parser.add_argument("offx", type = float, help = "how much offset in X axis in percent (0-100)")
parser.add_argument("offy", type = float, help = "how much offset in Y axis in percent (0-100)")
parser.add_argument("rotated", type = str, help = "tablet rotated (y/n)") 
args = parser.parse_args()

area_array = owl_lib.area()
res_array = owl_lib.res()

x_coor = area_array[2] * (args.area/100)
y_coor = x_coor * res_array[1] / res_array[0]
x_off  = (area_array[2] - x_coor) * (args.offx/100)
y_off  = (area_array[3] - y_coor) * (args.offy/100)

owl_lib.rotate(args.rotated)
owl_lib.no_smoothing()
owl_lib.set_area(0 + x_off, 0 + y_off, x_coor + x_off, y_coor + y_off) 
