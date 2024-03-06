def isPalindrome(s):
	return s == s[::-1]


# code
s = "abba"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
