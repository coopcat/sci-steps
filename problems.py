import math
import sympy as sp
from sympy.parsing.sympy_parser import *
from vectors import Vectors

class Problem(object):
    '''Problems consist of steps for solving equations.'''

    def __init__(self, equations, known_vars, vars_order):
        self.equations = equations
        self.known_vars = known_vars
        self.vars_order = vars_order

    def equations_rearrange(self, j, solve_for):
        '''Rearranges an equation with variables only. Returns rearranged equation.'''

        self.equations[j] = str(sp.solve(sp.sympify(self.equations[j]), sp,sympify(solve_for)))
        return sp.sympify(self.equations[j])

    def equations_fill(self, j):
        '''Replaces an equation's known variables with their numerical counterparts. Returns string and Sympy parsed version of equation.'''
        for i in range(len(self.known_vars)):  
            if self.known_vars[i] in self.equations[j]:
                self.equations[j] = self.equations[j].replace(self.known_vars[i], str(self.vars_order[i]))
        return (self.equations[j], sp.parsing.sympy_parser.parse_expr((self.equations[j]), evaluate=False))

    def equations_simplify(self, j):
        '''Simplies and evaluates an equation. Returns the sympified equation.'''

        self.equations[j] = str(sp.simplify(sp.sympify(self.equations[j])))
        return (sp.sympify(self.equations[j]))

    # Equations are not overwritten in the object by using the methods below.

    def separate_equation_rearrange(self, equation, solve_for):
        '''Solves one variable of an equation and returns the sympified version.'''

        return (sp.sympify(str(sp.solve(sp.sympify(equation), sp.sympify(solve_for)))), sp.parsing.sympy_parser.parse_expr(equation, evaluate=False))

    def separate_equation_fill(self, equation):
        '''Replaces the known variables of an equation with their numerical counterparts. Returns the sympified version.'''

        for i in range(len(self.known_vars)):
            if self.known_vars[i] in equation:
                equation = equation.replace(self.known_vars[i], str(self.vars_order[i]))
        return sp.parsing.sympy_parser.parse_expr(equation, evaluate=False)

    def separate_equation_fill_display(self, equation, display_vars_order):
        '''Replaces the known variables of an equation with their numerical counterparts. Returns the sympified version.'''
        for i in range(len(self.known_vars)):
            if self.known_vars[i] in equation:
                equation = equation.replace(self.known_vars[i], str(display_vars_order[i]))
        return sp.parsing.sympy_parser.parse_expr(equation, evaluate=False)

    def separate_equation_simplify(self, equation):
        '''Evaluates a single equation and returns the simplified and sympified version.'''

        equation = str(sp.simplify(sp.sympify(equation)))
        if ',' in equation:
            try:
                equation = eval(equation)
                for i in range(len(equation)):
                    if equation[i] >= 0:
                        equation = equation[i]
                        break
            except:
                equation = 'impossible'
        return sp.sympify(equation)

    def separate_equation_evaluate(self, equation):
        '''Evaluates a separate equation and returns the approximate and sympified version.'''

        equation = str(sp.simplify(sp.sympify(equation)))
        if ',' in equation:
            try:
                equation = eval(equation)
                for i in range(len(equation)):
                    if equation[i] >= 0:
                        equation = equation[i]
                        break
            except:
                equation = 'impossible'
        return sp.sympify(equation).evalf()

    def add_known_var(self, new_var, new_value):
        '''Adds known variable to object's known variable list.'''
        self.known_vars.append(new_var)
        self.vars_order.append(new_value)

    def get_known_vars(self):
        '''Returns object's known variables.'''

        return self.known_vars

    def get_equations(self):
        '''Returns object's equations.'''

        return self.equations

    def get_vars_order(self):
        '''Returns object's known variable numerical values.'''

        return self.vars_order

def check_if_unique(equation, variables):
    '''Global function that checks if an equation only consists of one variable. Returns True if unique, else returns False.'''

    counter = 0
    for i in range(len(variables)):
        if variables[i] in equation:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

### Problems ###

class ProjectileMotion(Problem):
    def __init__(self, equations, known_vars, vars_order, units, names, unknown_vars):
        super().__init__(equations, known_vars, vars_order)
        self.units = units
        self.names = names
        self.equations = equations
        self.display_equations = equations.copy() 
        self.display_vars_order = vars_order.copy() 
        self.unknown_vars = unknown_vars
        self.answer = ''
        self.show_full = True

        self.solve_for_velocity = True 
        
        if 'v_T' not in self.known_vars:
            self.solve_for_velocity = True
        else:
            self.solve_for_velocity = False  

        for i in range(len(self.get_equations())):
            self.equations_fill(i)

    def solve_it(self):
        self.not_yet_solved = []
        for i in range(len(self.unknown_vars)):
            solve_attempt = False
            for j in range(len(self.get_equations())):
                if solve_attempt is True:
                    continue
                if self.unknown_vars[i] in self.get_equations()[j]:
                    solved = self.separate_equation_rearrange(self.equations[j], self.unknown_vars[i])[0]
                    solved, solved_factor_sols = str(solved), solved
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
                            self.answer += str(r'@Solving for ' + self.names[self.unknown_vars[i]] + r':@')
                            self.answer += r'\newline@\newline@Using the equation,@' + r'\begin{equation*}' + sp.latex(sp.sympify(self.display_equations[j]), mode='plain') + ' = 0 ' + r'\end{equation*}' + '@Rearrange for $' + self.unknown_vars[i] + '$:@'
                            filler = str(self.separate_equation_rearrange(self.display_equations[j], self.unknown_vars[i])[0])[1:-1]

                            if ',' in filler: # selects answer of positive quadratic factor.
                                if solved_factor_sols[0] >= 0:
                                    filler = filler[:filler.find(',')] + ')'
                                else:
                                    filler = filler[filler.find(',')+2:]

                            self.answer += str(r'\begin{equation*}' + self.unknown_vars[i] + ' = ' + sp.latex(sp.sympify(filler), mode='plain') + r'\end{equation*}@') 

                            solved_fill = self.separate_equation_fill(filler)
                            solved_simplified = self.separate_equation_simplify(solved_fill)
                            solved_evaluated = self.separate_equation_evaluate(solved_fill)

                            solved_fill_display = sp.latex(self.separate_equation_fill_display(filler, self.display_vars_order), mode='plain')

                            if 'a_v' in filler:
                                self.answer += r'\begin{equation*}' + ' = ' + solved_fill_display
                            else:
                                self.answer += r'\begin{equation*}' + ' = ' + sp.latex(solved_fill, mode='plain')

                            solved_fill = self.separate_equation_fill(filler)
                            solved_simplified = self.separate_equation_simplify(solved_fill)
                            solved_evaluated = self.separate_equation_evaluate(solved_fill)

                            if 'a_v' == self.unknown_vars[i]:
                                solved_simplified, solved_evaluated = math.degrees(solved_evaluated), math.degrees(solved_evaluated)
                            if str(solved_fill) != str(solved_simplified):
                                try:
                                    self.answer += str(r'\end{equation*}' + r'@\begin{equation*}' + ' = ' + sp.latex(round(solved_simplified,2), mode='plain') + '\;' + self.units[self.unknown_vars[i]] + r'\end{equation*}@') 
                                except:
                                    self.answer += str(r'\end{equation*}' + r'@\begin{equation*}' + ' = ' + sp.latex(solved_simplified, mode='plain') + r'\end{equation*}@')
                            else:
                                self.answer += '\;' + self.units[self.unknown_vars[i]] + r'\end{equation*}@'

                            if str(solved_simplified)[str(solved_simplified).find('.'):str(solved_simplified).find('.')+3] != str(solved_evaluated)[str(solved_evaluated).find('.'):str(solved_evaluated).find('.')+3]:
                                try:
                                    self.answer += str(r'\begin{equation*}' + r'\;or\;' + sp.latex(round(solved_evaluated,2), mode='plain') + '\;' + self.units[self.unknown_vars[i]] + r'\end{equation*}@') 
                                except:
                                    self.answer += str(r'\begin{equation*}' + r'\;or\;' + sp.latex(round(solved_evaluated, 2), mode='plain') + r'\end{equation*}@')

                            # Called again to reset the values to radians.
                            if 'a_v' == self.unknown_vars[i]:
                                solved_fill = self.separate_equation_fill(filler)
                                solved_fill = str(solved_fill)
                                solved_simplified = self.separate_equation_simplify(solved_fill)
                                solved_evaluated = self.separate_equation_evaluate(solved_fill)
                        else:
                            solved_fill = self.separate_equation_fill(solved)
                            solved_fill = str(solved_fill)
                            solved_simplified = self.separate_equation_simplify(solved_fill)
                            solved_simplified = str(solved_simplified)
                            self.answer += self.unknown_vars[i] + ' = ' + solved_simplified + '\n'

                        try:
                            self.add_known_var(self.unknown_vars[i], str(round(solved_evaluated, 2)))
                            self.display_vars_order.append(round(solved_evaluated, 2))
                        except:
                            self.add_known_var(self.unknown_vars[i], str(solved_evaluated))
                            self.display_vars_order.append(solved_evaluated)

                        for t in range(len(self.equations)):
                            self.equations_fill(t)
                            solved, solved_fill, solved_simplified = '', '', ''
                            solve_attempt = True
                        else:
                            solved, solved_fill, solved_simplified = '', '', ''
                else:
                    solved, solved_fill, solved_simplified = '', '', ''
            if solve_attempt is False:
                self.not_yet_solved.append(self.unknown_vars[i])
            if self.unknown_vars[i] == self.unknown_vars[-1]:
                self.unknown_vars = self.not_yet_solved
                self.solve_it()
            if self.solve_for_velocity == True and 'v_T' in self.known_vars and 'a_v' in self.known_vars and 'v_x' in self.known_vars and 'v_y' in self.known_vars: # Solves the velocity vector when the magnitude and angle are found. 
                self.solved_velocity = (Vectors.get_vector([self.vars_order[self.known_vars.index('v_x')], self.vars_order[self.known_vars.index('v_y')]]))
                self.velocity_magnitude = self.solved_velocity[0]
                self.velocity_angle = self.vars_order[self.known_vars.index('a_v')]
                if self.show_full == True:
                    self.answer += 'Therefore, the magnitude and direction of initial velocity is:@'
                    self.answer += r'\begin{equation*}' + str(round(self.velocity_magnitude,2)) + r'\;m/s\;' + str(Vectors.get_directions([[self.velocity_magnitude, self.velocity_angle]])[0][1]).replace(' ', r'\;') + r'\end{equation*}@'
                else:
                    self.answer += 'initial velocity = ' + str(round(self.velocity_magnitude,2)) + ' m/s ' + str(Vectors.get_directions([[self.velocity_magnitude, self.velocity_angle]])[0][1]) + '\n'
                self.solve_for_velocity = False

    def __str__(self):
        return self.answer

    def get_solution_style(self):
        return self.show_full

    def get_answer(self):
        return self.answer

    def get_question_type(self):
        return 'Projectile Motion'
