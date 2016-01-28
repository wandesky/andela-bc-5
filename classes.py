class Vehicle(object):

    def __init__(self, engine_type, **kwargs):
        self.engine_type = engine_type
        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_color(self, color):
        self.color = color

    def set_speed(self, speed):
        self.speed = speed


class Truck(Vehicle):

    doors = 2

    def __init__(self, engine_type, wheels, **kwargs):
        super(Truck, self).__init__(engine_type, **kwargs)
        self.wheels = wheels


class Car(Vehicle):

    wheels = 4
    doors = 5

    def __init__(self, engine_type, category, **kwargs):
        super(Car, self).__init__(engine_type, **kwargs)
        self.category = category


def output(instance):
    print "Printing: {}".format(instance.__class__.__name__)
    for attr in dir(instance):
        attribute = getattr(instance, attr)
        # don't print "private" methods/attributes and methods.
        if attr[:2] not in ('_', '__') and not hasattr(attribute, '__call__'):
            print("{}: {}".format(attr, attribute))
    print


car = Car('V12', 'sport', **{'colour': 'white', 'model': 'Camaro Z12', 'top_speed': 200 * 1.6})
truck = Truck('V10', '24', color='black', model="MACK")

output(car)

output(truck)
