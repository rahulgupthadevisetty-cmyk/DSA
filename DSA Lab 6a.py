queue = []

def enqueue () :
    value = int(input("Enter element to insert: "))
    queue.append(value)
    print(value, "inserted into queue.")

def dequeue () :
    if len(queue) == 0:
        print("Queue is Empty.")
    else:
        value = queue.pop (0)
        print(value, "deleted from queue.")

def peek () :
    if len(queue) == 0:
        print("Queue is Empty.")
    else:
        print("Front element is:", queue[0])

def display ():
    if len(queue) == 0:
        print("Queue is Empty.")
    else:
        print("Queue elements are:", queue)
while True:
    print("\n--- QUEUE USING ARRAY ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue ()

    elif choice == 2:
        dequeue ()

    elif choice == 3:
        peek ()

    elif choice == 4:
        display ()

    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
    
