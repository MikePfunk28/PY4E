# Find min and max of numbers user enters
numbers = []

while True:
    # Try input if use enters done break, 
    
    line = input("Enter a number ")
    if line == "done":
        break
    try:
        num = int(line)
    except ValueError:
        print("Invalid number")
    else:
        numbers.append(num)
        

print(type(numbers))
print(num)
print(numbers)
print(min(numbers))
print(max(numbers))