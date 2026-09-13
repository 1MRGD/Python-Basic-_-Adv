# Reverse a string without using a built-in reverse function

text = input("Enter a string: ")

reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text = reversed_text + text[i]

print("Reversed string:", reversed_text)