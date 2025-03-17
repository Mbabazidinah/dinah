#print("Hello, word")
#name = input("enter any name:")
# print(len(name))
# names = input("enter any names you want:").replace(" ","")
# print(len(names))
# a = input("enter the first name A:")
# b = input("enter the second name B:")
# c = input("enter the third name C:")
# d = input("enter the forth name D:")
# e = input("enter the fifth name E:")
# a = a.replace(" ","")
# b = b.replace(" ","")
# c = c.replace(" ","")
# d = d.replace(" ","")
# e = e.replace(" ","")
# print("lengthof A=", len(a),"lengthof B=", len(b),"lengthof C=", len(c),"lengthof D=", len(d),"lengthof E=", len(e))
arr1 = ['a', 'i', 'o', 'e', 'u']
arr2 = ['k', 'j', 'p', 't', 'f']

# Function to replace characters based on arr1 and arr2
def kajipo(text):
    result = []
    for char in text:
        if char in arr1:
            index = arr1.index(char)
            result.append(arr2[index])
        elif char in arr2:
            index = arr2.index(char)
            result.append(arr1[index])
        else:
            result.append(char)
    return ''.join(result)

# Get user input
user_input = input("Enter text: ")

# Replace characters in the user input
result = kajipo(user_input)

print("Updated text:", result)