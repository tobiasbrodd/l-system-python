class System():
    pass

class PlantSystem(System):
    def __init__(self):
        self.start = 'X'
        self.rules = {'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF', '[': '[', ']': ']', '+': '+', '-': '-'}
        self.d_vars = ['F']
        self.d_opt = {'F': 'g-'}
        self.a_inc_vars = ['+']
        self.a_dec_vars = ['-']
        self.a_inc = 25.0
        self.a_dec = 25.0
        self.s_app_vars = ['[']
        self.s_pop_vars = [']']

class TreeSystem(System):
    def __init__(self):
        self.start = '0'
        self.rules = {'0': '1[0]0', '1': '11', '[': '[', ']': ']'}
        self.d_vars = ['0', '1']
        self.d_opt = {'0': 'r-', '1': 'g-'}
        self.a_inc_vars = ['[']
        self.a_dec_vars = [']']
        self.a_inc = 45.0
        self.a_dec = 45.0
        self.s_app_vars = ['[']
        self.s_pop_vars = [']']

