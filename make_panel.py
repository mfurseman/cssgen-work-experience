#!/usr/bin/env dls-python2.7

from pkg_resources import require #imports require function from pkg_resources library
require('cssgen==0.4dls1') #runs require function with argument

from opimodel import widgets, colors, fonts, dls_utils, borders #imports functions from opimodel library
from renderers.css import render #imports render function from renderer.css library

numOfCells = 24

FILENAME = 'test.opi' #sets the target file in folder

colors.parse_css_color_file(dls_utils.find_color_file())
fonts.parse_css_font_file(dls_utils.find_font_file())

display = widgets.Display(604, 367) #sets display size
#rectangle = widgets.Rectangle(0, 0, 50, 50) #makes rectangle variable 50x50px
#display.add_child(rectangle) #uses add_child method to add rectangle to canvas

def initialiseTopCells(canvasWidth, xCanvasMargin, yCanvasMargin, cellSize, numOfCells):
	xpos = xCanvasMargin
	ypos = yCanvasMargin
	count = 0

	for cell in range(numOfCells):
		count += 1
		cell = str(cell+1)
		xpos += (canvasWidth/numOfCells) - ((xCanvasMargin*2)/numOfCells)
		cellLabel = widgets.Label(xpos, ypos, cellSize, cellSize, cell)
		cellLabel.set_font(fonts.FINE_PRINT)
		cellLabel.set_bg_color(colors.GREY_90_)
		cellLabel.set_transparency(False)
		cellLabel.set_border(borders.Border(borders.LINE_STYLE, 1, colors.BLACK, False))
		display.add_child(cellLabel)
	

initialiseTopCells(604, 13, 2, 20, 24)

display.set_bg_color(colors.WHITE)

# Write out the display
render.get_opi_renderer(display).write_to_file(FILENAME)
