def computepay(h, r):
    if h > 40:
        pay = ((h - (h - 40)) * r) + ((r * 1.5) * (h - 40))
        return pay
    else:
        pay = h * r
        return pay


# Asks User for input
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

pay = computepay(hrs, rate)

print("Pay", computepay(hrs, rate))
print("Pay", pay)