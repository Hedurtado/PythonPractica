adc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
       't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(len(adc), 1, -1):
    if x % 3 == 0:
        adc.pop(x - 1)

print(adc)
