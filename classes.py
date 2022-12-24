class Person:
    def __init__(self, name, gender, profession,id):
        # data members (instance variables)
        self.name = name
        self.gender = gender
        self.profession = profession
        self.id = id

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Gender:', self.gender, 'Profession:', self.profession, self.id)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)


# create object of a class
Ali = Person('Ali', 'Male', 'Software Engineer',34)
Ahmed = Person('Ahmed', 'Male', 'Computer Engineer', 38)
hamza = Person('hamza', 'male','civil engineer', 40)

# call methods
Ali.show()
Ali.work()
Ahmed.show()
Ahmed.work()
hamza.show()
hamza.work()