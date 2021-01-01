print('''
1.Celsius to Fahrenheit
2.Celsius to Kelvin
3.Fahrenheit to Celsius
4.Fahrenheit to Kelvin
5.Kelvin to Celsius
6.Kelvin to Fahrenheit
''')

temp = int(input("Enter your choice: "))

if temp == 1:
    c = float(input("Enter centigrade: "))
    f = (c * 1.8) + 32
    print(f, "*F")

elif temp == 2:
    c = float(input("Enter centigrade: "))
    k = c + 273.15
    print(k, " K")

elif temp == 3:
	f = float(input("Enter fahrenheit: "))
	c = (f - 32) / 1.8
	print(c, "*C")    

elif temp == 4:
    f = float(input("Enter fahrenheit: "))
    c = (f - 32) / 1.8
    k = c + 273.15
    print(k, " K")

elif temp == 5:
    k = float(input("Enter kelvin: "))
    c = k - 273.15
    print(c, "*C")    

elif temp == 6:
    k = float(input("Enter kelvin: "))
    c = k - 273.15
    f = (c * 1.8) + 32
    print(c, "*F")    

else:
    print("Invalid option entered")
