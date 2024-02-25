x = 5+3
print(x)

print(type(x))

print(True and False)

def num(x):
    f = x+4
    print(f)
    return f
num(5)

def wage(wh):
    return wh * 25

def bonus(wh):
    return wage(wh) + 50

print(wage(8), bonus(8))

def add(m):
    if m > 10:
        m = m + 10
        return m
    else:
        return "Save More!"

print(add(11))

print(int(5.7))
print(max(10, 20, 30))
print(abs(-2))
print(round(3.4, 2))
print(pow(10, 2))
print(2**10)
print(len('Mathematics'))

list1 = [1, 2, 3, 4, 5]
print(sum(list1))
print(list1[-1])

del list1[2]
print(len(list1))
list1[1] = 7
print(list1)

list1.append(6)
print(list1)
list1.extend([7, 8, 9, 10])
print(list1)
print('Ayush got ' + str(list1[1]) + ' Marks in coding test')
print()
print(list1)
print(list1[-1])
print(list1[3::])
print(list1[::-3])
print(list1[1:6])
print(list1[1:8:2])

print()
list1.sort()
print(list1)
list1.reverse()
print(list1)

test = "Jayant is boi"
x = test.split(" ")
print(x)

dict = {'k1': "cat", 'k2': "dog", 'k3': "mouse",
        'k4': "dog"}  # No Append in Dictionaries
print(dict["k1"])


n = [1, 3, 53, 2, 6, 6, 1, 6, 2, 6, 23, 26, 34, 2, 6, 6, 31, 523, 3, 6, 2]
for i in n:
    print(i, end=" ")

print()
for i in range(1, 6):  # range(len(arrayname))
    print(i, end=" ")

print()
student_grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}

for name, grade in student_grades.items():
    print(f"{name}: {grade}")
for grade in student_grades.values():
    print(grade)

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):  # enumerate is important for index
    print(f"Index {index}: {fruit}")

x = 0
while x <= 20:
    print(x, end=" ")
    x += 2

print(list(range(10)))
print(list(range(3, 7)))
print(list(range(3, 7, 2)))

number = [1, 12, 3, 4, 53, 100]
new_number=[]
for n in number:
    new_number.append(n * 2)
print(new_number)

#list comprehension - we can write shorter code - The above code in just 2 lines
new_numbers = [n * 2 for n in number]
print(new_numbers)

new_list = [i+j for i in range(2) for j in range(5)]
print(new_list)

print([num ** 3 for num in range(1,12) if num % 2 !=0])
print([num ** 3 if num%2!=0 else "even" for num in range(1, 11)])

quantities = 'Jayant'
print("Ayush Loves %s" %quantities) # %d for integers & #f for float values

length = 8.0
width = 4.0
print('The dimension are %.2f feet long & %.2f feet wide' % (length, width))
print('The dimension are {length:.2f} feet long & {width:.2f} feet wide'.format(length=length, width=width))

s = 'price per unit'
s1 = s.replace('price', 'cost')
print(s1)

print(s1.startswith('cost'))
print(s1.endswith('nit'))
print(s1.split('s')), print(s1.split(' '))

s4 = ' cayman foda ahe '
print(s4.strip(' cay'))

#Promting a password
import getpass
password = getpass.getpass('Your Password')
print(password)



