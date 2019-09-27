print("hello,world")
message = "hello python world!"
print(message)
message = "hello"
print(message)
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'dd')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
last = motorcycles.pop()
print(last)
print(motorcycles)
m_name = motorcycles.pop(0)
print(m_name)
print(motorcycles)
motorcycles[0] = 'a'
print(motorcycles)
motorcycles.remove('a')
print(motorcycles)
motorcycles.append('a')
print(motorcycles)
motorcycles[0] = 'b'
print(motorcycles)
cars = ['a', 'c', 'b', 'h', 'g']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
cars.reverse()
print(cars)
print(cars.reverse())
print(cars)
print(len(cars))
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + 'good')
print("thank you  very much")
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
squares = list()
print(squares)
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
squares = [value ** 2 for value in range(1, 11)]
print(squares)
for value in range(1, 21, 2):
    print(value)
a = []
for x in range(3, 31):
    if x % 3 == 0:
        a.append(x)
print(a)
b = list(range(3, 31, 3))
for x in b:
    print(x)
player = ['a', 2, 3, 'b', 'c', 'd']
print(player[0:3])
print(player[:12])
a = [1, 2, 3, 4]
b = a[:]
a.insert(0,11)
print(b)
s = 'a b c d e'
for x in s:
    print(x)

J = 14
if J > 14:
    print(15)
elif J < 14:
    print(13)
else:
    print(14)
g = []
if g:
    print(1)
else:
    print(2)
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
del alien_0['points']
print(alien_0)
for key, value in alien_0.items():
    print(key+value)
for key in alien_0.keys():
    print(key.title())
if 'co' not in alien_0.keys():
    print(11)
for name in sorted(alien_0.keys()):
    print(name)
for color in alien_0.values():
    print(color)
q = {1: 2, 1: 1, 3: 2, 4: 4}
for n in set(q.values()):
    print(n)
# message = input("tell me somthing and t will tell you: ")
print(message)
print("测试feature")


def name(pet, me):
    print(pet, me)


name(me="mf", pet=1)


def test1(mr, gi, **c):
    p = {}
    p['name'] = mr
    p['age'] = gi
    for k, v in c.items():
        p[k] = v
    return p


q = test1("nn", "mm", gg="ii", pp="gg")
print(q)

app = {1: 1, 2: 2}
print(app[1])

def test2(m, g, *k, **l):
    
