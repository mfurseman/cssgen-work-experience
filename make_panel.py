#!/usr/bin/env dls-python2.7

from pkg_resources import require
require('cssgen==0.4dls1')

from opimodel import widgets, colors, fonts, dls_utils
from renderers.css import render


FILENAME = 'test.opi'

colors.parse_css_color_file(dls_utils.find_color_file())


display = widgets.Display(588, 180)
rectangle = widgets.Rectangle(0, 0, 50, 50)
display.add_child(rectangle)

# Write out the display
render.get_opi_renderer(display).write_to_file(FILENAME)
