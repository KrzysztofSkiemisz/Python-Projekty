# Even or odd number

x = None

while not(x):
    x = int(input('Enter an int number for x: '))

if x%2== 0:
    print('Entered number is even!')
    print('Your number was: ' + ' ' + str(x))
else:
    print('Entered number is odd!')
    print('Your number was: ' + ' ' + str(x))