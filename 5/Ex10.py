
prices = [50, 75, 46, 22, 80, 65, 8]
times = [1, 2, 3, 4, 5, 6]
bigger = 0
smaller = 0
for price in prices:
    for time in times:
        num1 = price
        if bigger < num1 > prices[time]:
            bigger = num1
        elif smaller > num1 < prices[time]:
            smaller = num1
print(bigger, smaller)









