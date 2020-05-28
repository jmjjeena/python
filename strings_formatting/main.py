# f-strings
first_name = "Jeena"
last_name = "John"

print(f"Hello {first_name} {last_name}")
# with .format()
name = "Sam"
greeting = "Hello {}"
with_name = greeting.format(name)
with_name2 = greeting.format('Tedd')
'''
What is happening here?

    --> Calling the format() inside of greeting
    --> It is giving the name to this template
    --The template will replace the curly braces by the contents of the name variable

Benefits of this:
    --> define a template and reuse it with multiple values
'''

print(with_name)
print(with_name2)

'''
format():
    --> with format() we make longer template
'''
longer_phase = "Hello {}. Today is {}."

formatted = longer_phase.format("Rolf", "Monday")

print(formatted)
