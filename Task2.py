List = [1,2,3,4,5,6,7,8,9,10]

A = List[:5]

B = List[:5]
B.reverse()

print("Original list:",List)
print("Extracted first five elements:",A)
print("Reversed extracted elements:",B)