# Draft for lecture-02

var1 = "My String"
print(var1)
print(type(var1))
var1 = 100
print(var1)
print(type(var1))
print(var1 + 50)
print(type(int))
print(type(str))
print(type(True))
print(True)
print(int(True))
print(int(False))
# 
print()
print(bool(3.4)) # True
print(bool(-150)) # True
print(bool(0)) # False
print(bool(' ')) # True
print(bool('')) # False
print(3 == 5) # False
print(3 != 5) # True
print(3 > 5) # False
print(3 < 5) # True
print(3 >= 5) # False
print(3 <= 5) # True

print(9 > 7) and (2 < 4) # True
print(8 == 8) or (6 != 6) # True
print(not(3 <= 1)) # True

print()
x = 10
y = 4
print(x & y)   # 0
print(x | y)   # 14
print(~x)      # -11
print(x ^ y)   # 14
print(x >> 2)  # 2
print(x << 2)  # 40


print()
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1) # prints False
print(x2 is y2) # prints True
print(x3 is y3) # prints False, bacause both variables are strings and depend on different part of memory, but
print(x3 == y3) # True


print()
print(type(10)) # <class 'int'> Binary system
print(type(0o10)) # <class 'int'> Octal numeral system (oct)
print(type(0x10)) # <class 'int'> Hexadecimal numeral system (hex)

print()
print(isinstance(1, int)) # True
print(isinstance(0.1, int)) # False

print()
a = 10_000_000_000
print(a)

print()
print(bin(5))
print(hex(20))
print(oct(20))
x = 12.77
print(int(x))

print()
print(3 ** 150)

print(int()) # Print 0
print(int(42.0))
print(int("42"))

print()
x = 0.1 + 0.2 
print(x) # 0.30000000000000004

x = 0.1 + 0.1 
print(x) # 0.2

# Точність дійсних чисел дорівнює 15 знаків у дробній частині.
print(1.12345678901234567890) # 1.1234567890123457

import math
math.pi  # 3.141592653589793
math.sqrt(85) # 9.219544457292887
# Тригонометричні функції, наприклад sin(), cos(), tan(), та їх варіанти на кшталт asin().
math.sin(math.pi / 2) # 1.0
math.tan(math.pi / 4) # 0.99999999999999989

print()
# Import the Decimal class from the decimal module
from decimal import Decimal
# Create Decimal objects and perform addition
x = Decimal("0.1") + Decimal("0.2") 
# Print the result
print(x) # 0.3

print()
# Import decimal and getcontext from decimal module
from decimal import Decimal, getcontext
# Set precision
getcontext().prec = 4 
# getcontext()
# Define price and quantity as Decimal objects
price = Decimal("19.99")
qty = Decimal("3")
# Calculate total and print it
total = price * qty
# Print the total
print(total)  # 59.97

print()
print(Decimal('3.14'))
print(Decimal(3.14))

print()
value1 = Decimal('1.01')
value2 = Decimal('10.001')
print(value1, value2)
value1.quantize(value2)  # Decimal('1.010')
value2.quantize(value1) # Decimal('10.00')
print(value1.quantize(value2), value2.quantize(value1))


print()
getcontext().prec = 28
print(Decimal(10)) # Decimal('10')
print(Decimal('3.14')) # Decimal('3.14')
print(Decimal(3.14)) # Decimal('3.140000000000000124344978758017532527446746826171875')
print(Decimal((0, (3, 1, 4), -2))) # Decimal('3.14')
print(Decimal(str(2.0 ** 0.5))) # Decimal('1.4142135623730951')
print(Decimal(2) ** Decimal('0.5')) # Decimal('1.414213562373095048801688724')
print(Decimal('NaN')) # Decimal('NaN'))
print(Decimal('-Infinity')) # Decimal('-Infinity')) 





print()
print("foobar" == 'foobar')

print("This string contains a single quote (') character." )
print('This string contains a double quote (") character.' )

print('Цей рядок містить символ одинарної лапки (\').') # Одинарна лапка екрануэться символом \
print('foo\\bar') # Символ \ екрануэться символом \

raw_s = r'Hi\nHello' # префiкс r або R створюэ необроблений рядок
print(raw_s)

print( )
var = "string1"
print(var)
var = 1
print(var)
var += 2
print(var)

print()
s = 'foo'
t = 'bar'
u = 'baz'
print(s + t) # 'foobar'
print(s + t + u) # 'foobarbaz'
print('Go team' + '!!!') # Go team!!!

# s * n
# n * s
s = 'foo.'
print(s * 4) # 'foo.foo.foo.foo.'
print(4 * s) # 'foo.foo.foo.foo.'

hello = "hello"
print(hello[0]) # h
print(hello[1]) # e
print(hello[2]) # l
print(hello[3]) # l
print(hello[4]) # o

print(hello[0] * 100)

print("_" * 100)

print()
s = 'foo'
print(s in 'That\'s food for thought.') # True
print(s in 'That\'s good for now.') # False
# Оператор not in повертає False, якщо перший операнд міститься в другому, і True в іншому випадку
print('z' not in 'abc') # True
print('z' not in 'xyz') # False
# Рядки чутливі до регістру; 
Hello = "Hello"
hello = "hello"
print("Hello == hello: ", Hello == hello) # Hello == hello:  False
Hello_there = "Hello"
print("Hello == Hello_there:", Hello == Hello_there) # Hello == Hello_there:  True

print("---Strings---")
s = 'foobar'
print(s[0]) # 'f'
print(s[1]) # 'o'
print(s[3]) # 'b'
print(len(s)) # 6
print(s[len(s)-1]) # 'r'
# Кілька прикладів негативної індексації:
print(s[-1]) # 'r'
print(s[-2]) # 'a'
print(len(s)) # 6
print(s[-len(s)]) # 'f' first symbol
print(min(s))
print(max(s))
print(s.count("f"))
print(s.count("o"))
k = [1, 2, 3, 2, 2, 4]
print(k.count(2))  # 3
print(k.count(5))  # 0

print("---Slising---")
s = 'foobar'
print(s[2:5]) # 'oba'
print(s[2:5]) # 'oba'
# Перший символ у рядку має індекс 0. Другий індекс визначає перший символ, який не включено до 
# результату. Якщо опустити перший індекс, зріз починається на початку рядка:
print(s[:4]) # 'foob'
print(s[0:4]) # 'foob'
# Якщо ви опустите другий індекс, як у s[n:], зріз поширюється від першого індексу до кінця рядка. 
print(s[2:]) # 'obar'
print(s[:4] + s[4:]) # 'foobar'
# Якщо перший індекс у зрізі більший або дорівнює другому індексу, Python повертає порожній рядок:
print(s[2:2]) # Empty
print(s[4:2]) # Empty
# Індекс  -1 відноситься до останнього символу, -2 до передостаннього, і так далі.
print(s[-5:-2]) # 'oob'
print(s[-5:-2] == s[1:4]) # True

print(s[0:6:2]) # 'foa'
print(s[1:6:2]) # 'obr'
print(s[5:0:-2]) # 'rbo'
print(s[5:0:1]) # Empty

sentence = "Flat is better than nested"
words = sentence.split() # ['Flat', 'is', 'better', 'than', 'nested']
print(words)

print()
numbers = "1-2-3-4-5"
head, sep, tail = numbers.partition("-")
numbers.rpartition("-") # ('1-2-3-4', '-', '5')

name, age = "John", 30
print("Мене звати %s, мені %d років." % (name, age))
print("Мене звати {}, мені {} років".format(name, age))

ord('a') # 97
ord('#') # 35
ord('€') # 8364
ord('∑') # 8721
chr(97) # 'a'
chr(35) # '#'
chr(8364) # '€'
chr(8721) # '∑'
len( 'I am a string.') # 14
str(49.2) # '49.2'

print()
num1 = 100
num2 = 0
#op = '/'

try:
    print(f"{num1} / {num2} = {num1 / num2}")  # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

while x < 10:
    x += 1
else:
    print("x is not less than 10")

x = 3
while x < 10:
    x += 1
    if x == 7:
        continue
    print(x)
