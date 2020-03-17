import sympy as sp
import math

# Sample format for how lists of vectors should be input: vector_list = [[-100, -359]]

class Vectors(object):
    def __init__(self, vectors):
        for i in range(len(vectors)):
            vectors[i][1] = math.radians(vectors[i][1])
        self.vector_list = vectors

    def get_vector(components):
        '''Takes in two components in an array and returns a vector in array form.'''
        components = [(sp.sympify(components[0])).evalf(), (sp.sympify(components[1])).evalf()]
        hypoteneuse = math.sqrt((components[0])**2 + (components[1])**2)
        try:
            angle = math.degrees(math.asin(components[1]/hypoteneuse))
        except:
            angle = math.degrees(math.acos(components[0]/hypoteneuse))
        angle = round(angle, 2)
        return [hypoteneuse, angle]

    def get_sum(self):
        new_sum = []
        x_component = 0
        y_component = 0
        for i in range(len(self.vector_list)):
            x_component += self.vector_list[i][0] * math.cos(self.vector_list[i][1])
            y_component += self.vector_list[i][0] * math.sin(self.vector_list[i][1])
        x_component = round(x_component, 2)
        y_component = round(y_component, 2)
        # These specific trigonometric relations had to be used to fix a bug that occured when solving certain problem types.
        try:
            new_sum = [round(x_component/math.cos(math.atan(y_component/x_component)), 10), round(math.degrees(math.atan(y_component/x_component)), 1)]
        except:
            try:
                new_sum = [round(y_component/math.sin(math.asin(y_component/math.sqrt(x_component**2 + y_component**2)))), round(math.degrees(math.asin(y_component/math.sqrt(x_component**2 + y_component**2))), 1)]
            except:
                new_sum = [0.0, 0.0]
        new_sum[1] = math.radians(new_sum[1])
        return [new_sum]

    def get_component(vector):
        x_component = vector[0] * math.cos(vector[1])
        y_component = vector[0] * math.sin(vector[1])
        return [x_component, y_component]

    def get_components(self):
        component_list = []
        x_component = 0
        y_component = 0
        for i in range(len(self.vector_list)):
            x_component = self.vector_list[i][0] * math.cos(self.vector_list[i][1])
            y_component = self.vector_list[i][0] * math.sin(self.vector_list[i][1])
            component_list.append([x_component, y_component])
            x_component, y_component = 0, 0
        return component_list
    
    def get_directions(vectors): # Cardinal directions 
        vector_list = vectors
        for i in range(len(vector_list)):
            vector_list[i][1] = round(math.degrees(sp.sympify(vector_list[i][1]).evalf()), 1)
        for i in range(len(vector_list)):
            if vector_list[i][0] > 0:
                if abs(vector_list[i][1]) == 0:
                    vector_list[i][1] = "[E]"
                elif abs(vector_list[i][1]) == 90:
                    vector_list[i][1] = "[N]"
                elif abs(vector_list[i][1]) == 180:
                    vector_list[i][1] = "[W]"
                elif abs(vector_list[i][1]) == 270:
                    vector_list[i][1] = "[S]"
                elif abs(vector_list[i][1]) == 360:
                    vector_list[i][1] = "[E]"
                elif 0 < vector_list[i][1] < 90:
                    vector_list[i][1] = r"[E " + str(vector_list[i][1]) + r" N]"
                elif 90 < vector_list[i][1] < 180:
                    vector_list[i][1] = r"[N " + str(vector_list[i][1] - 90) + r" W]"
                elif 180 < vector_list[i][1] < 270:
                    vector_list[i][1] = r"[W " + str(vector_list[i][1] - 180) + r" S]"
                elif 270 < vector_list[i][1] < 360:
                    vector_list[i][1] = r"[S " + str(vector_list[i][1] - 270) + r" E]"
                elif -90 < vector_list[i][1] < 0:
                    vector_list[i][1] = r"[E " + str(abs(vector_list[i][1])) + r" S]"
                elif -180 < vector_list[i][1] < 90:
                    vector_list[i][1] = r"[S " + str(abs(vector_list[i][1]) - 90) + r" W]"
                elif -270 < vector_list[i][1] < -180:
                    vector_list[i][1] = r"[W " + str(abs(vector_list[i][1]) - 180) + r" N]"
                elif -360 < vector_list[i][1] < -270:
                    vector_list[i][1] = r"[N " + str(abs(vector_list[i][1]) - 270) + r" E]"
            elif vector_list[i][0] < 0:
                vector_list[i][0] = abs(vector_list[i][0])
                if abs(vector_list[i][1]) == 0:
                    vector_list[i][1] = "[W]"
                elif abs(vector_list[i][1]) == 90:
                    vector_list[i][1] = "[S]"
                elif abs(vector_list[i][1]) == 180:
                    vector_list[i][1] = "[E]"
                elif abs(vector_list[i][1]) == 270:
                    vector_list[i][1] = "[N]"
                elif abs(vector_list[i][1]) == 360:
                    vector_list[i][1] = "[W]"
                elif 0 < vector_list[i][1] < 90:
                    vector_list[i][1] = "[W " + str(abs(vector_list[i][1])) + " S]"
                elif 90 < vector_list[i][1] < 180:
                    vector_list[i][1] = "[S " + str(abs(vector_list[i][1]) - 90) + " E]"
                elif 180 < vector_list[i][1] < 270:
                    vector_list[i][1] = "[E " + str(abs(vector_list[i][1]) - 180) + " N]"
                elif 270 < vector_list[i][1] < 360:
                    vector_list[i][1] = "[N " + str(abs(vector_list[i][1]) - 270) + " W]"
                elif -90 < vector_list[i][1] < 0:
                    vector_list[i][1] = r"[W " + str(abs(vector_list[i][1])) + r" N]"
                elif -180 < vector_list[i][1] < -90:
                    vector_list[i][1] = r"[N " + str(abs(vector_list[i][1]) - 90) + r" E]"
                elif -270 < vector_list[i][1] < -180:
                    vector_list[i][1] = r"[E " + str(abs(vector_list[i][1]) - 180) + r" S]"
                elif -360 < vector_list[i][1] < -270:
                    vector_list[i][1] = r"[S " + str(abs(vector_list[i][1]) - 270) + r" W]"
        return vector_list
