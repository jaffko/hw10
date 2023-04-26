class Dragon:
    def __init__(self, height, danger, color) -> None:
        self.height = height
        self.danger = danger
        self.color = color
    
    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.danger} and color {self.color}'
    
    def __repr__(self) -> str:
        return f'Dragon({self.height}, {self.danger}, {self.color})'
    
    def color_num(self):
        return ord(self.color[0]) - ord('a') + 1
    
    def __eq__(self, object):
        return self.height == object.height and self.danger == object.danger and self.color_num() == object.color_num()
    
    def __ge__(self, object):
        return self.height >= object.height and self.danger >= object.danger and self.color_num() >= object.color_num()
    
    def __le__(self, object):
        return self.height <= object.height and self.danger <= object.danger and self.color_num() <= object.color_num()
    
    def __gt__(self, object):
        return self.height > object.height and self.danger > object.danger and self.color_num() > object.color_num()
    
    def __lt__(self, object):
        return self.height < object.height and self.danger < object.danger and self.color_num() < object.color_num()
    
    def __add__(self, object):
        import math
        d2_h = math.floor((self.height + object.height)/2)
        d2_d = max(self.danger, object.danger)
        d2_c = self.color
        if self.color_num() > object.color_num():
            d2_c = object.color
        return Dragon(d2_h, d2_d, d2_c)
    
    def __sub__(self, number):
        self.height -= self.height // number
        self.danger += self.danger % number
        return self

    def change_color(self, new_color):
        self.color = new_color

    def __call__(self, word):
        return word * self.danger


dr = Dragon(69, 5, 'brown')
dr1 = Dragon(69, 5, 'gray')
print(dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep='\n')
print()
dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")
print(dr('Welcome'))
