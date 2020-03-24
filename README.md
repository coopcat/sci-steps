# sci-steps
a prototype for generating solutions to high school science problems.

Requirements:

Python 3.0+, Sympy, PyLaTeX, and a LaTeX compiler.

Run parser.py to generate solutions. Solutions will be saved as a LaTeX .pdf. You'll need to edit the 'pdfopen.sh' shell script to open the .pdf file with your .pdf viewer.

To edit/create new problems, use the ProjectileMotion(Problem) class in problems.py and alter it to your liking.
