# 1.Доопрацюйте класс Point так, щоб в атрибути х та у обʼєктів цього класу можна було записати тільки числа.
#  Використовуйте property
# 2.Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
#  Реалізуйте перевірку даних, що пишуться в точки аналогічно до класу Line.
#  Визначет атрибут, що містить площу трикутника (за допомогою property).
#  Для обчислень можна використати формулу Герона

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


class Triangle:
    point_a = None
    point_b = None
    point_c = None

    def __init__(self, init_a, init_b, init_c):
        self.a = init_a
        self.b = init_b
        self.c = init_c

    @property
    def a(self):
        return self.point_a

    @a.setter
    def a(self, new_a):
        if not isinstance(new_a, Point):
            raise TypeError
        self.point_a = new_a

    @property
    def b(self):
        return self.point_b

    @b.setter
    def b(self, new_b):
        if not isinstance(new_b, Point):
            raise TypeError
        self.point_b = new_b

    @property
    def c(self):
        return self.point_c

    @c.setter
    def c(self, new_c):
        if not isinstance(new_c, Point):
            raise TypeError
        self.point_c = new_c

    @property
    def triangle_area(self):
        """
        Расчёт площади треугольника по формуле Герона
        :return: Площадь треугольника в формате Float
        """
        ab = ((((self.point_a.crd_x - self.point_b.crd_x) ** 2) + ((self.point_a.crd_y - self.point_b.crd_y) ** 2)) +
              ((self.point_a.crd_z - self.point_b.crd_z) ** 2)) ** 0.5

        ac = ((((self.point_a.crd_x - self.point_c.crd_x) ** 2) + ((self.point_a.crd_y - self.point_c.crd_y) ** 2)) +
              ((self.point_a.crd_z - self.point_c.crd_z) ** 2)) ** 0.5

        bc = ((((self.point_b.crd_x - self.point_c.crd_x) ** 2) + ((self.point_b.crd_y - self.point_c.crd_y) ** 2)) +
              ((self.point_b.crd_z - self.point_c.crd_z) ** 2)) ** 0.5

        p = (ab + ac + bc) / 2
        area = ((p - ab) * (p - ac) * (p - bc)) ** 0.5
        return area


a = Point(init_x=0, init_y=0, init_z=0)
b = Point(init_x=1, init_y=1, init_z=1)
c = Point(init_x=0, init_y=1, init_z=0)
abc = Triangle(init_a=a, init_b=b, init_c=c)

print(abc.triangle_area)
print(type(abc.triangle_area))
