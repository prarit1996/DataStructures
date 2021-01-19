class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkList:
    def __init__(self):
        self.head=None
        self.length=0

    def push(self,data):
        if self.head==None:
            self.head=node(data)
            self.length+=1
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
            self.length+=1
    def pop(self):
        if self.head!=None:
            if self.length==1:
                self.head=None
                self.length-=1
            else:
                self.head=self.head.next
                self.length-=1
        
            
            
    def printStack(self):
        if self.head!=None:
            temp=self.head
            print("Length of stack is ",self.length)
            while temp.next!=None:
                print(temp.data,end=" -> ")
                temp=temp.next
            print("",temp.data)
        else:
            print("Empty Stack")

stack=linkList()
stack.push(5)
stack.push(8)
stack.push(9)
stack.printStack()
stack.pop()
stack.printStack()
stack.pop()
stack.printStack()
stack.pop()
stack.printStack()
stack.pop()
stack.printStack()


            
