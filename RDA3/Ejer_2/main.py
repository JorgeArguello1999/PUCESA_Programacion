class patient:
    """
    A class representing a patient with a name and priority.
    """
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"Patient(Name: {self.name}, Priority: {self.priority})"
    
    def __repr__(self):
        return f"Patient({self.name!r}, {self.priority!r})"
    
    def __getitem__(self, index):
        if index == 0:
            return self.name
        elif index == 1:
            return self.priority
        else:
            raise IndexError("Index out of range for patient attributes")

class Queue:
    """
    A simple queue implementation using a list.
    This queue supports basic operations like enqueue, dequeue, peek, and size.
    """
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item) -> 'Queue':
        self.items.append(item)
        return item

    def dequeue(self) -> 'Queue':
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> 'Queue':
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty queue")
    
    def __str__(self):
        return f"Queue({self.items})"

    def __iter__(self):
        return iter(self.items)


menu = f"""
{"=" * 30}
Welcome to the Patient Management System
{"=" * 30}

1. Add Patient
2. Attend Patient
3. Show Patients (Order by arrival)
4. Show Patients (Order by priority)
5. Exit

{"=" * 30}

Please select an option (1-5): """

def main():
    while True:
        try:
            queue = Queue()
            choice = int(input(menu))

            if choice == 1:
                name = input("Enter patient name: ")
                priority = int(input("Enter patient priority (1-5, 1 being highest): "))
                p = patient(name, priority)
                queue.enqueue(p)
                print(f"Patient {p} added to the queue.")

            elif choice == 2:
                if not queue.is_empty():
                    attended_patient = queue.dequeue()
                    print(f"Attending to {attended_patient}.")
                else:
                    print("No patients in the queue.")

            elif choice == 3:
                if not queue.is_empty():
                    print("Patients in order of arrival:")
                    for p in queue:
                        print(p)
                else:
                    print("No patients in the queue.")

            elif choice == 4:
                if not queue.is_empty():
                    sorted_patients = sorted(queue.items, key=lambda x: x.priority)
                    print("Patients in order of priority:")
                    for p in sorted_patients:
                        print(p)
                else:
                    print("No patients in the queue.")

            elif choice == 5:
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
        
        except KeyboardInterrupt:
            print("\nExiting the system. Goodbye!")
            break


if __name__ == "__main__":
    main()
