import os
import sympy as sp
import math
from problems import *
from pylatex.package import Package
from pylatex import Document, Section, Subsection, Command, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat 
from pylatex.utils import NoEscape, italic

unknown_vars = ['t_i', 'v_x', 'v_y', 'v_X', 'v_Y', 'd_x']
units = {'d_y':'m', 'g_e':'m/s**2', 'h_y':'m', 't_i':'s', 'd_x':'m', 'v_T':'m/s', 'v_x':'m/s', 'v_y':'m/s', 'v_X':'m/s', 'v_Y':'m/s', 'a_v':'degrees'}
names = {'g_e':'gravity of earth', 'h_y': 'height', 't_i': 'time', 'd_x': 'horizontal displacement', 'v_T': 'total initial velocity', 'v_x': 'initial horizontal velocity', 'v_y': 'initial vertical velocity', 'v_X': 'horizontal velocity on impact', 'v_Y': 'vertical velocity on impact', 'a_v': 'angle of initial velocity'}
equations = ['v_x*t_i-d_x', 'v_x-v_X', '1/2*g_e*t_i**2+v_y*t_i+h_y', 'v_y+g_e*t_i-v_Y', '-cos(a_v)+v_x/v_T', '-sin(a_v)+v_y/v_T', 'v_total**2-v_x**2+v_y**2', '-tan(a_v)+(v_y/v_x)']
known_vars = ['g_e', 'v_T', 'h_y', 'a_v']
vars_order = [-9.8, 100, 20, math.radians(82)]
x = ProjectileMotion(equations, known_vars, vars_order, units, names, unknown_vars)
x.solve_it()
z = x.get_answer()
question_type = x.get_question_type()

def part_splitter(unparsed_text):
    '''Creates a list of indices of the unparsed text where the '@' sign shows up.'''
    master_list = []
    for i in range(len(unparsed_text)):
        if unparsed_text[i] == "@":
            master_list.append(i)
    return master_list

if x.get_solution_style() == True:
    parts = part_splitter(z)
    solutions = Document()
    solutions.preamble.append(Command('usepackage', 'amsmath'))
    solutions.preamble.append(Command('title', question_type))
    solutions.preamble.append(Command('author', 'Generated Solutions'))
    solutions.preamble.append(Command('date', NoEscape(r'\today')))
    # solutions.append(NoEscape(r'\maketitle')) Use if a title is desired.

    with solutions.create(Section('Solutions Generated for ' + question_type, numbering=False)):
        for i in range(len(parts)-1):
            x = z[parts[i]+1:parts[i+1]]
            solutions.append(NoEscape(x))

    solutions.generate_tex('Solved-TeX') # Generates .tex file
    solutions.generate_pdf('Solved') # Generates .pdf file
    print("PDF sucessfully created! Opening now...")
    os.popen('./pdfopen.sh')     

else:
    print(x.get_answer()[:-1])
