class Father:
    def __init__(self, f_age):
        self.fage = f_age

    def father_style(self):
        print('father style')


class Son(Father):
    def __init__(self, f_age, s_age):
        super().__init__(f_age)
        self.sage = s_age

    def son_style(self):
        print('son style')


class GSon(Son):
    def __init__(self, f_age, s_age, g_age):
        super().__init__(f_age,s_age)
        self.gage = g_age

    def gson_style(self):
        print('gson style')
