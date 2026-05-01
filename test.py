words = ["hello","world","python"]
upper = [word.upper() for word in words ]
print(upper)
#2
numbers = [10,20,30,40,50]
multiply = [number *2 for number in numbers]
print(multiply)
#3
names = ["ali","sara","jhon"]
damn = [name + "!" for name in names]
print(damn)
#4
numbers = [1,2,3,4,5,6,7,8,9,10]
num = [ num for num in numbers if num % 2 == 0 ]
print(num)
#5
numbers = [5,10,15,20,25,30]
grater = [n for n in numbers if n > 15]
print(grater)
#6
names = ["ali","sara","jhon","bob","elizebeth"]
more = [ n for n in names if len(n)>3 ]
print(more)
#7
ages = [12,18,15,21,17,25,16]
adult = [a for a in ages if a >=18]
print(adult)
# 8 
numbers = [1,2,3,4,5,6,7,8,9,10]
eve = [eve * 2  for eve in numbers if eve % 2 == 0 ]
print(eve)
#9
numbers = [1,2,3,4,5,6,7,8,9,10]
num = [ n * 3 for n in numbers if n % 2 != 0 ]
print(num)
#10
prices = [100,200,300,400,500]
price = [p *0.9  for p in prices if p > 200]
print(price)
#11
names = ["ali","sara","jhon","bob","alizebeth"]
name = [n.upper() for n in names if len(n)>3]
print(name)
#12
words = ["cat","elephant","dog","butterfly","ant"]
word = [w.title() for w in words if len(w) > 3 ]
print(word)
#13
ages = [10,13,15,18,21,25,12,17]
age = [a * 2 for a in ages if a < 18]
print(age)
#14
numbers = [1,2,3,4,5,6,7,8,9,10]
num = [n + 100 for n in numbers if  n % 2 == 0 ]
print(num)
#15
numbers = [5,10,15,20,25]
num = [n *5 for n in numbers if n > 10 ]
print(num)