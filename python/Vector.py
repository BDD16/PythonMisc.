import math


me = '[Vector]'
THREE_D = 3

'''
Vector is an elementary vector which inputs are dimensions which is an int and
values which is meant to be an array of length dimensions.
'''
class Vector:
    #class to define an arbitrary vector of n elements long
    def __init__(self,dimensions,values):
        self.n = dimensions
        self.values = values
        if dimensions != len(values):
            print me + 'Please put in all values of your vector'
            return None
        self.vector = {}
        self.BuildVector()

    '''
    Builds a vector through a dictionary where the key is the string value of the
    dimensions i.e. int(1) = '1' int(2) = '2'...int(n) = 'n'
    '''
    def BuildVector(self):
        try:
            for i in range(self.n):
                self.vector[str(i)] = self.values[i]
        except OSError as e:
            print me + 'ERROR SOMEWHERE POSSIBLY OVERLOAD ERROR: ' + str(e)


    '''
    ThreeDVector is a shortcut to make a quick vector of three dimensions
    @input dimensions is the integer number of dimensions, checks that this is
    three
    @input values are the values of the vector
    '''
    def ThreeDVector(self, dimensions, values):
        if self.dimensions == THREE_D and len(values) == THREE_D:
            for i in range(3):
                self.vector[str(i)] = values[i]

    '''
    VectorAddition adds two vectors of the same dimensions together
    @input vector1 is the first vector
    @input vector2 is the second vector
    '''
    def VectorAddition(self, vector1, vector2):
        if isinstance(vector1, Vector):
            print me + 'vector1 is of Type Vector'
        else:
            print me + 'vector1 is not of Type Vector returning None'
            return None
        if isinstance(vector2, Vector):
            print me + 'vector2 is of Type Vector'

        else:
            print me + 'vector2 is not of Type Vector returning None'
            return None
        if vector1.n == vector2.n:
            x = Vector(vector1.n, vector1.values)
            try:
                for i in range(vector1.n):
                    x.vector[str(i)] = vector1.vector[str(i)] + vector2.vector[str(i)]
            except OSError as e:
                print me + 'DEBUG> something went wrong with adding vectors, returning None: ' +str(e)
                return None

            return x

        else:
            print me + 'Vector is not of correct dimensions'

'''
example usage
'''
if __name__ == '__main__':
    x = Vector(3, [1,2,3])
    y = Vector(3,[1,2,3])

    print(x.vector)
    print(y.vector)
    z = x.VectorAddition(x, y)
    print(z.vector)
