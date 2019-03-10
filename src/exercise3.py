
total = 0
count = 0
numbers = list()

while True:
    number = input ('Enter a number: ')

    if number == 'done' :
        break

    try:
        number = int(number)
        numbers.append(number)
    except:
        print ('Invalid input, try again')

for number in numbers:
    count += 1
    total += number

average = total / count

print (total, count, average)
