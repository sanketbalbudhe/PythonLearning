
'''
#Task 1: Read a File and Handle Errors
try:
    file = open("file.txt","r")

    lines = file.readlines()

    i = 1
    for line in lines:
        print("Line ", i, ":", line)
        i += 1

    file.close()
except FileNotFoundError :
    print("Error: The file 'file.txt' was not exist.")
'''

#Task 2: Write and Append Data to a File

a = input("Enter text to write to the file:")
file = open("output.txt","w")
a+='\n'
file.write(a)
file.close()
print("Data Successfully written to output.txt")

a = input("Enter additional text to append:")
file = open("output.txt","a")
file.write(a)
file.close()
print("Data Successfully appended")


file = open("output.txt","r")
lines = file.read()
print ("File content of output.txt:",lines)
file.close()