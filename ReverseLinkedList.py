class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


class Linklist:
    def __init__(self):
         self.head = None

    def insert_data(self,data):     
        if self.head is None:
                self.head = Node(data,None)
                return
            
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None)


    def Reverse(self):
         temp = self.head
         while temp.next:
            temp = temp.next
         self.head = temp.next

            





    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next



ls=Linklist()
ls.insert_data(1)
ls.insert_data(2)
ls.insert_data(3)
ls.Reverse()

