while true:
    number = input ('Enter a number: ')
    if number == 'done' :
        break

    try:
        number = int(number)
        count = count + 1
        total = total + number
    except:
        print ('Invalid input, try again')

    average = total + number
    print (total, count, average)
    
