class Patient:
    """
    A class representing a patient with a name and priority.
    """
    def __init__(self, name, priority, order):
        self.name = name
        self.priority = priority
        self.order = order  # Se usa para mantener el orden de llegada

    def __str__(self):
        return f"{self.name} (Priority: {self.priority})"
    
    def __repr__(self):
        return f"Patient({self.name!r}, {self.priority!r}, {self.order!r})"

    def __lt__(self, other):
        # Ordena primero por prioridad, luego por orden de llegada
        if self.priority == other.priority:
            return self.order < other.order
        return self.priority < other.priority


class Queue:
    """
    A queue to manage patients, ordered by arrival.
    """
    def __init__(self):
        self.items = []
        self.counter = 0  # Mantiene el orden de llegada

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, name, priority):
        self.counter += 1
        new_patient = Patient(name, priority, self.counter)
        self.items.append(new_patient)
        return new_patient

    def dequeue(self):
        if not self.is_empty():
            # Encuentra al paciente con mayor prioridad (menor número) y orden de llegada
            highest_priority = min(self.items)
            self.items.remove(highest_priority)
            return highest_priority
        raise IndexError("Dequeue from empty queue")

    def size(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)


menu = f"""
{"=" * 40}
      Patient Management System
{"=" * 40}
1. Add Patient
2. Attend Patient (by priority)
3. Show Patients (by arrival)
4. Show Patients (by priority)
5. Exit
{"=" * 40}
Select an option (1-5): """


def main():
    queue = Queue()

    # 🌟 Ejemplo con 8 pacientes precargados
    preload = [
        ("Ana", 3), ("Luis", 2), ("Marta", 1), ("Carlos", 5),
        ("Lucía", 2), ("Pedro", 1), ("Sara", 3), ("Elena", 4)
    ]
    for name, priority in preload:
        queue.enqueue(name, priority)

    while True:
        print("\n" + "=" * 40)
        try:
            choice = int(input(menu))

            if choice == 1:
                name = input("Enter patient name: ").strip()
                priority = int(input("Enter priority (1=Urgent, 5=Low): "))
                if priority < 1 or priority > 5:
                    print("Priority must be between 1 and 5.")
                    continue
                p = queue.enqueue(name, priority)
                print(f"✅ Added: {p}")

            elif choice == 2:
                if not queue.is_empty():
                    patient = queue.dequeue()
                    print(f"🚑 Attending to: {patient}")
                else:
                    print("⚠️ No patients in the queue.")

            elif choice == 3:
                if not queue.is_empty():
                    print("📋 Patients (by arrival):")
                    for p in queue:
                        print(f"- {p}")
                else:
                    print("⚠️ No patients in the queue.")

            elif choice == 4:
                if not queue.is_empty():
                    sorted_patients = sorted(queue.items)
                    print("📋 Patients (by priority):")
                    for p in sorted_patients:
                        print(f"- {p}")
                else:
                    print("⚠️ No patients in the queue.")

            elif choice == 5:
                print("👋 Exiting the system. Goodbye!")
                break

            else:
                print("❌ Invalid option. Please try again.")
        
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
        
        except KeyboardInterrupt:
            print("\n👋 Exiting the system. Goodbye!")
            break


if __name__ == "__main__":
    main()
