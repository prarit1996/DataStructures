class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkList:
    def __init__(self):
        self.head=None
        self.length=0

    def enqueue(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)
        self.length+=1
        
    def dequeue(self):
        if self.head!=None:
            if self.length==1:
                self.head=None
                self.length-=1
            else:
                self.head=self.head.next
                self.length-=1

    def printQueue(self):
        if self.head!=None:
            temp=self.head
            print("Length of queue is ",self.length)
            while temp.next!=None:
                print(temp.data,end=" -> ")
                temp=temp.next
            print("",temp.data)
            print("\n")
        else:
            print("Empty Queue\n")

queue=linkList()
queue.enqueue(5)
queue.printQueue()
queue.enqueue(8)
queue.printQueue()
queue.enqueue(9)
queue.printQueue()
queue.dequeue()
queue.printQueue()
queue.dequeue()
queue.printQueue()
queue.dequeue()
queue.printQueue()

