count = 0
total = 0
average = 0
while True:
    line = input("Enter a Number: ")
    if line == 'done':
        break
    try:
        numbers = int(line)
    except ValueError:
        print("Enter a number Please")
    else:
        count = count + 1
        total = total + numbers
        average = total / count
print(total, count, average)