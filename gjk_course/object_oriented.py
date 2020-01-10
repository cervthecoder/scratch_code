
# objekt je věc, která má v sobě nějká data a nějaké funkce


class person_1:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def speak(self, text):
        print(f'Hello my name is {self.age}, {text}')

matej = person_1('Matěj', 16, 177, 66)

matej.speak('and I hate objects')
person_1.speak(matej, 'COOOOL') # to je to samé


# @dataclass
# class person_2:
#     name: str
#     age: int
#     height: int
#     weight: int

# data spojená s člověkem





