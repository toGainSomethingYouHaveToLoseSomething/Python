#Data type list

#Number 
  # Integer
  # Float
  # Complex
a = 5; print(type(a)) # <class 'int'>
b = 5.0; print(type(b)) # <class 'float'>
c = 5+3j; print(type(c)) # <class 'complex'>



#Sequence
  # String
s = "This is a string"
print(s,type(s)) # <class 'str'>
s = '''This is a multi-line string'''
print(s,type(s)) # <class 'str'>

  # List
a = [1,2.2,'smith',3+4j]
print(a,type(a)) # <class 'list'>
a[0] = 10 #mutable
print(a,type(a)) # <class 'list'>


  # Tuple
t = (1,2.2,'smith',3+4j)
print(t,type(t)) # <class 'tuple'>
# t[0] = 10 #immutable

# Dictionary
d = {
      'name':'smith',
      'age':30
    }
print(d,type(d)) # <class 'dict'>
print(d['name']) # smith

# Set
set1 = {1,2,3,4,5}
print(set1,type(set1)) # <class 'set'>
# print(set1[0]) # TypeError: 'set' object is not subscriptable

#Mutable data types: List, Dictionary, Set, bytearray
#Immutable data types: Integer, Float, Complex, String, Tuple