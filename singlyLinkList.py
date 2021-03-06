class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkList:
    def __init__(self):
        self.head=None
        self.length=0

    def insert(self,data):
        if self.head==None:
            self.head=node(data)
            
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)
        self.length+=1
    def insertAtPosition(self,data,position):
        if self.head==None:
            if position!=1:
                print("List is empty, we can not insert at position ",position)
            else:
                self.insert(data)
        elif position > self.length:
           choice= input("Position does not exist. Do you want to insert at the end of the list? Press Y for Yes, N for No. ")
           print()
           print()
           if choice=="Y":
               self.insert(data)
           else:
               return
        else:
            temp=self.head
            element_count=1
            while element_count<position:
                temp1=temp
                temp=temp.next
                element_count+=1
            temp2=node(data)
            temp1.next=temp2
            temp2.next=temp
            self.length+=1
    def deleteFromList(self,data):
        temp=self.head
        count=1
        temp1=temp
        
        while temp.data!=data and temp.next!=None:
            temp1=temp
            temp=temp.next
            count+=1
        if self.length==1:
            if temp.data==data:
                self.head=None
                self.length=-1
            else:
                print("element does not exist")
        elif count==self.length:
            if temp.data!=data:
                print("element does not exist")
            else:
                temp1.next=None
                self.length-=1
        elif self.length==0:
            print("List is empty")
        
        else:
            temp1.next=temp.next
            self.length-=1
        
    def printList(self):
        if self.head!=None:
            temp=self.head
            print("Length of Linked List: ",self.length )
            while temp.next!=None:
                print(temp.data,end=" -> ")
                temp=temp.next
            print(temp.data)
        else:
            print("list is empty")
        print()
        print()

list1=linkList()
list1.insert(1)
list1.insert(2)
list1.printList()
list1.insertAtPosition(3,3)
list1.printList()
list1.insertAtPosition(4,2)
list1.printList()
list1.deleteFromList(4)
list1.printList()
list1.deleteFromList(3)
list1.printList()
list1.deleteFromList(2)
list1.printList()
list1.deleteFromList(4)
list1.printList()
list1.deleteFromList(1)
list1.printList()
