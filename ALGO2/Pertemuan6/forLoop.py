data = [1,2,3,4,5]
for i in data:
    print(i)

print('\n')
for y in range(2,7) :
    print('ayo berhitung',y)
print('\n')

fruits = ['apel','duren','pisang','nanas']
number = [1,3,4,6,7,8]
for fruit in fruits:
    print(fruit)
print('\n')
for index,fruit in enumerate(fruits)  :
    print(index,fruit)
print('\n')
for number,fruit in zip(number,fruits):
    print(number,fruit)


print('\n')
names = 'Joko Anwar'
for name in names:
    print(name)

biodata = {'Nama':'Joko Anwar','NIM':2000120}
for data in biodata:
    print(data)
for value in biodata.values():
    print(value)
for label,value in biodata.items():
    print(label,':',value)

print('\n')
for i in range(1,11):
    if i % 2 == 0 :
        print(i,'adalah bilangan genap')
    else:
        print(i,'adalah bilangan ganjil')