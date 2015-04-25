__author__ = 'Will'

class color:
    R = 0
    G = 0
    B = 0

    def set(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b

    def get(self):
        return self

    @staticmethod
    def blue():
        result = color()
        result.B = 255
        return result

    @staticmethod
    def red():
        result = color()
        result.R = 255
        return result

    @staticmethod
    def green():
        result = color()
        result.G = 255
        return result