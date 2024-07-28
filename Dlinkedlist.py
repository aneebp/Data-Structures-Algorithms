class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data= data
        self.next = next
        self.prev = prev

class LinkList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_at_ending(self,data):
        if self.head == None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new_node = Node(data,None,temp)
        temp.next =new_node

    def insert_data_list(self,datalist):
        self.head = None
        for data in datalist:
            self.insert_at_ending(data)

    def remove_at(self,index):
        if index<0:
            raise Exception("Invalid Value")
        if index == 0:
            if self.head is None:
                print("list is empty")
            self.head = self.head.next
            if self.head is not None:
                self.head.prev= None
        temp = self.head
        count = 0
        while temp:
            if count == index -1:
                temp.next = temp.next.next
            temp = temp.next
            count += 1

    def insert_at(self,index,data):
        if index<0:
            raise Exception("Invalid Value")
            return
        if index == 0:
            new_node = Node(data,self.head,None)
            self.head = new_node
            return
        
        temp = self.head
        count = 0
        while temp:
            if count == index -1:
                temp.next = Node(data,temp.next,temp.next.next)
            temp = temp.next
            count += 1



    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next



ls= LinkList()
ls.insert_at_ending(12)
ls.insert_at_ending(1233)
ls.insert_at_ending(10)
ls.insert_data_list([1,2,3,4,5,6,7,8,9])
ls.remove_at(2)
ls.insert_at(6,10)
ls.print()
