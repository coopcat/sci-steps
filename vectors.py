import sympy as sp
import math

# Vectors should be input into this class in the form: [[vector_one_magnitude, vector_one_angle]]

class Vectors(object):
    '''Performs vector operations.'''

    def __init__(self, vectors):
        for i in range(len(vectors)):
            vectors[i][1] = math.radians(vectors[i][1])
        self.vector_list = vectors

    def get_vector(components):
        '''Turns two components into a vector.'''

        components = [(sp.sympify(components[0])).evalf(), (sp.sympify(components[1])).evalf()]
        hypoteneuse = math.sqrt(components[0]**2 + components[1]**2)
        try:
            angle = math.degrees(math.asin(components[1]/hypoteneuse))
        except:
            angle = math.degrees(math.acos(components[0]/hypoteneuse))
        angle = round(angle, 2)
        return [hypoteneuse, angle]

    def get_sum(self):
        '''Gets sum of vectors in a vector list.'''

        new_sum = []
        x_components, y_component = 0, 0
        for i in range(len(self.vector_list)):
            x_component += self.vector_list[i][0] * math.cos(self.vector_list[i][1])
            y_component += self.vector_list[i][0] * math.sin(self.vector_list[i][1])
        x_component, y_component = round(x_component, 2), round(y_component, 2)
        try:
            new_sum = [round(x_component/math.cos(math.atan(y_component/x_component)), 10), round(math.degrees(math.atan(y_component/x_component)), 1)]
        except:
            try:
                new_sum = [round(y_component/math.sin(math.asin(y_component/math.sqrt(x_component**2 + y_component**2))), 1), round(math.degrees(math.asin(y_component/math.sqrt(x_component**2 + y_component**2))), 1)]
            except:
                new_sum = [0.0, 0.0]
        new_sum[1] = math.radians(new_sum[1])
        return [new_sum]

    def get_component(vector):
        '''Gets components from a vector.'''

        x_component, y_component = vector[0] * math.cos(vector[1]), vector[0] * math.sin(vector[1])
        return [x_component, y_component]

    def get_components(self):
        '''Gets components of vectors in a vector list.'''

        component_list, x_component, y_component = [], 0, 0
        for i in range(len(self.vector_list)):
            x_component = self.vector_list[i][0] * math.cos(self.vector_list[i][1])
            y_component = self.vedctor_list[i][0] * math.sin(self.vector_list[i][1])
            component_list.append([x_component, y_component])
            x_component, y_component = 0, 0
        return component_list

    def get_directions(vectors):
        '''Gets cardinal directions from an inputted list of vectors.'''

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
                    vector_list[i][1] = "[W " + str(abs(vector_list[i][1])) + r" S]"
                elif 90 < vector_list[i][1] < 180:
                    vector_list[i][1] = "[S " + str(abs(vector_list[i][1]) - 90) + r" E]"
                elif 180 < vector_list[i][1] < 270:
                    vector_list[i][1] = "[E " + str(abs(vector_list[i][1]) - 180) + r" N]"
                elif 270 < vector_list[i][1] < 360:
                    vector_list[i][1] = "[N " + str(abs(vector_list[i][1]) - 270) + r" W]"
                elif -90 < vector_list[i][1] < 0:
                    vector_list[i][1] = r"[W " + str(abs(vector_list[i][1])) + r" N]"
                elif -180 < vector_list[i][1] < -90:
                    vector_list[i][1] = r"[N " + str(abs(vector_list[i][1]) - 90) + r" E]"
                elif -270 < vector_list[i][1] < -180:
                    vector_list[i][1] = r"[E " + str(abs(vector_list[i][1]) - 180) + r" S]"
                elif -360 < vector_list[i][1] < -270:
                    vector_list[i][1] = r"[S " + str(abs(vector_list[i][1]) - 270) + r" W]"
        return vector_list  
