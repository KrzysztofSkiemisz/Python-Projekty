# WHILE LOOP

#while 1==1:
#    print('Holy cow! I am stuck in loop!')

name = ''

while len(name) == 0:
    name = input('Enter your name: ')

print('Hello ' + name + '!')

x = None
y = None
summary = None

while not(x and y):
    x = int(input('Enter an int number for x: '))
    y = int(input('Enter and int number for y: '))
    summary = x + y

print('Summary of your number is: ' + str(summary))