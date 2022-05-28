# Доопрацюйте класс Triangle таким чином, щоб він підтримував інтерфейс ітератора.
# Ітератор повинен віддавати сторони трикутника (обʼєкт класу Line)

class Point:
    crd_x = 0
    crd_y = 0
    crd_z = 0

    def __init__(self, init_x, init_y, init_z):
        self.x = init_x
        self.y = init_y
        self.z = init_z

    @property
    def x(self):
        return self.crd_x

    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError
        self.crd_x = new_x

    @property
    def y(self):
        return self.crd_y

    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError
        self.crd_y = new_y

    @property
    def z(self):
        return self.crd_z

    @z.setter
    def z(self, new_z):
        if not isinstance(new_z, (int, float)):
            raise TypeError
        self.crd_z = new_z


class Line:
    point_1 = None
    point_2 = None

    def __init__(self, init_p1, init_p2):
        self.p1 = init_p1
        self.p2 = init_p2

    @property
    def p1(self):
        return self.point_1

    @p1.setter
    def p1(self, new_1):
        if not isinstance(new_1, Point):
            raise TypeError
        self.point_1 = new_1

    @property
    def p2(self):
        return self.point_2

    @p2.setter
    def p2(self, new_2):
        if not isinstance(new_2, Point):
            raise TypeError
        self.point_2 = new_2

    @property
    def line_length(self):
        '''
        Функция расчитывает длину линии
        :return: Длина линии в формате Float
        '''
        res = ((((self.point_1.crd_x - self.point_2.crd_x) ** 2) + ((self.point_1.crd_y - self.point_2.crd_y) ** 2)) +
               ((self.point_1.crd_z - self.point_2.crd_z) ** 2)) ** 0.5
        return res


class Triangle:
    point_1 = None
    point_2 = None
    point_3 = None
    line_1 = None
    line_2 = None
    line_3 = None
    _idx = 0
    _val = []

    def __init__(self, init_p1, init_p2, init_p3):
        self.p1 = init_p1
        self.p2 = init_p2
        self.p3 = init_p3
        self.line_1 = Line(init_p1=self.point_1, init_p2=self.point_2)
        self.line_2 = Line(init_p1=self.point_2, init_p2=self.point_3)
        self.line_3 = Line(init_p1=self.point_1, init_p2=self.point_3)

    def __iter__(self):
        self._val = [getattr(self, name) for name in dir(self) if name.startswith('line')]
        return self

    def __next__(self):
        try:
            res = self._val[self._idx]
        except IndexError:
            raise StopIteration
        else:
            self._idx += 1
            return res

    @property
    def p1(self):
        return self.point_1

    @p1.setter
    def p1(self, new_1):
        if not isinstance(new_1, Point):
            raise TypeError
        self.point_1 = new_1

    @property
    def p2(self):
        return self.point_2

    @p2.setter
    def p2(self, new_2):
        if not isinstance(new_2, Point):
            raise TypeError
        self.point_2 = new_2

    @property
    def p3(self):
        return self.point_3

    @p3.setter
    def p3(self, new_3):
        if not isinstance(new_3, Point):
            raise TypeError
        self.point_3 = new_3

    @property
    def triangle_area(self):
        """
        Расчёт площади треугольника по формуле Герона
        :return: Площадь треугольника в формате Float
        """
        len1 = self.line_1.line_length
        len2 = self.line_2.line_length
        len3 = self.line_3.line_length

        p = (len1 + len2 + len3) / 2
        area = ((p - len1) * (p - len2) * (p - len3)) ** 0.5
        return area


a = Point(init_x=0, init_y=0, init_z=0)
b = Point(init_x=3, init_y=4, init_z=0)
c = Point(init_x=0, init_y=1, init_z=0)

ab = Line(init_p1=a, init_p2=b)

abc = Triangle(init_p1=a, init_p2=b, init_p3=c)

print(a)
print(ab)
print(abc)
print(type(abc.point_1))
print(type(abc.line_1))
print(ab.line_length)
print(abc.triangle_area)

for i in abc:
    print(i.line_length)
    print(type(i))

