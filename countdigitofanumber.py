num=int(input("Enter number: "))
count=0
i = num
# count digits of a number
while(i>0):
    count=count+1
    i=i//10
print(f"The number of digits in {num}:",count)
