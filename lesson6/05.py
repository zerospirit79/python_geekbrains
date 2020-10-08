'''
5. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


class Example:
    attr1: int
    _attr2: int

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def get_attr2(self):
        return self.attr2


ex1 = Example(5, 7)
print(ex1.attr1)
print(ex1.get_attr2())
