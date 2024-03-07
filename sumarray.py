def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_sum = sum_of_array(arr, low, mid)
    right_sum = sum_of_array(arr, mid+1, high)
    return left_sum + right_sum
#Examples
arr = [5, 6, 7]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 18
 
arr = [1, 2, 13, 10]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 26
