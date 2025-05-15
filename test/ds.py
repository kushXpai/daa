class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DataStructures:
    def __init__(self):
        self.array = []
        self.sll_head = None  # Singly Linked List head
        self.dll_head = None  # Doubly Linked List head
        self.stack = []
        self.queue = []
        self.comparisons = 0
        self.shifts = 0
    
    def create(self, ds_type):
        self.comparisons = 0
        self.shifts = 0
        if ds_type == 'array':
            self.array = []
        elif ds_type == 'sll':
            self.sll_head = None
        elif ds_type == 'dll':
            self.dll_head = None
        elif ds_type == 'stack':
            self.stack = []
        elif ds_type == 'queue':
            self.queue = []
        print(f"{ds_type.upper()} created successfully")
    
    def insert(self, ds_type, value, position=None):
        self.comparisons = 0
        self.shifts = 0
        
        if ds_type == 'array':
            if position is None:
                position = len(self.array)
            self.array.insert(position, value)
            self.shifts += len(self.array) - position
            
        elif ds_type == 'sll':
            new_node = Node(value)
            if position == 0 or self.sll_head is None:
                new_node.next = self.sll_head
                self.sll_head = new_node
                self.shifts += 1
            else:
                current = self.sll_head
                for i in range(position - 1):
                    if current.next:
                        current = current.next
                        self.shifts += 1
                new_node.next = current.next
                current.next = new_node
                self.shifts += 1
                
        elif ds_type == 'dll':
            new_node = Node(value)
            if position == 0 or self.dll_head is None:
                new_node.next = self.dll_head
                if self.dll_head:
                    self.dll_head.prev = new_node
                self.dll_head = new_node
                self.shifts += 1
            else:
                current = self.dll_head
                for i in range(position - 1):
                    if current.next:
                        current = current.next
                        self.shifts += 1
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                self.shifts += 1
                
        elif ds_type == 'stack':
            self.stack.append(value)
            self.shifts += 1
            
        elif ds_type == 'queue':
            self.queue.append(value)
            self.shifts += 1
            
        print(f"Inserted {value} successfully")
        print(f"Comparisons: {self.comparisons}, Shifts: {self.shifts}")
    
    def search(self, ds_type, value):
        self.comparisons = 0
        self.shifts = 0
        
        if ds_type == 'array':
            for i, item in enumerate(self.array):
                self.comparisons += 1
                if item == value:
                    return i
                    
        elif ds_type == 'sll':
            current = self.sll_head
            position = 0
            while current:
                self.comparisons += 1
                if current.data == value:
                    return position
                current = current.next
                position += 1
                self.shifts += 1
                
        elif ds_type == 'dll':
            current = self.dll_head
            position = 0
            while current:
                self.comparisons += 1
                if current.data == value:
                    return position
                current = current.next
                position += 1
                self.shifts += 1
                
        elif ds_type == 'stack':
            for i, item in enumerate(self.stack):
                self.comparisons += 1
                if item == value:
                    return i
                    
        elif ds_type == 'queue':
            for i, item in enumerate(self.queue):
                self.comparisons += 1
                if item == value:
                    return i
                    
        print(f"Element {value} not found")
        print(f"Comparisons: {self.comparisons}, Shifts: {self.shifts}")
        return -1
    
    def delete(self, ds_type, position):
        self.comparisons = 0
        self.shifts = 0
        
        if ds_type == 'array':
            if 0 <= position < len(self.array):
                deleted = self.array.pop(position)
                self.shifts += len(self.array) - position
                print(f"Deleted {deleted}")
                
        elif ds_type == 'sll':
            if position == 0 and self.sll_head:
                deleted = self.sll_head.data
                self.sll_head = self.sll_head.next
                self.shifts += 1
                print(f"Deleted {deleted}")
            else:
                current = self.sll_head
                for i in range(position - 1):
                    if current and current.next:
                        current = current.next
                        self.shifts += 1
                if current and current.next:
                    deleted = current.next.data
                    current.next = current.next.next
                    self.shifts += 1
                    print(f"Deleted {deleted}")
                    
        elif ds_type == 'dll':
            if position == 0 and self.dll_head:
                deleted = self.dll_head.data
                self.dll_head = self.dll_head.next
                if self.dll_head:
                    self.dll_head.prev = None
                self.shifts += 1
                print(f"Deleted {deleted}")
            else:
                current = self.dll_head
                for i in range(position):
                    if current:
                        current = current.next
                        self.shifts += 1
                if current:
                    deleted = current.data
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                    self.shifts += 1
                    print(f"Deleted {deleted}")
                    
        elif ds_type == 'stack':
            if self.stack:
                deleted = self.stack.pop()
                self.shifts += 1
                print(f"Deleted {deleted}")
                
        elif ds_type == 'queue':
            if self.queue:
                deleted = self.queue.pop(0)
                self.shifts += len(self.queue)
                print(f"Deleted {deleted}")
                
        print(f"Comparisons: {self.comparisons}, Shifts: {self.shifts}")
    
    def update(self, ds_type, position, value):
        self.comparisons = 0
        self.shifts = 0
        
        if ds_type == 'array':
            if 0 <= position < len(self.array):
                self.array[position] = value
                self.shifts += 1
                
        elif ds_type == 'sll':
            current = self.sll_head
            for i in range(position):
                if current:
                    current = current.next
                    self.shifts += 1
            if current:
                current.data = value
                self.shifts += 1
                
        elif ds_type == 'dll':
            current = self.dll_head
            for i in range(position):
                if current:
                    current = current.next
                    self.shifts += 1
            if current:
                current.data = value
                self.shifts += 1
                
        elif ds_type == 'stack':
            if 0 <= position < len(self.stack):
                self.stack[position] = value
                self.shifts += 1
                
        elif ds_type == 'queue':
            if 0 <= position < len(self.queue):
                self.queue[position] = value
                self.shifts += 1
                
        print(f"Updated successfully")
        print(f"Comparisons: {self.comparisons}, Shifts: {self.shifts}")
    
    def reverse(self, ds_type):
        self.comparisons = 0
        self.shifts = 0
        
        if ds_type == 'array':
            self.array.reverse()
            self.shifts += len(self.array) // 2
            
        elif ds_type == 'sll':
            prev = None
            current = self.sll_head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                self.shifts += 1
            self.sll_head = prev
            
        elif ds_type == 'dll':
            current = self.dll_head
            while current:
                temp = current.next
                current.next = current.prev
                current.prev = temp
                current = temp
                self.shifts += 1
            temp = self.dll_head
            self.dll_head = current if current else temp
            
        print(f"Reversed successfully")
        print(f"Comparisons: {self.comparisons}, Shifts: {self.shifts}")

# Example usage
ds = DataStructures()

# Interactive menu
while True:
    print("\nData Structure Operations:")
    print("1. Create")
    print("2. Insert")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Reverse")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '7':
        break
        
    ds_type = input("Enter data structure type (array/sll/dll/stack/queue): ").lower()
    
    if choice == '1':
        ds.create(ds_type)
    elif choice == '2':
        value = int(input("Enter value to insert: "))
        if ds_type in ['stack', 'queue']:
            ds.insert(ds_type, value)
        else:
            position = int(input("Enter position: "))
            ds.insert(ds_type, value, position)
    elif choice == '3':
        value = int(input("Enter value to search: "))
        position = ds.search(ds_type, value)
        if position != -1:
            print(f"Element found at position {position}")
    elif choice == '4':
        if ds_type in ['stack', 'queue']:
            ds.delete(ds_type, 0)
        else:
            position = int(input("Enter position to delete: "))
            ds.delete(ds_type, position)
    elif choice == '5':
        position = int(input("Enter position to update: "))
        value = int(input("Enter new value: "))
        ds.update(ds_type, position, value)
    elif choice == '6':
        if ds_type in ['array', 'sll', 'dll']:
            ds.reverse(ds_type)
        else:
            print("Reverse operation not supported for this data structure")
            