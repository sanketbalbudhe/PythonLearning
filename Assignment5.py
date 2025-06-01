
'''

#Task 1: Create a Dictionary of Student Marks

dic={'Alice':85,'Sanket':15}

a = input("Enter the student's name: ")

if a in dic:
    print("{}'s marks:{}".format(a,dic[a]))
else:
    print("Student not found")

'''

#Task 2: Demonstrate List Slicing

lst = list(range(1,11))

print("Original list:",lst)

HalfList = list(lst[0:5])
print("Extractyed first five element:",HalfList)
HalfList.reverse()
print("Reversed extractyed element: ",HalfList)
