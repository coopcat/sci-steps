import os
import sympy as sp
from Problems import *
from pylatex.package import Package
from pylatex import Document, Section, Subsection, Command, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat # These might help with making visual diagrams in later versions. 
from pylatex.utils import NoEscape, italic

x = ProjectileMotion() # Change name of problem to specify which type of problem you'd like to solve in Problems.py. 
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

    solutions.generate_tex('Solved') # Generates .tex file, check in folder for the .tex dump.
    solutions.generate_pdf('Solved') # Generates .pdf file, check in folder for the .pdf dump.
    print("PDF sucessfully created! Opening now...")
    os.popen('./pdfopen.sh')     

else:
    print(x.get_answer()[:-1])
