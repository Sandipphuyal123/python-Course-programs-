# .items(), .Keys(), .values() function
Std_id = {
    'name': 'Sandip Phuyal',
    'Location': 'MaitiDevi',
    'Age': 20,
    'Course': 'Bachelor of Information Technology'
}
print('Values of the Dictionary')
for index, titles in  enumerate(Std_id.values()):
    print(f'{index}. {titles}')
print('Keys of the Dictionary')
for index, titles in  enumerate(Std_id.keys()):
    print(f'{index}. {titles}')
print("Dictionary content's")
for index, titles in  enumerate(Std_id.items()):
    print(f'{index}. {titles}')
