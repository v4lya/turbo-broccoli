my_rect_x = int(input("Введите одну из сторон вашего прямоугольника: "))
my_rect_y = int(input("Введите вторую из сторон вашего прямоугольника: "))
my_square_t = int(input("Введите одну из сторон вашего квадрата: "))


class Rectangle():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        print("1")
    def calc_perim(self):
        return (self.x + self.y) *2, " см"
class Square():
    def __init__(self, t):
        self.t = t
        print("1")
    def calc_perimm(self):
        h = self.t *4, " см"
        self.h = h
        return self.h
    def change_size(self):
        quest = int(input(" Хотите изменить значение квадрата? Если нет, то введите 0"))
        return ((self.t) - 1) *4
        return 
        
    
my_square = Square(my_square_t)
print(my_square.calc_perimm())
print(my_square.change_size())
my_rect = Rectangle(my_rect_x, my_rect_y)
print(my_rect.calc_perim())

