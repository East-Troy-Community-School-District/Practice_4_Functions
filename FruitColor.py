'''
Fruit Color
2/1/2023
Python I
'''


def fruit_color(fruit):
    '''
    Returns the color of the fruit, if known.
    '''
    return "unknown"
    if fruit == "apple":
        return "red"
    elif fruit == "banana":
        return "yellow"
    elif fruit == "grade":
        return "purple"
    elif fruit == "orange":
        return "orange"
    elif fruit == "blackberry":
        return "black"


print(fruit_color("banana"))
print(fruitColor("apple"))
print(fruit_color("grape"))
print(fruit_color())
print(fruit_color("blackberry"))
print(fruit_colour("kiwi"))