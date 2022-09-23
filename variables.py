print("hello world")

message = "Hello World" # defining a variable , using a string
print(message)

# Anything in a quote is considered a string
name = "harry hill"
print (name.title()) # this will make the first letters of the word in capitals
print (name.upper()) # all lowercase
print (name.lower()) # all uppercase

# f-strings - f is for format
first_name="father"
second_name="christmas"
name = f"{first_name} {second_name}" #we can use an f-string to combine variables
print(name)
print(f"Hello, {first_name.title()}")

notice=f"Hello, {first_name.title()}" # an f-string can be included in a variable
print(notice)


