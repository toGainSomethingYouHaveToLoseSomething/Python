#functons: input();int();float();str();bool();eval()

a = input("Enter a number: ") #input() returns string
print(a,type(a)) # <class 'str'>

b = int(input("Enter a number: "))
print(b,type(b)) # <class 'int'>

c = eval(input("Enter a number: ")) #eval() returns the data type of the input
print(c,type(c)) # <class 'int'> or <class 'float'> or <class 'complex'> depending on the input
