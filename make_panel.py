#!/usr/bin/env dls-python2.7

from pkg_resources import require     #imports the required functions from package resources
require('cssgen==0.4dls1')            #runs the require function 

from opimodel import widgets, colors, fonts, dls_utils #imports modules to edit the GUI
from renderers.css import render          #imports modules to allow the GUI to be viewed


FILENAME = 'test.opi'              #sets the target file in the folder

colors.parse_css_color_file(dls_utils.find_color_file())  #reads the color configuration files


display = widgets.Display(588, 180)               #creates the root widget and sets display size
rectangle = widgets.Rectangle(0, 0, 50, 50)       #adds a rectangle
display.add_child(rectangle)                      #adds a rectangle

# Write out the display
render.get_opi_renderer(display).write_to_file(FILENAME)
