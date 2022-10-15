## Lecture #1 [Link](https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0)
### about programming
* ~~PL Syntax~~
* ~~Libraries~~
* Algorithms & Data structures
* Programming  art/craft (Programmer - writer)
* Programming practice (skills)
* Solution design (architecture)
* Work in groups (ability to collaborate and work with people)
### python 3 syntax
```python
print("Hello World!")
x = "Hello World!"
print (x)
print(type(x))
x = 1 + 2 + 3 + 4
```
python constantly frees the memory 
if we want to store something in memory 
we have to place a link to value in memory.
**=** in Python is a **link** . 
```python
# python will create temporary objects.
# then calculates value which will be stored in memory as object.
# once object got calculated x is linked to new object and previous object (x) will be removed.
x = 1 + 2 + 3 + 4 
```
variables values exchange through additional variables
```python
a = 2
b = 5
tmp = a
a = b
b = tmp
```
variables values exchange using tuples
```python
a = 2
b = 5
tmp1, tmp2 = b, a # schematically this work through a temp tuple
a, b = tmp1, tmp2
a,b = b,a # factually this is done through a temp tuple
```
### arithmetic operations
in python operations performed from left to right
unary operations have priority over binary
```python
a = b = c = ...
a^b^c == a**b**c
-a     # unary minus
a * b  # binary multiplication 
a / b  # binary division
a // b # binary integer division
a % b  # binary mod (division remainder) 
a/b*c == (a / b) * c # left to right
a - b  # has the smallest priority
a + b  # has the smallest priority
# !!! IMPORTANT
-12 // 10 == -2 
-12 % 10 == 8
# this is correct from mathematical point of view!
# but many processors including intel cals it differently.
# remainder should always belong to [0,n).
```

### main statements
there is only 1 loop in python - "while".
"for" is a syntax sugar
iteration - single run of a loop body

"while" operator
```python
# some code before
while ...:
    ...
    if ...:
        break # quit the while loop
    ...
    continue # go to next cycle iteration
else:
    ...
    # instructions after all iterations 
# do something after
# while can be nested
y = ...
y -= ... # syntax sugar for y = y + ...
y *= ...
y /= ...
y //= ...
y %= ...
```
"if" operator
```python
if ...:
    ...
else:
    ...
```
"for" operator
```python
for x in 1, 5, 2, 4, 3: 
    print(x ** 2)
for i in range(1, 10, 1):
    print(x ** 2)
```
