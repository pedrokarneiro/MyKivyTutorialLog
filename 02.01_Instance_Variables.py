# This is how the variables of an instance work.
# Suppose you have a class A().
# Then you instantiate it in a and in b.
# Then you add a variable x to each of the instances.
# Despite these variables have the same name, they belong to different instances.
class A():
    pass

a = A()
a.x = 3

b = A()
b.x = 5

print(a.x)
print(b.x)
