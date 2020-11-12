from typing import List

from PIL import Image
import numpy
from numpy import asarray

me = '[Sobel]'
count = 0


class Sobel:

    def __init__(self, filename, Threshold, Gx: List = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]],
                 Gy: List = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]):
        self.filename = filename
        self.threshold = Threshold
        self.Gx = Gx
        self.Gy = Gy
        self.img = Image.open(self.filename)
        self.processThis = asarray(self.img)
        self.Gx = asarray(self.Gx)
        self.Gy = asarray(self.Gy)
        self.rows, self.columns, self.depth = self.processThis.shape
        self.result = Image.new(self.img.mode, (self.rows, self.columns))
        self.result1 = self.result.load()
        self.mag = Image.new(self.img.mode, (self.rows, self.columns))
        self.magMap = self.mag.load()
        self.NormI = Image.new(self.img.mode, (self.rows, self.columns))
        self.sobel()

    def sobel(self) -> Image:
        mag = []
        maxScalar = 0
        for i in range(self.rows - 2):
            for j in range(self.columns - 2):
                S1 = self.Gx.dot(self.processThis[i:i + len(self.Gx), j:j + len(self.Gy), 0] + \
                                 self.processThis[i:i + len(self.Gx), j:j + len(self.Gy), 1] + \
                                 self.processThis[i:i + len(self.Gx), j:j + len(self.Gy), 2]) / 8
                S2 = self.Gy.dot(self.processThis[i:i + len(self.Gx), j:j + len(self.Gy), 0] + \
                                 self.processThis[i:i + len(self.Gx), j:j + len(self.Gy), 1] + \
                                 self.processThis[i:i + len(self.Gx), j:j + len(self.Gy), 2]) / 8

                mag_scalar = numpy.linalg.norm((numpy.sum(S1) ** 2) + (numpy.sum(S2) ** 2))

                self.magMap[i, j] = (int(mag_scalar), 0, 0)

                if mag_scalar > maxScalar:
                    maxScalar = mag_scalar

                if self.magMap[i, j][0] >= self.threshold:
                    self.result1[i, j] = (0, 0, 0)
                else:
                    self.result1[i, j] = (255, 255, 255)

        print("Max Gradient: " + str(maxScalar))
        maxGradient = maxScalar
        NormalizedGradient = self.NormI.load()

        for i in range(self.rows):
            for j in range(self.columns):
                NormalizedGradient[i, j] = (int((self.magMap[i, j][0] / 1028) * 255), 0, 0)
                print(NormalizedGradient[i, j][0])
                if NormalizedGradient[i, j][0]:
                    NormalizedGradient[i, j] = (0, 0, 0)
                else:
                    NormalizedGradient[i, j] = (255, 255, 255)
        global count
        count += 1
        self.NormI.save('Normalized_Gradient_' + str(count) + self.filename)
        print(me + 'INFO>Successfully Edge Detected with Sobel')

        return self.NormI


if __name__ == '__main__':
    obj = Sobel("logo.png", 200)
    obj.result.save('sobel_' + obj.filename)
    # laplacian
    lap = Sobel("logo.png", 200, [[0, -1, 0], [-1, 4, -1], [0, -1, 0]], [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    obj.result.save('laplacian_' + obj.filename)
