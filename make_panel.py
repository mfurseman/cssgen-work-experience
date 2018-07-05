#!/usr/bin/env dls-python2.7

from pkg_resources import require #imports require function from pkg_resources library
require('cssgen==0.4dls1') #runs require function with argument

from opimodel import widgets, colors, fonts, dls_utils, borders #imports functions from opimodel library
from renderers.css import render #imports render function from renderer.css library

FILENAME = 'test.opi' #sets the target file in folder

colors.parse_css_color_file(dls_utils.find_color_file()) #parses pre-defined colours and fonts into program
fonts.parse_css_font_file(dls_utils.find_font_file())

display = widgets.Display(604, 367) #sets display widget and its dimensions


def initialiseCells(x, y, cell_width, cell_height, cell_gap, side_name_list, top_name_list, display):

	num_of_side_cells = len(side_name_list)
	num_of_top_cells = len(top_name_list)
	y_pos_list = []
	x_pos_list = []
	
	####SIDE CELLS####
	
	for i in range(num_of_side_cells):
		y_pos_list.append(y*2 + cell_height + (i * cell_height) + (i * cell_gap))
		#sets y positions for cells and adds to list

	for ypos, name in zip(y_pos_list, side_name_list): 
	#runs for each element in both lists, assigns temp variables to both
	
		cell_label = widgets.Label(x, ypos, cell_width, cell_height, name) #creates label
		cell_label.set_font(fonts.FINE_PRINT)
		cell_label.set_bg_color(colors.GREY_50_)
		cell_label.transparent = False #disables transparency, allows for background
		#cell_label.set_border(borders.Border(borders.LINE_STYLE, 1, colors.BLACK, False))
		display.add_child(cell_label) #adds cell to display
	
	####TOP CELLS####
	
	for i in range(num_of_top_cells):
	
		x_pos_list.append(x*2 + cell_width + (i * cell_width) + i *cell_gap)

	for xpos, name in zip(x_pos_list, top_name_list):
	
		cell_label = widgets.Label(xpos, y, cell_width, cell_height, name)
		cell_label.set_font(fonts.FINE_PRINT)
		cell_label.set_bg_color(colors.GREY_50_)
		cell_label.transparent = False
		#cell_label.set_border(borders.Border(borders.LINE_STYLE, 1, colors.BLACK, False))
		display.add_child(cell_label)
		
		
list_of_side = ["S1", "S2", "01", "02", "03", "04", "05", "C1", "C2", "06", "07", "08", "10"]
list_of_top = []

for i in range(24): #creates list of labels for top cells
	i += 1
	list_of_top.append(i)

initialiseCells(2, 2, 18, 22, 5, list_of_side, list_of_top, display) #calls function with arguments

display.set_bg_color(colors.CANVAS) #sets background color

# Write out the display
render.get_opi_renderer(display).write_to_file(FILENAME)

