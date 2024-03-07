def swapPositions(lis, pos1, pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis
# code
List = [16, 17, 18, 19]
pos1, pos2 = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))
