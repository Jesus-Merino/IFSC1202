#N students take K apples from a basket and distribute them among each other evenly. 
#The remaining (the undivisible) apples remains in the basket.
#Prompt for the number of students and apples.
#How many apples will each single student get?
#How many apples will remain in the basket?
N = int(input("Number of Students: "))
K = int(input("Number of Apples: "))
print(K//N)
print(K%N)
