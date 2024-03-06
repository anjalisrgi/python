def isPalindrome(s):
	return s == s[::-1]


# code
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
