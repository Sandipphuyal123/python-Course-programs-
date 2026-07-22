class dogInfo:
    def __init__(self,name,breed,age,gender,Neutered):
        self.d_name = name
        self.d_breed = breed
        self.d_age = float(age)
        self.d_gender = gender
        self.d_neutered = bool(Neutered)
    
dog_info_db = []
    
while True:
    name = input('enter your dog name (type "exit" to stop): ')
    if name.lower() == 'exit':
        break
    breed = input('What is your dog breed: ')
    age = float(input('How old is your your dog?: '))
    gender = input('is your dog male or female: ')
    Neutered = input('is your dog Neutered or not: ')
    
    dogInfo_obj = dogInfo(name,breed,age,gender,Neutered)
    dog_info_db.append(dogInfo_obj)
print("\n--- Current Dog Database ---")
for dog_info in dog_info_db:
    print(f"Name: {dog_info.d_name} | Breed: {dog_info.d_breed} | Age: {dog_info.d_age} years | Gender: {dog_info.d_gender} | Neutered: {dog_info.d_neutered}")