class person:
    def __init__(self, name, age, email, hobbies):
        self.name = name 
        self.age = age 
        self.email = email 
        self.hobbies = hobbies
obj = person('sandip', 20, 'FakeEmail101@gmail.com', 'playing_Chess')

for attr in dir(obj):
    if not attr.startswith('__') and not callable(getattr(obj, attr)):
        value = getattr(obj, attr)
        print(f'{attr}: {value}')