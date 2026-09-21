#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\HP\Documents\llm_wiki\llm-wiki\diff\20260922_Python__ingest\pages\wiki'
SRC = '[[raw/tutorials/Python/20260921_Python_]]'
TODAY = '2026-09-21'

for d in ['concepts','comparisons','entities','practice']:
    os.makedirs(os.path.join(BASE, d), exist_ok=True)

def mk(kind, tags, title, body):
    return f'''---
title: {title}
kind: {kind}
status: 
understanding_level: 1
need_practice: true
last_review: {TODAY}
source: "{SRC}"
source_type: tutorial
tags:
  - python
  - {tags[0]}
---

{body}'''

def w(rel, content):
    path = os.path.join(BASE, rel)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {rel}')

# 
# CONCEPTS
# 

w('concepts/.md', mk('concept', ['',''], '', '''## 

` = ` Python {SRC}#2. 

```python
name = ''
age = 18
weight = 65.2
```

> [!warning]
>  a=10a  a  10 {SRC}#2.1. 

## 

Python {SRC}#2.3. 

```python
ADULT_AGE = 18
MONTHS_IN_YEAR = 12
MAX_USERS = 1200
```

 Python 

## 

{SRC}#2.2. 

1. 
2. Name  name 
3. FalseNoneTrueandasassertasyncawaitbreakclasscontinuedefdelelifelseexceptfinallyforfromglobalifimportinislambdanonlocalnotorpassraisereturntrywhilewithyield
4. 
5. 

 Python snake_case user_name
'''))

w('concepts/.md', mk('concept', ['int','float','str'], '', '''## 

{SRC}#5. 

|  |  |  |  |
| --- | --- | --- | --- |
| **** | int | 5, -3, 0, 2025 |  |
| **** | float | 3.14, -0.01 |  |
| **** | str | Hello, Python |  |

> [!tip]
> 

## 

 type() type() {SRC}#5.2. 

```python
result1 = type('')   # <class 'str'>
result2 = type(18)      # <class 'int'>
result3 = type(72.5)    # <class 'float'>
print(result1, result2, result3)
```

> [!warning]
>  Python 

## int

Python {SRC}#5.3. 

```python
num1 = 10_000_000  # 
print(num1)  # 10000000
```

Python  print  4300 

## float

{SRC}#5.4. 

```python
weight = 65.2
speed_of_sound = 3.4e+2  # 
```

## str

{SRC}#5.5. 

```python
message1 = ''
message2 = ""
message3 = ''''''
```

> [!warning]
> 
'''))

w('concepts/.md', mk('concept', ['',''], '', '''## 

{SRC}#7.1. 

|  |  |  |
| --- | --- | --- |
| + |  | 9 + 7  16 |
| - |  | 7 - 2  5 |
| * |  | 3 * 4  12 |
| / |  | 9 / 3  3.0 |
| // |  | 9 // 6  1 |
| % |  | 9 % 6  3 |
| ** |  | 2 ** 3  8 |

## 

|  |  |  |
| --- | --- | --- |
| += | age += 1 | age = age + 1 |
| -= | age -= 1 | age = age - 1 |
| *= | price *= discount | price = price * discount |
| /= | pay /= 5 | pay = pay / 5 |
| //= | apple //= num | apple = apple // num |
| %= | seconds %= minutes | seconds = seconds % minutes |
| **= | a **= b | a = a ** b |

## 

|  |  |  |
| --- | --- | --- |
| == |  | a == b |
| != |  | a != b |
| > |  | a > b |
| < |  | a < b |
| >= |  | a >= b |
| <= |  | a <= b |

> [!NOTE]
>  Unicode 

## 

TrueFalse{SRC}#7.4. 

```python
is_student = True
is_adult = False
result = 5 > 3  # True
```

> [!NOTE]
>  0 '' False True

## 

|  |  |  |
| --- | --- | --- |
| and |  | a and b |
| or |  | a or b |
| not |  | not a |
'''))

w('concepts/.md', mk('concept', ['if',''], '', '''## 

{SRC}#1. 

## 

```python
age = 20
if age >= 18:
    print('')
```

## 

```python
age = 15
if age >= 18:
    print('')
else:
    print('')
```

## 

```python
score = 85
if score >= 90:
    print('')
elif score >= 80:
    print('')
elif score >= 60:
    print('')
else:
    print('')
```

## 

```python
age = 25
gender = ''
if age >= 18:
    if gender == '':
        print('')
    else:
        print('')
else:
    print('')
```

> [!NOTE]
> Python  switch/case  if/elif/else 
'''))

w('concepts/.md', mk('concept', ['while','for'], '', '''## while 

{SRC}#2.1. while 

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## for 

{SRC}#2.2. for 

```python
# 
for i in range(5):
    print(i)

# 
for char in 'hello':
    print(char)
```

> [!NOTE]
> for 

## continue  break

- continue
- break

```python
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
```

## 

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}x{i}={i*j}', end='\\t')
    print()
```
'''))

w('concepts/.md', mk('concept', ['def',''], '', '''## 

 def {SRC}#1.1. 

```python
def greet(name):
    print(f'{name}')
```

## 

1. Python  print()len()type() 
2. {SRC}#1.2. Python 

## 

```python
def (1, 2):
    """"""
    # 
    return 
```

## 

```python
greet('')  # 
```

## 

- 
- =
- 
-  *args **kwargs {SRC}#3. 

## 

 return {SRC}#4. 

```python
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

> [!NOTE]
>  return  None

## 

{SRC}#6. 

```python
def greet(name):
    print(f'{name}')

def welcome(name, msg):
    print('---')
    greet(name)
    print(msg)
    print('---')

welcome('', ' Python ')
```

## 

{SRC}#7. 

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

> [!warning]
> 

## 

{SRC}#8. 

```python
def add(a, b):
    """
    
    :param a: 
    :param b: 
    :return: 
    """
    return a + b
```
'''))

w('concepts/.md', mk('concept', ['str',''], '', '''## 

{SRC}#4. 

```python
s1 = ''
s2 = ""
s3 = ''''''
s4 = """"""
```

## 

- 
- 
- 

## 

|  |  |  |
| --- | --- | --- |
| upper() |  | 'abc'.upper()  'ABC' |
| lower() |  | 'ABC'.lower()  'abc' |
| strip() |  | ' abc '.strip()  'abc' |
| split() |  | 'a,b,c'.split(',')  ['a','b','c'] |
| join() |  | '-'.join(['a','b'])  'a-b' |
| replace() |  | 'hello'.replace('l','L')  'heLLo' |
| find() |  | 'hello'.find('ll')  2 |
| startswith() |  | 'hello'.startswith('he')  True |
| endswith() |  | 'hello'.endswith('lo')  True |
| isdigit() |  | '123'.isdigit()  True |

## 

|  |  |  |
| --- | --- | --- |
| len() |  | len('hello')  5 |
| max() |  | max('abc')  'c' |
| min() |  | min('abc')  'a' |
| sorted() |  | sorted('cba')  ['a','b','c'] |
| reversed() |  | list(reversed('abc'))  ['c','b','a'] |

## 

```python
for char in 'hello':
    print(char)
```

## 

|  |  |
| --- | --- |
| \' |  |
| \" |  |
| \\ |  |
| \\n |  |
| \\t |  |
| \\r |  |

## 

```python
# f-string
name = ''
age = 18
print(f'{name}{age}')

# 
print('%s%d' % (name, age))
```
'''))

w('concepts/.md', mk('concept', ['list'], '', '''## 

 Python  [] {SRC}#2. 

```python
names = ['', '', '']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]
empty = []
```

## 

 0  -1 {SRC}#2.3. 

```python
nums = [10, 20, 30, 40]
print(nums[0])   # 10
print(nums[-1])  # 40
```

## 

|  |  |  |
| --- | --- | --- |
|  | append() | lst.append(5) |
|  | insert(, ) | lst.insert(0, 1) |
|  | extend() | lst.extend([6,7]) |
|  | remove() | lst.remove(3) |
|  | pop() | lst.pop(0) |
|  | del lst[] | del lst[1] |
|  | lst[] =  | lst[0] = 99 |
|  |  in lst | 3 in lst  True |
|  | lst.index() | lst.index(3)  1 |

## 

|  |  |
| --- | --- |
| append() |  |
| insert() |  |
| remove() |  |
| pop() |  |
| clear() |  |
| count() |  |
| index() |  |
| sort() |  |
| reverse() |  |
| copy() |  |

## 

|  |  |  |
| --- | --- | --- |
| len() |  | len([1,2,3])  3 |
| max() |  | max([1,3,2])  3 |
| min() |  | min([1,3,2])  1 |
| sum() |  | sum([1,2,3])  6 |
| sorted() |  | sorted([3,1,2])  [1,2,3] |
| reversed() |  | list(reversed([1,2,3]))  [3,2,1] |

## 

```python
nums = [10, 20, 30, 40]
for num in nums:
    print(num)

# 
for i, num in enumerate(nums):
    print(i, num)
```

## 

- 
- 
- 
'''))

w('concepts/.md', mk('concept', ['tuple'], '', '''## 

 Python  () {SRC}#3. 

```python
coordinates = (10, 20)
names = ('', '', '')
single = (1,)  # 
empty = ()
```

## 

```python
# 
tup = (10, 20, 30)

# 
tup2 = 10, 20, 30
```

## 

```python
tup = (10, 20, 30)
print(tup[0])   # 10
print(tup[-1])  # 30
```

## 

```python
tup = (10, 20, 30)
# tup[0] = 99  # TypeError: 'tuple' object does not support item assignment
```

## 

|  |  |
| --- | --- |
| count() |  |
| index() |  |

## 

|  |  |
| --- | --- |
| len() |  |
| max() |  |
| min() |  |
| sum() |  |
| sorted() |  |
| reversed() |  |

## 

```python
def show_info(name, age):
    print(f'{name}, {age}')

# 
info = ('', 18)
show_info(*info)  # , 18

# 
data = {'name': '', 'age': 20}
show_info(**data)  # , 20
```

## 

- 
- 
- 
'''))

w('concepts/.md', mk('concept', ['dict'], '', '''## 

 Python  {} key-value{SRC}#8. 

```python
student = {'name': '', 'age': 18, 'score': 90}
empty = {}
```

## 

```python
# 
person = {'name': '', 'age': 20}

#  dict() 
person2 = dict(name='', age=25)

# 
empty_dict = dict()
```

## 

|  |  |  |
| --- | --- | --- |
| / | d[key] = value | d['age'] = 19 |
|  | del d[key] | del d['age'] |
|  | d.pop(key) | d.pop('age') |
|  | d.popitem() |  |
|  | d[key] | d['name']  '' |
|  | d.get(key) | d.get('age', 0) |
|  | key in d | 'name' in d  True |

## 

|  |  |
| --- | --- |
| keys() |  |
| values() |  |
| items() |  |
| get(key, default) |  |
| update() |  |
| setdefault() |  |
| clear() |  |

## 

```python
person = {'name': '', 'age': 18}

# 
for key in person:
    print(key)

# 
for key, value in person.items():
    print(f'{key}: {value}')
```

## 

- Python 3.7+ 
- 
- 
- 
'''))

w('concepts/.md', mk('concept', ['set'], '', '''## 

 Python  {}  set() {SRC}#7. 

```python
fruits = {'', '', ''}
empty = set()
```

## 

```python
# {} 
nums = {1, 2, 3, 3, 2}  # {1, 2, 3} 

#  set() 
letters = set('hello')  # {'h', 'e', 'l', 'o'}
```

## 

|  |  |  |
| --- | --- | --- |
|  | add() |  |
|  | update() |  |
|  | remove() |  |
|  | discard() |  |
|  | pop() |  |
|  | clear() |  |
|  | x in s |  |

## 

|  |  |  |  |
| --- | --- | --- | --- |
|  | s1 & s2 / intersection() | & |  |
|  | s1 | s2 / union() | | |  |
|  | s1 - s2 / difference() | - |  s1  s2  |
|  | s1 ^ s2 / symmetric_difference() | ^ |  |

## 

```python
fruits = {'', '', ''}
for fruit in fruits:
    print(fruit)
```

## 

- 
- 
- 
'''))

w('concepts/.md', mk('concept', [''], '', '''## 

slicing{SRC}#5. 

## 

```python
[::]
```

-  0
- 
-  1

## 

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]     # [2, 3, 4]         24
nums[:5]      # [0, 1, 2, 3, 4]   5
nums[5:]      # [5, 6, 7, 8, 9]   5
nums[:]       # [0,1,...,9]       
nums[::2]     # [0, 2, 4, 6, 8]   2
nums[::-1]    # [9,8,...,0]       
nums[-3:]     # [7, 8, 9]         3
nums[:-3]     # [0,...,6]         3
```

## 

- 
- 
- 
'''))

w('concepts/.md', mk('concept', [''], '', '''## 

{SRC}#6. 

## 

1. 
2. 
3. 

## 

|  |  |  |
| --- | --- | --- |
| int(x) |  | int('123')  123 |
| float(x) |  | float('3.14')  3.14 |
| str(x) |  | str(123)  '123' |
| bool(x) |  | bool(0)  False |
| list(x) |  | list('abc')  ['a','b','c'] |
| tuple(x) |  | tuple([1,2])  (1,2) |
| set(x) |  | set('aab')  {'a','b'} |

> [!NOTE]
>  int('abc') 
'''))

w('concepts/.md', mk('concept', [''], '', '''## 

{SRC}#3. 

## 

1. 
2. 

> [!tip]
> 

## 

 Python  # {SRC}#3.3. 

```python
# name 
name = ''
# age 
age = 18
```

> [!NOTE]
> Python  #  # 

## 

Python {SRC}#3.4. 

```python
"""


"""
```

> [!tip]
> Python 

## 

 Python {SRC}#3.5. 

```python
# coding=utf-8
print('')
```

> [!tip]
>  Python3  Python3  UTF-8 
'''))

w('concepts/.md', mk('concept', ['','UTF-8'], '', '''## 

{SRC}#4. 

> [!tip]
> 

## 

|  |  |  |
| --- | --- | --- |
| ASCII |  | 128 |
| ISO 8859-1 |  ASCII  | 256 |
| GB2312 |  6763  | ~6763 |
| GBK |  GB2312 | ~20000+ |
| UTF-8 |  ASCII |  |

> [!success]
>  UTF-8 

> [!tip]
>  Python3  Python3  UTF-8 

## 

```python
#   
text = ''
encoded = text.encode('utf-8')

#   
decoded = encoded.decode('utf-8')
```
'''))

w('concepts/.md', mk('concept', ['input'], '', '''## 

Python  input() {SRC}#9. 

```python
name = input('')
print('' + name)
```

> [!NOTE]
> input() 

```python
age = int(input(''))  # 
score = float(input(''))  # 
```
'''))

w('concepts/.md', mk('concept', [''], '', '''## 

{SRC}#1. 

```python
''    # 
18        # 
65.2      # 
True      # 
None      # 
```

> [!warning]
> 
'''))

w('concepts/.md', mk('concept', ['','import'], '', '''## 

 Python  .py {SRC}#1. 

## 

1. Python  ossysmath 
2.  requestspandas 
3. {SRC}#1.2. 

## 

```python
# my_module.py
def say_hello(name):
    return f'{name}'

PI = 3.14159
```

## 

```python
# 
import my_module
my_module.say_hello('')

# 
from my_module import say_hello
say_hello('')

# 
import my_module as mm
mm.say_hello('')
```

## __name__ 

```python
# my_module.py
print(__name__)  #  '__main__'
```

> [!NOTE]
> 
> ```python
> if __name__ == '__main__':
>     # 
> ```
'''))

w('concepts/.md', mk('concept', ['','package'], '', '''## 

 __init__.py {SRC}#2. 

## 

```
mypackage/
 __init__.py
 module1.py
 module2.py
 subpackage/
     __init__.py
     module3.py
```

## 

1. Python 
2.  pip 
3. {SRC}#2.3. 

## 

```python
# 
import mypackage.module1

# 
from mypackage import module1

# 
from mypackage.subpackage import module3
```

## 

```
/
 __init__.py
 package_a/
    __init__.py
    module_a.py
 package_b/
     __init__.py
     module_b.py
```
'''))

w('concepts/.md', mk('concept', ['','try'], '', '''## 

- 
- {SRC}#1. 

## 

```python
try:
    # 
    result = 10 / 0
except ZeroDivisionError:
    # 
    print('')
except Exception as e:
    # 
    print(f'{e}')
else:
    # 
    print('')
finally:
    # 
    print('')
```

## 

```python
try:
    pass
except (ErrorType1, ErrorType2) as e:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass
```

> [!NOTE]
>  except 

## 

```python
raise ValueError('')
```

## 

{SRC}#4. 

## 

```python
class MyError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

raise MyError('')
```
'''))

w('concepts/.md', mk('concept', ['','iterator'], '', '''## iterable

 for {SRC}#11.  vs   1iterable

range 

```python
from collections.abc import Iterable
isinstance('hello', Iterable)  # True
isinstance(123, Iterable)      # False
```

## iterator

{SRC}#11.  vs   2iterator

1. 
2. 
3. 

```python
from collections.abc import Iterator
isinstance(iter('hello'), Iterator)  # True
isinstance('hello', Iterator)        # False
```

## 

```python
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration
```

## 

1. 
2. 
3. {SRC}#11.  vs   4
'''))

w('concepts/.md', mk('concept', ['','open'], '', '''## 

1.  .txt.py 
2. {SRC}#12.   1. 

##  vs 

-  C:\\Users\\test.py
-  test.py.\\data\\test.py{SRC}#12.   2.  vs 

## Python 

1. f = open('file.txt', 'r')
2. 
3. f.close(){SRC}#12.   3. Python 

## 

```python
# read() 
f = open('test.txt', 'r', encoding='utf-8')
content = f.read()
f.close()

# readline() 
line = f.readline()

# readlines() 
lines = f.readlines()

# for 
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
```

## 

```python
# w 
f = open('test.txt', 'w', encoding='utf-8')
f.write('Hello, World!')
f.close()

# x 
f = open('test.txt', 'x', encoding='utf-8')

# a 
f = open('test.txt', 'a', encoding='utf-8')
f.write('\\nNew line')
f.close()
```

##  with

 with {SRC}#12.   5.  with

```python
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 
```

## 

|  |  |
| --- | --- |
| rt |  |
| wt |  |
| xt |  |
| at |  |
| rb |  |
| wb |  |
| rt+ |  |
| wt+ |  |

## flush 

```python
f = open('test.txt', 'w')
f.write('Hello')
f.flush()  # 
```

## 

```python
import os
os.mkdir('new_dir')           # 
os.listdir('.')               # 
os.rename('old', 'new')       # 
os.remove('file.txt')         # 
```
'''))

# 
# COMPARISONS
# 

w('comparisons/-vs-.md', mk('comparison', ['',''], ' vs ', '''## 

********{SRC}#4. 

## 

**** Windows  .exe {SRC}#4.1. 

- 
- 

## 

****{SRC}#4.2. 

- 
- 

## 

|  |  |  |
| --- | --- | --- |
| **** | CC++GoRust  | PythonJavaScriptRuby  |
| **** |  |  |
| **** |  |  |
| **** |  |  |
| **** |  |  |
| **** |  | AI Web |
'''))

w('comparisons/while--vs-for-.md', mk('comparison', ['while','for'], 'while  vs for ', '''## 

Python while  for {SRC}#2. 

## while 

****{SRC}#2.1. while 

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

## for 

****{SRC}#2.2. for 

```python
for i in range(10):
    print(i)

for char in 'hello':
    print(char)
```

##  while  for

| | **while ** | **for ** |
| --- | --- | --- |
| **** |  |  |
| **** | `while :` | `for  in :` |
| **** |  |  |
| **** |  |  |
| **** |  | range |
'''))

w('comparisons/-vs-.md', mk('comparison', ['','copy'], ' vs ', '''## 

 b = a  b  a  b a {SRC}#10.  vs 

```python
nums1 = [10, 20, 30, 40]
nums2 = nums1
nums2[3] = 99
print(nums1[3])  # 99
```

## 

{SRC}#10.3. 

```python
import copy
nums1 = [10, 20, 30, 40]
nums2 = copy.copy(nums1)
nums2[3] = 99
print(nums1[3])  # 40
```

****

```python
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.copy(nums1)
nums2[3][0] = 99
print(nums1[3][0])  # 99
```

## 

****{SRC}#10.4. 

```python
import copy
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.deepcopy(nums1)
nums2[3][0] = 99
print(nums1[3][0])  # 40
```

## 

| | **** | **** | **** |
| --- | --- | --- | --- |
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |
'''))

w('comparisons/-vs-.md', mk('comparison', ['tuple','list'], ' vs ', '''## 

 Python ********{SRC}#3.10.  VS 

## 

|  | **** | **** |
| --- | --- | --- |
| **** | [] | () |
| **** |  |  |
| **** |  |  |
| **** |  |  |
| **** |  |  |
| **** |  |  |

## 

```python
nums = [10, 20, 30]
nums.append(40)  # OK
nums[0] = 99     # OK
```

## 

```python
coords = (10, 20, 30)
# coords.append(40)  # TypeError
# coords[0] = 99     # TypeError
```
'''))

w('comparisons/-vs-.md', mk('comparison', ['',''], ' vs ', '''## 

###  vs 

- ****CPU {SRC}#13.   1 vs 
- **** CPU  CPU

###  vs 

- ****{SRC}#13.   3 vs 
- ****

## 

|  | **** | **** |
| --- | --- | --- |
| **** |  |  |
| **** | QueuePipe  |  |
| **** |  |  |
| **GIL ** |  |  GIL  |
| **** |  |  |
| **** | CPU  | I/O  |

## GIL

CPython  Python {SRC}#13.   15. GIL 

> [!warning]
> GIL  CPU  I/O 

## 

- **CPU **
- **I/O **
- ****
- ****
'''))

w('comparisons/-vs-.md', mk('comparison', ['',''], ' vs ', '''## 

{SRC}#12.   2.  vs 

## 

{SRC}#12.   1

```python
# Windows
path = r'C:\\Users\\test.py'
# Linux/Mac
path = '/home/user/test.py'
```

## 

{SRC}#12.   2

```python
# 
path = 'test.py'
# 
path = '../config.ini'
# 
path = 'data/result.txt'
```

## 

| | **** | **** |
| --- | --- | --- |
| **** | / |  |
| **** |  |  |
| **** |  |  |
| **** |  |  |
'''))

# 
# ENTITIES
# 

w('entities/Python.md', mk('entity', ['',''], 'Python', '''## 

Python  Guido van Rossum  1989 1991 {SRC}#2.  Python  1.1. Python 

## 

Python  Guido van Rossum  CFortran  Shell Monty Python's Flying Circus Python{SRC}#2.  Python  1.1. Python 

> [!NOTE]
> Python 

## 

****
- 
- 
- 
- 
-  + 

****
- 
- 
- GIL

##  AI  Python

1. 
2. TensorFlowPyTorch 
3. 
4. 
5.  + {SRC}#2.  Python  1.3.  AI  Python 

## 

- 1991 Python 0.9.0 
- 1994 Python 1.0 
- 2000 Python 2.0 
- 2008 Python 3.0  Python 2 
- 2020 Python 2 
- 2024 Python 3.13 
'''))

w('entities/PyCharm.md', mk('entity', ['IDE',''], 'PyCharm', '''## 

PyCharm  JetBrains  Python IDE{SRC}#2.  Python  2.3.  PyCharm

> [!NOTE]
> PyCharm https://www.jetbrains.com/pycharm/download

## 

PyCharm  +  30 {SRC}#2.  Python  2.3.  PyCharm

## 

|  |  |
| --- | --- |
| Ctrl + / |  |
| Ctrl + Alt + L |  |
| Ctrl + C |  /  |
| Ctrl + D |  /  |
| Ctrl + Z |  |
| Ctrl + Y |  / () |
| Ctrl + X |  /  |
| Shift + Enter |  |
'''))

w('entities/Guido-van-Rossum.md', mk('entity', ['','Python'], 'Guido van Rossum', '''## 

Guido van Rossum  Python {SRC}#2.  Python  1.1. Python 

## 

- 
-  CFortran  Shell 
- 1989  Python 
- Monty Python's Flying Circus Python

## Python 

{SRC}#2.  Python  1.1. Python 

> [!NOTE]
> Python  1991 
'''))

# 
# PRACTICE
# 

w('practice/-Python-.md', mk('practice', ['','Python'], ' Python ', '''## 

 Windows  Python  PyCharm IDE

##  Python {SRC}#2.  Python  2.1.  Python 

1.  https://www.python.org/downloads/ Downloads
2.  Python 3.13+
3. 
4.  Next
5.  Install 
6. **** Disable path length limit 
7.  Win + R cmd `python --version`

##  PyCharm{SRC}#2.  Python  2.3.  PyCharm

1.  https://www.jetbrains.com/pycharm/download/
2. 
3. 
4. 
5. 
6. 

## {SRC}#2.  Python  2.4.  PyCharm

1.  PyCharm
2.  Python 
3. 

##  Python 

{SRC}#2.  Python  3.  Python 

### 
```
python        # 
print(100)
exit()        # 
```

### 
```bash
python test.py
```

### IDE 
 PyCharm   Run
'''))

w('practice/-.md', mk('practice', ['',''], '', '''## 

 Python 

## {SRC}#10.   1.3. 

 Python  mymath.py
```python
# mymath.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

if __name__ == '__main__':
    print(add(1, 2))
```

## {SRC}#10.   1.4. 

```python
# 1
import mymath
print(mymath.add(3, 5))

# 2
from mymath import add
print(add(3, 5))

# 3
import mymath as m
print(m.subtract(10, 3))

# 4
from mymath import *
```

## {SRC}#10.   2.4. 

```
myproject/
 __init__.py
 math_ops/
    __init__.py
    operations.py
 string_ops/
     __init__.py
     operations.py
```

## {SRC}#10.   2.5. 

```python
# 
import myproject.math_ops.operations as ops
print(ops.add(1, 2))

# 
from myproject import math_ops
```

## 

1.  __init__.py Python 3.3+ 
2. Windows  multiprocessing  if __name__ == '__main__' 
3. 
'''))

# 
# SUMMARY
# 
counts = {
    'concepts': len(os.listdir(os.path.join(BASE, 'concepts'))),
    'comparisons': len(os.listdir(os.path.join(BASE, 'comparisons'))),
    'entities': len(os.listdir(os.path.join(BASE, 'entities'))),
    'practice': len(os.listdir(os.path.join(BASE, 'practice'))),
}
print(f'All pages generated successfully.')
print(f'Concepts: {counts["concepts"]}, Comparisons: {counts["comparisons"]}, '
      f'Entities: {counts["entities"]}, Practices: {counts["practice"]}')
