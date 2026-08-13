def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Input
arr = [10, 20, 30, 40, 50]

target = int(input("Enter the element to search: "))

# Function call
position = linear_search(arr, target)

# Output
if position != -1:
    print("Element", target, "found at position", position)
else:
    print("Element", target, "not found")
    
