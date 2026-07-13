class person:
    def __init__(self, name, age, location):
        self.name =name
        self.age = age
        self.location = location
    
obj_1 = person('Sandip', 20, 'maitidevi')
attr_name = input('enter the attribute you want to see: ')
print(getattr(obj_1, attr_name, "Attr not found!"))