class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def search(head, key):
        current = head
        while current is not None:
            if current.value == key:
                return True
            current = current.next
        return False
    
    def insert_after_nth_node(head, n, value):
        current = head
        size = 1 
        new_node = LLNode(value)

        while current and size < n:
            current = current.next 
            size += 1 
        if new_node is None:
            print("Error")
            return head

        new_node.next = current.next 
        current.next = new_node

        return head


z = LLNode(3, None)
y = LLNode(2, z)
x = LLNode(1, y)

n_insert = 4
n_position = 2
LLNode.insert_after_nth_node(x, n_position, n_insert)

key_search = 2
print(LLNode.search(x, key_search)) 

current = x
while current is not None:
    print(current.value, end=" -> ")
    current = current.next
print()