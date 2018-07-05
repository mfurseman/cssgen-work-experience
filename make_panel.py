#!/usr/bin/env dls-python2.7

from pkg_resources import require #imports require function from pkg_resources library
require('cssgen==0.4dls1') #runs require function with argument
require('numpy')

from opimodel import widgets, colors, fonts, dls_utils, borders
from renderers.css import render
import numpy as np


BPM_OPI = 'test.opi' #sets the target file in folder
corrector_OPI = 'Corrector.opi'


colors.parse_css_color_file(dls_utils.find_color_file()) #parses pre-defined colours and fonts into program
fonts.parse_css_font_file(dls_utils.find_font_file())


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


def headerBox(xsize, ysize, title, display):
    pinkBanner = widgets.Rectangle(0, 0, xsize, ysize)
    pinkBanner.set_bg_color(colors.DI_TITLE)
    display.add_child(pinkBanner)

    label = widgets.Label(0, 0, xsize, ysize, title) #creates label object - sets size and position
    label.set_font(fonts.HEADER_2)                                     #sets font to Fine Print - Liberation Sans-regular-12px
    display.add_child(label)


def green_rectangle(xpos, ypos, xsize, ysize, display):                              #function creates the bunch of 4 small green rectangles
    border_width = 1

    rectangleSH = widgets.Rectangle(xpos, ypos, xsize/2, ysize/2)      #rectangle for each of SH, SV, FH AND FV  (slow/fast, horizontal/vertical)
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
            if cell_array[x,y] == 1:
                rec_function(xcoords[x,y], ycoords[x,y], rec_width, rec_height)


def bpm_positions():
    rows = 14
    columns = 24

    full_row = []
    for i in range(columns):
        full_row.append(1)

    s_one_two = []
    for i in range(columns):
        s_one_two.append(0)
    s_one_two[8] = 1
    s_one_two[12] = 1

    eight = []
    for i in range(columns):
        eight.append(0)
    eight[1] = 1

    cell_array = np.array([s_one_two, s_one_two, full_row, full_row, full_row, full_row, full_row, full_row, full_row, eight])

    return cell_array

def corrector_positions():
    rows = 10
    columns = 24

    full_row = []
    for i in range(columns):
        full_row.append(1)

    s_one_two = []
    for i in range(columns):
        s_one_two.append(0)
    s_one_two[8] = 1
    s_one_two[12] = 1

    two_three_six = []
    for i in range(columns):
        two_three_six.append(1)
    two_three_six[1] = 0

    five = []
    for i in range(columns):
        five.append(1)
    five[10] = 0

    c_one_two_eight_ten = []
    for i in range(columns):
        c_one_two_eight_ten.append(0)
    c_one_two_eight_ten[1] = 1

    cell_array = np.array([s_one_two, s_one_two, full_row, two_three_six, two_three_six, full_row, five, c_one_two_eight_ten, c_one_two_eight_ten, two_three_six, full_row, c_one_two_eight_ten, c_one_two_eight_ten])

    return cell_array


def main():
    display = widgets.Display(604, 367)
    cell_array = corrector_positions()
    headerBox(604, 50, "SOFB and FOFB BPM Masks", display)
    def display_func(xpos, ypos, xsize, ysize):
        green_rectangle(xpos, ypos, xsize, ysize, display)
    gen_grid(cell_array, 30, 80, 15, 20, 4, display_func)

    list_of_side = ["S1", "S2", "01", "02", "03", "04", "05", "C1", "C2", "06", "07", "08", "10"]
    list_of_top = ['%02d' % xx for xx in range(1, 25)]
    for i in range(24): #creates list of labels for top cells
        i += 1
        list_of_top.append(i)
    initialiseCells(2, 2, 18, 22, 5, list_of_side, list_of_top, display) #calls function with arguments

    # Write out the display
    render.get_opi_renderer(display).write_to_file(corrector_OPI)


if __name__ == "__main__":
    main()
