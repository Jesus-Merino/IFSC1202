def hms_to_sec(hms_str):
    h, m, s = hms_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

print("First Timestamp")
h1 = int(input("Enter Hours: "))
m1 = int(input("Enter Minutes: "))
s1 = int(input("Enter Seconds: "))

hms_str1 = str(h1) + ":" + str(m1) + ":" + str(s1)
hms1 = hms_to_sec(hms_str1)

print("Second Timestamp")
h2 = int(input("Enter Hours: "))
m2 = int(input("Enter Minutes: "))
s2 = int(input("Enter Seconds: "))

hms_str2 = str(h2) + ":" + str(m2) + ":" + str(s2)
hms2 = hms_to_sec(hms_str2)

print(hms2 - hms1)
