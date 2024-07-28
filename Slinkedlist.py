
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_ending(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None)

    def insert_data_list(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_ending(data)

    def remove_at(self,index):
        if index<0:
            raise Exception("invalid Value")
        if index == 0:
            self.head = self.head.next
        count =0
        temp = self.head
        while temp:
            if count == index -1:
                temp.next = temp.next.next
            temp = temp.next
            count+=1

    def inset_at(self,index,value):
        if index<0:
            raise Exception("invalid Value")
        if index == 0:
            node = Node(value,self.head)
            self.head = node

        temp = self.head
        count = 0
        while temp:
            if count == index -1:
                #the previous node next would be your new node next , your sneaking inside b/w them
                node = Node(value,temp.next)
                #the previous node next locate the new node
                temp.next = node
                break
            temp = temp.next
            count += 1
              



    def print(self):
        print("worked")
        if self.head is None:
            print("linkedlist is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next

ls = LinkedList()
ls.insert_at_beginning(12345)
ls.insert_data_list([1,3,4,5,6,7,8])
ls.inset_at(3,43)
ls.inset_at(0,43)


ls.print()
        