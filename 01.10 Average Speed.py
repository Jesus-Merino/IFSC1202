Length = int(input("Enter Length of Race in Kilometers: "))
Minutes = int(input("Enter Minutes: "))
Seconds = int(input("Enter Seconds: "))
print((Length/((Minutes*60+Seconds)/3600))/1.61)