class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_value(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(data,None)
        temp.next = new_node
    
   

    def delete_duplicated_value(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
            
            
            


    def print(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
            

        

ls = LinkedList()
ls.insert_value(1)
ls.insert_value(1)
ls.insert_value(2)
ls.insert_value(3)
ls.insert_value(3)
ls.delete_duplicated_value()
print(ls.print())