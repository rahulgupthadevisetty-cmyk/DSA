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
arr = [50, 20, 70, 10, 40, 60, 30]

target = int(input("Enter the element to search: "))

# Sort the array
arr.sort()

# Function call
position = binary_search(arr, target)

# Output
print("Sorted array:", arr)

if position != -1:
    print("Element", target, "found at position", position)
else:
    print("Element", target, "not found")
