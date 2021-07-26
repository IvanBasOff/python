string = "Hello"
print(string[0])
print(string[-1])
print(string.upper())
print(string.lower())

#format
a = 'test'
b = 'This is {}'.format(a)
print(b)

#join
a = 'abc'
print('+'.join(a))
words = ['a', 'b', 'c', 'd']
print("   ".join(words))

#capitalize
print("text".capitalize())

#split
print("This, is, text".split(","))

#strip
print("    TEST   ".strip())

#replace
print("TEST TEST TEST".replace("E", "O"))

#index
print("This is a little test".index("a"))

#in
print("Hey" in "Hey \"all!\"")

#\n
print("this\nis\ntext")

#cutting
text = "Some sample text for exercises"
print(text[5:12])
print(text[:4])
print(text[4:].strip())
fict = ["test1", "test2", "test3", "test4"]
print(fict[0:2])
