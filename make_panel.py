#!/usr/bin/env dls-python2.7

from pkg_resources import require     #imports the required functions from package resources
require('cssgen==0.4dls1')            #runs the require function 
require('numpy')

import numpy as np
from opimodel import widgets, colors, borders, fonts, dls_utils #imports modules to edit the GUI
from renderers.css import render          #imports modules to allow the GUI to be viewed
import os                                 #imports os


FILENAME = 'test.opi'              #sets the target file in the folder

colors.parse_css_color_file(dls_utils.find_color_file())  #reads the color configuration files
fonts.parse_css_font_file(dls_utils.find_font_file())     #reads the font config file


def headerBox(xsize, ysize, title, display):
	pinkBanner = widgets.Rectangle(0, 0, xsize, ysize)
	pinkBanner.set_bg_color(colors.DI_TITLE)
	display.add_child(pinkBanner)

	label = widgets.Label(0, 0, xsize, ysize, title) #creates label object - sets size and position
	label.set_font(fonts.HEADER_2)                                     #sets font to Fine Print - Liberation Sans-regular-12px
	display.add_child(label)                                           


def green_rectangle(xpos, ypos, xsize, ysize, display):                              #function creates the bunch of 4 small green rectangles
	border_width = 1
	
	rectangleSH = widgets.Rectangle(xpos, ypos, xsize/2, ysize/2)      #rectangle for each of SH, SV, FH AND FV
	rectangleSV = widgets.Rectangle(xpos + (xsize/2) - (border_width), ypos, xsize/2, ysize/2)
	rectangleFH = widgets.Rectangle(xpos, ypos+ysize/2 - (border_width), xsize/2, ysize/2)
	rectangleFV = widgets.Rectangle(xpos+xsize/2 - (border_width), ypos+ysize/2 - (border_width), xsize/2, ysize/2)

	rec_list = [rectangleSH, rectangleSV, rectangleFH, rectangleFV]

	for rectangle in rec_list:
		rectangle.set_bg_color(colors.GREEN)                       
		rectangle.set_border(borders.Border(borders.LINE_STYLE, border_width, colors.BLACK, False))    #sets black borders 
		display.add_child(rectangle)  


def gen_grid(cell_array, xpos, ypos, rec_width, rec_height, padding, rec_function):
	rows, columns = cell_array.shape
	row_array = np.arange(ypos, (rec_height+padding)*rows + ypos, rec_height+padding)
	column_array = np.arange(xpos, (rec_width+padding)*columns + xpos, rec_width+padding)	
	xcoords, ycoords = np.meshgrid(column_array, row_array)                #creates two 2D arrays of x coordinates and y coordinates

	for x in range(rows):
		for y in range(columns):
			if cell_array[x,y] == True:
				rec_function(xcoords[x,y], ycoords[x,y], rec_width, rec_height)


def main():		
	display = widgets.Display(604, 367)  
	cell_array = np.ones((14, 24), dtype=bool)
	headerBox(604, 50, "SOFB and FOFB BPM Mask", display)

	def display_func(xpos, ypos, xsize, ysize):
		green_rectangle(xpos, ypos, xsize, ysize, display)

	gen_grid(cell_array, 30, 80, 15, 20, 4, display_func)

	render.get_opi_renderer(display).write_to_file(FILENAME)


if __name__ == "__main__":
	main()




