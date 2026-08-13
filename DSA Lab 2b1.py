def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
arr = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter the element to search: "))

# Function call
position = binary_search(arr, target)

# Output
if position != -1:
    print("Element", target, "found at position", position)
else:
    print("Element", target, "not found")
