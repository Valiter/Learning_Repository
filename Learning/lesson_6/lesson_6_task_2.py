class Road:
    # Атрибуты
    def __init__(self, lenght, width):
        self._lenght_inside = lenght
        self._width_inside = width

    def formula(self, _width_inside, _lenght_inside):
        asphalt = _lenght_inside * _width_inside * 25 * 5
        print(asphalt)

n_132 = Road()
n_154 = Road()
n_132.formula(12, 20)
