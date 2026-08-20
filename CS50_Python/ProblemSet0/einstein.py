#make a program that prompts for mass as an intefer in kilos, and outputs the number of joules as an integer
#assume that they will input an integer

#E = mc^2

c = 300000000
mass = int(input("Input the mass of an item in kilograms: "))
energy = mass * c ** 2
print("E =", energy)