class Patient:
    """
    A class representing a patient with a name and priority.
    """
    def __init__(self, name: str, priority: int):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name must be a non-empty string")
        if not isinstance(priority, int) or priority < 1 or priority > 5:
            raise ValueError("Priority must be an integer between 1 and 5")
        
        self.name = name.strip()
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
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        """Add an item to the rear of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)

    def peek(self):
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty queue")
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self.items.clear()
    
    def __str__(self):
        return f"Queue({self.items})"

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("    Patient Management System")
    print("=" * 40)
    print("1. Add Patient")
    print("2. Attend Next Patient")
    print("3. Show All Patients (Order by arrival)")
    print("4. Show All Patients (Order by priority)")
    print("5. Show Queue Status")
    print("6. Clear Queue")
    print("7. Exit")
    print("=" * 40)


def add_patient(queue: Queue) -> None:
    """Add a new patient to the queue."""
    try:
        name = input("Enter patient name: ").strip()
        if not name:
            print("Error: Patient name cannot be empty.")
            return
        
        priority_input = input("Enter patient priority (1-5, 1 being highest): ")
        priority = int(priority_input)
        
        patient = Patient(name, priority)
        queue.enqueue(patient)
        print(f"✓ Patient '{patient.name}' with priority {patient.priority} added to the queue.")
        
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Error: Priority must be a number between 1 and 5.")
        else:
            print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def attend_patient(queue: Queue) -> None:
    """Attend to the next patient in the queue."""
    try:
        if not queue.is_empty():
            attended_patient = queue.dequeue()
            print(f"✓ Now attending to: {attended_patient}")
        else:
            print("No patients in the queue.")
    except Exception as e:
        print(f"Error attending patient: {e}")


def show_patients_by_arrival(queue: Queue) -> None:
    """Display all patients in order of arrival."""
    if not queue.is_empty():
        print(f"\nPatients in queue (order of arrival) - Total: {len(queue)}")
        print("-" * 40)
        for i, patient in enumerate(queue, 1):
            print(f"{i}. {patient}")
    else:
        print("No patients in the queue.")


def show_patients_by_priority(queue: Queue) -> None:
    """Display all patients sorted by priority."""
    if not queue.is_empty():
        sorted_patients = sorted(queue.items, key=lambda x: x.priority)
        print(f"\nPatients sorted by priority - Total: {len(queue)}")
        print("-" * 40)
        for i, patient in enumerate(sorted_patients, 1):
            priority_text = {1: "(Highest)", 2: "(High)", 3: "(Medium)", 4: "(Low)", 5: "(Lowest)"}
            print(f"{i}. {patient} {priority_text.get(patient.priority, '')}")
    else:
        print("No patients in the queue.")


def show_queue_status(queue: Queue) -> None:
    """Display queue status and statistics."""
    if not queue.is_empty():
        print(f"\nQueue Status:")
        print(f"Total patients: {len(queue)}")
        print(f"Next patient: {queue.peek()}")
        
        # Priority distribution
        priority_count = {}
        for patient in queue:
            priority_count[patient.priority] = priority_count.get(patient.priority, 0) + 1
        
        print("\nPriority distribution:")
        for priority in sorted(priority_count.keys()):
            print(f"  Priority {priority}: {priority_count[priority]} patient(s)")
    else:
        print("Queue is empty.")


def clear_queue(queue: Queue) -> None:
    """Clear all patients from the queue with confirmation."""
    if not queue.is_empty():
        confirmation = input(f"Are you sure you want to clear all {len(queue)} patients? (y/N): ")
        if confirmation.lower() in ['y', 'yes']:
            queue.clear()
            print("✓ Queue cleared successfully.")
        else:
            print("Operation cancelled.")
    else:
        print("Queue is already empty.")


def main():
    """Main function to run the Patient Management System."""
    queue = Queue()  # Create queue outside the loop to persist data
    
    print("Welcome to the Patient Management System!")
    
    while True:
        try:
            display_menu()
            choice = input("Please select an option (1-7): ").strip()
            
            if choice == '1':
                add_patient(queue)
            
            elif choice == '2':
                attend_patient(queue)
            
            elif choice == '3':
                show_patients_by_arrival(queue)
            
            elif choice == '4':
                show_patients_by_priority(queue)
            
            elif choice == '5':
                show_queue_status(queue)
            
            elif choice == '6':
                clear_queue(queue)
            
            elif choice == '7':
                print("\nThank you for using the Patient Management System!")
                print("Goodbye! 👋")
                break
            
            else:
                print("❌ Invalid option. Please select a number between 1 and 7.")
        
        except KeyboardInterrupt:
            print("\n\nSystem interrupted. Goodbye! 👋")
            break
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()