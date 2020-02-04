#Positive Slicing
print("Positive Slicing")
cities = ["Faisalabad", "Lahore", "Islamabad", "Peshawar", "Quetta", "Sahiwal", "Rawalpindi", "Sialkot"]
i=1
#Output1
start=cities.index("Faisalabad")
end=cities.index("Peshawar")
print(cities[start:end+i])
#Output2
start=cities.index("Islamabad")
end=cities.index("Sahiwal")
print(cities[start:end+i])
#Output3
start=cities.index("Sahiwal")
print(cities[start:])

#Negative Slicing
print("\nNegative Slicing")
#Output1
print(cities[-4:-2+i])
#Output2
print(cities[-5:])