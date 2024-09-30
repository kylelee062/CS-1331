class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, n):
        self.size = n
        self.head = None

    def circular(self):
        #Makes the linked list circular
        if self.size <= 0:
            return
        self.head = Node(0)
        current = self.head
        for i in range(1, self.size):
            current.next = Node(i)
            current = current.next
        current.next = self.head

    def remove(self, node):
        if node.next == node:  #If only one node left
            self.head = None
        else:
            node.next = node.next.next

    def last_one(self, k):
        if not self.head:
            return None

        current = self.head
        while current.next != current:  #Repeats until only one node left
            for _ in range(k - 1):  #Move k amount of steps
                current = current.next
            self.remove(current)  
            current = current.next  #Move to the next node after removal

        return current.data
    
def last_potato(n, k):
    if n <= 0 or k <= 0:  
        return None
    LL = LinkedList(n)  #Instantiate LinkedList with size n
    LL.circular()  #Calls circular method on the instance
    return LL.last_one(k) #Returns the value k in the last_one method

n = 11
k = 3
print("Last remaining person:", last_potato(n, k))  #Output: 8
