import sympy as sp
from sympy.parsing.sympy_parser import *
import math
import vectors

class Problem(object):
    '''Problem class that consists of steps for solving equations and vectors.'''

    def __init__(self, equations, known_vars, vars_order):
        self.equations = equations
        self.known_vars = known_vars
        self.vars_order = vars_order

    def equations_rearrange(self, j, solve_for):
        '''Rearranges an equation with variables only. Returns the equation value.'''
        self.equations[j] = str((sp.solve(sp.sympify(self.equations[j]), sp.sympify(solve_for))))
        return (sp.sympify(self.equations[j]))

    def equations_fill(self, j):
        '''Fills a rearranged equation's known variables with their corresponding numerical value. Returns the string value and equation value.'''
        for i in range(len(self.known_vars)):
            if self.known_vars[i] in self.equations[j]:
                self.equations[j] = self.equations[j].replace(self.known_vars[i], str(self.vars_order[i]))
        return (self.equations[j], (sp.parsing.sympy_parser.parse_expr((self.equations[j]), evaluate=False)))

    def equations_simplify(self, j):
        '''Simplifies and evaluates an equation. Returns the equation value.'''
        self.equations[j] = str(sp.simplify(sp.sympify(self.equations[j])))
        return (sp.sympify(self.equations[j]))

    # Equations are not overwritten using the methods below. 

    def seperate_equation_rearrange(self, equation, solve_for):
        '''Solves for one variable of an equation and returns the sympified version of it.'''
        return (sp.sympify(str((sp.solve(sp.sympify(equation), sp.sympify(solve_for))))),
                sp.parsing.sympy_parser.parse_expr(equation, evaluate=False))

    def seperate_equation_fill(self, equation):
        '''Fills in a single equation with known variables and returns the sympified version of it.'''
        for i in range(len(self.known_vars)):
            if self.known_vars[i] in equation:
                equation = equation.replace(self.known_vars[i], str(self.vars_order[i]))
        return sp.parsing.sympy_parser.parse_expr(equation, evaluate=False)

    def seperate_equation_fill_display(self, equation, vars_order_display):
        '''Fills in a single equation with known variables and returns the sympified version of it.'''
        for i in range(len(self.known_vars)):
            if self.known_vars[i] in equation:
                equation = equation.replace(self.known_vars[i], str(vars_order_display[i]))
        return sp.parsing.sympy_parser.parse_expr(equation, evaluate=False)

    def seperate_equation_simplify(self, equation):
        '''Evaluates a single equation and returns the simplified & sympified version of it.'''
        equation = str(sp.simplify(sp.sympify(equation)))
        if ',' in equation:
           try:
               equation = eval(equation)
               for i in range(len(equation)):
                   if equation[i] >= 0:
                       equation = equation[i]
                       break
           except:
               equation = "impossible"
        return sp.sympify(equation)

    def seperate_equation_evaluate(self, equation):
        '''Evaluates a single equation and returns the evaluated (approximate) & sympified version of it.'''
        equation = str(sp.simplify(sp.sympify(equation)))
        if ',' in equation:
           try:
               equation = eval(equation)
               for i in range(len(equation)):
                   if equation[i] >= 0:
                       equation = equation[i]
                       break
           except:
               equation = "impossible"
        return sp.sympify(equation).evalf()

    def add_known_var(self, new_var, new_value):
        self.known_vars.append(new_var)
        self.vars_order.append(new_value)

    def get_known_vars(self):
        return self.known_vars

    def get_equations(self):
        return self.equations

    def get_vars_order(self):
        return self.vars_order


def check_if_unique(equation, variables):
    '''Global function that checks if an equation only consists of one variable. Returns true if it is unique, else returns false.'''
    counter = 0
    for i in range(len(variables)):
        if variables[i] in equation:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

class ProjectileMotion:
    '''Projectile motion problem.'''

    def __init__(self):
        self.show_full = True # Set to True to show full solutions
        self.units = {'d_y':'m', 'g_e':'m/s**2', 'h_y':'m', 't_i':'s', 'd_x':'m', 'v_T':'m/s', 'v_x':'m/s', 'v_y':'m/s', 'v_X':'m/s', 'v_Y':'m/s', 'a_v':'degrees'}
        self.names = {'g_e':'gravity of earth', 'h_y': 'height', 't_i': 'time', 'd_x': 'horizontal displacement', 'v_T': 'total initial velocity', 'v_x': 'initial horizontal velocity',
                      'v_y': 'initial vertical velocity', 'v_X': 'horizontal velocity on impact', 'v_Y': 'vertical velocity on impact', 'a_v': 'angle of initial velocity'}
        self.equations = ['v_x*t_i-d_x', 'v_x-v_X', '1/2*g_e*t_i**2+v_y*t_i+h_y',
                          'v_y+g_e*t_i-v_Y', '-cos(a_v)+v_x/v_T', '-sin(a_v)+v_y/v_T', 'v_total**2-v_x**2+v_y**2', '-tan(a_v)+(v_y/v_x)']
        self.display_equations = ['v_x*t_i-d_x', 'v_x-v_X', '1/2*g_e*t_i**2+v_y*t_i+h_y',
                          'v_y+g_e*t_i-v_Y', '-cos(a_v)+v_x/v_T', '-sin(a_v)+v_y/v_T', 'v_total**2-v_x**2+v_y**2', '-tan(a_v)+(v_y/v_x)']
        'Integration selfs'
        self.known_vars = ['g_e', 'h_y', 't_i', 'd_x']
        self.vars_order = [-9.8, 20, 3, 9] # Each value corresponds to the variable with the same index position in self.known_vars. 
        self.vars_order_display = [-9.8, 20, 3, 9]
        self.unknown_vars = ['v_T', 'v_x', 'v_y', 'v_X', 'v_Y', 'a_v'] # Order doesn't matter 
        self.answer = ''
        self.model = Problem(self.equations, self.known_vars, self.vars_order)
        self.answer = ''

        # If magnitude of velocity is not known, it will attempt to find the magnitude and direction of velocity. 
        if 'v_T' not in self.known_vars:
            self.solve_for_velocity = True
        else:
            self.solve_for_velocity = False

        for i in range(len(self.model.get_equations())):
            self.model.equations_fill(i)

    def solve_it(self):
        self.not_yet_solved = []
        for i in range(len(self.unknown_vars)):
            solve_attempt = False
            for j in range(len(self.model.get_equations())):
                if solve_attempt is True:
                    continue
                if self.unknown_vars[i] in self.model.get_equations()[j]:
                    solved = \
                    self.model.seperate_equation_rearrange(self.model.get_equations()[j], self.unknown_vars[i])[0]
                    solved_factor_sols = solved
                    solved = str(solved)
                    if ', ' in solved:
                        try:
                            solved = eval(solved)
                            for t in range(len(solved)):
                                if solved[t] >= 0:
                                    solved = str(solved[t])
                        except:
                            continue
                    if '[' and ']' in solved:
                        solved = str(solved[1:-1])
                    if check_if_unique(solved, self.unknown_vars) == True:
                        if self.show_full == True:
                            self.answer += str(r"@Solving for " + self.names[self.unknown_vars[i]] + r":") + ('@')
                            self.answer += (r"\newline@\newline@Using the equation,@" + r'\begin{equation*}' + sp.latex(
                                sp.sympify(self.display_equations[j]),
                                mode='plain') + " = 0" + r'\end{equation*}' + "@Rearrange for $" +
                                            self.unknown_vars[i] + "$:@")
                            filler = str(
                                self.model.seperate_equation_rearrange(self.display_equations[j], self.unknown_vars[i])[
                                    0])[1:-1]

                            if ',' in filler: # Used to check which solution of the quadratic is positive
                                if solved_factor_sols[0] >= 0:
                                    filler = filler[:filler.find(',')] + ')'
                                else:
                                    filler = filler[filler.find(',')+2:]

                            self.answer += str(r'\begin{equation*}' + self.unknown_vars[i] + " = " + sp.latex(sp.sympify(filler), mode='plain') + r'\end{equation*}') + ('@')

                            solved_fill = self.model.seperate_equation_fill(filler)
                            # solved_fill = str(solved_fill)
                            solved_simplified = self.model.seperate_equation_simplify(solved_fill)
                            solved_evaluated = self.model.seperate_equation_evaluate(solved_fill)

                            solved_fill_display = sp.latex(
                                self.model.seperate_equation_fill_display(filler, self.vars_order_display),
                                mode='plain')

                            if 'a_v' in filler:
                                self.answer += r'\begin{equation*}' + " = " + solved_fill_display
                            else:
                                self.answer += r'\begin{equation*}' + " = " + sp.latex(solved_fill, mode='plain')

                            solved_fill = self.model.seperate_equation_fill(filler)
                            # solved_fill = str(solved_fill)
                            solved_simplified = self.model.seperate_equation_simplify(solved_fill)
                            solved_evaluated = self.model.seperate_equation_evaluate(solved_fill)

                            if 'a_v' == self.unknown_vars[i]:
                                solved_simplified, solved_evaluated = math.degrees(solved_evaluated), math.degrees(solved_evaluated)
                            if str(solved_fill) != str(solved_simplified):
                                try:
                                    self.answer += str(r'\end{equation*}' + r'@\begin{equation*}' + " = " + sp.latex(round(solved_simplified,2), mode='plain') + '\;' + self.units[self.unknown_vars[i]] + r'\end{equation*}') + ('@')
                                except:
                                    self.answer += str(r'\end{equation*}' +
                                        r'@\begin{equation*}' + " = " + sp.latex(solved_simplified,
                                                                                mode='plain') + r'\end{equation*}') + (
                                                       '@')
                            else:
                                self.answer += '\;' + self.units[self.unknown_vars[i]] + r'\end{equation*}' + '@'

                            if str(solved_simplified)[str(solved_simplified).find('.'):str(solved_simplified).find('.')+3] != str(solved_evaluated)[str(solved_evaluated).find('.'):str(solved_evaluated).find('.')+3]: # Due to floating points being inaccurate, it checks only if the first 2 decimal places are equal.
                                try:
                                    self.answer += str(r'\begin{equation*}' + r"\;or\;" + sp.latex(round(solved_evaluated,2), mode='plain') + '\;' + self.units[self.unknown_vars[i]] + r'\end{equation*}') + ('@') # Shows approximate solution
                                except:
                                    self.answer += str(
                                        r'\begin{equation*}' + r"\;or\;" + sp.latex(round(solved_evaluated, 2),
                                                                                    mode='plain') + r'\end{equation*}') + (
                                                       '@')

                            # Called again to reset the values to radians.
                            if 'a_v' == self.unknown_vars[i]:
                                solved_fill = self.model.seperate_equation_fill(filler)
                                solved_fill = str(solved_fill)
                                solved_simplified = self.model.seperate_equation_simplify(solved_fill)
                                solved_evaluated = self.model.seperate_equation_evaluate(solved_fill)
                        else:
                            solved_fill = self.model.seperate_equation_fill(solved)
                            solved_fill = str(solved_fill)
                            solved_simplified = self.model.seperate_equation_simplify(solved_fill)
                            solved_simplified = str(solved_simplified)
                            self.answer += self.unknown_vars[i] + " = " + solved_simplified + "\n"

                        try:
                            self.model.add_known_var(self.unknown_vars[i], str(round(solved_evaluated, 2)))
                            self.vars_order_display.append(round(solved_evaluated, 2))
                        except:
                            self.model.add_known_var(self.unknown_vars[i], str(solved_evaluated))
                            self.vars_order_display.append(solved_evaluated)

                        for t in range(len(self.model.get_equations())):
                            self.model.equations_fill(t)
                            solved, solved_fill, solved_simplified = "", "", ""
                            solve_attempt = True
                        else:
                            solved, solved_fill, solved_simplified = "", "", ""
                else:
                    solved, solved_fill, solved_simplified = "", "", ""
            if solve_attempt == False:
                self.not_yet_solved.append(self.unknown_vars[i])
            if self.unknown_vars[i] == self.unknown_vars[-1]:
                self.unknown_vars = self.not_yet_solved
                self.solve_it()
            if self.solve_for_velocity == True and 'v_T' in self.known_vars and 'a_v' in self.known_vars: # Solves the velocity vector when the magnitude and angle are found. 
                self.solved_velocity = (vectors.Vectors.get_vector(
                    [self.model.get_vars_order()[self.model.get_known_vars().index('v_x')],
                     self.model.get_vars_order()[self.model.get_known_vars().index('v_y')]]))
                self.velocity_magnitude = self.solved_velocity[0]
                self.velocity_angle = self.model.get_vars_order()[self.model.get_known_vars().index('a_v')]
                if self.show_full == True:
                    self.answer += "Therefore, the magnitude and direction of initial velocity is:@"
                    self.answer += r'\begin{equation*}' + str(round(self.velocity_magnitude,2)) + r"\;m/s\;" + str(vectors.Vectors.get_directions([[self.velocity_magnitude, self.velocity_angle]])[0][1]).replace(' ', r'\;') + r'\end{equation*}@'
                else:
                    self.answer += "initial velocity = " + str(round(self.velocity_magnitude,2)) + " m/s " + str(vectors.Vectors.get_directions([[self.velocity_magnitude, self.velocity_angle]])[0][1]) + "\n"
                self.solve_for_velocity = False

    def __str__(self):
        return self.answer

    def get_solution_style(self):
        return self.show_full

    def get_answer(self):
        return self.answer

    def get_question_type(self):
        return "Projectile Motion"
