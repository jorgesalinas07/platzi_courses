class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello, my name us {} and I am {} years old'.format(self.name, self.age))
    
if __name__=="__main__":
    persona = Person('david', '34')

    print('Age: {}'.format(persona.age))
    persona.say_hello()