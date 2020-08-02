if "mot" in "monkey":
    print("yes its there")
else:
    print("no, not there")
  
print("\n")
print("-----------------------------------------------------")

colors = ["red", "orange", "green", "purple", "black", "pink"]
for color in colors:
    print("Is " + color + " your favroutie color?")
 
print("\n")
print("-----------------------------------------------------")

for num in [1,2,3,4,5,6]:
    double = num * 2
    print("Twice " + str(num) + " is " + str(double))

print("\n")
print("-----------------------------------------------------")


colors = ["red", "orange", "green", "purple", "black", "pink"]
modifiers = ["dark", "light", "brownish"]
for c in colors:
    for m in modifiers:
        print(c + " " + m)
        
print("\n")
print("-----------------------------------------------------")

count = 10
while count >= 0:
    print(str(count))
    count -= 1

