# To  find reverse words in a given string
string = "my name is anjali"
s = string.split()[::-1]
l = []
for i in s:
	l.append(i)
print(" ".join(l))
