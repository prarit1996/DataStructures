class Heap:
    def __init__(self):
        self.heap_arr=[]
        self.hashMap={}
        self.heapSize=0
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=data
            self.hashMap[self.root]=[]
            self.hashMap[self.root].append(0)
            self.heap_arr.append(self.root)
            self.heapSize+=1
        else:
            self.heap_arr.append(data)
            self.heapSize+=1
            if data in self.hashMap:
                self.hashMap[data].append(len(self.heap_arr)-1)
            else:
                self.hashMap[data]=[]
                self.hashMap[data].append(len(self.heap_arr)-1)
            parent=(len(self.heap_arr)-2)//2
            child=(len(self.heap_arr)-1)
            self.sinkUp(parent,child)
    def sinkUp(self,parent,child):
        while parent>=0 and self.heap_arr[parent]>self.heap_arr[child]:
            temp=self.heap_arr[parent]
            
            parent_index=self.hashMap[self.heap_arr[parent]].index(parent)
            child_index=self.hashMap[self.heap_arr[child]].index(child)
            self.hashMap[self.heap_arr[parent]][parent_index]=child
            self.hashMap[self.heap_arr[child]][child_index]=parent
            self.heap_arr[parent]=self.heap_arr[child]
            self.heap_arr[child]=temp
            child=parent
            parent=(child-1)//2
    def sinkDown(self,parent):
        while parent<((self.heapSize)//2):
            
            if parent*2+2<self.heapSize:
                if self.heap_arr[parent*2+1]<self.heap_arr[parent*2+2]:
                    minimumChild=self.heap_arr[parent*2+1]
                    minimumChildIndex=parent*2+1
                else:
                    minimumChild=self.heap_arr[parent*2+2]
                    minimumChildIndex=parent*2+2
            else:
                 minimumChild=self.heap_arr[parent*2+1]
                 minimumChildIndex=parent*2+1
            if self.heap_arr[parent]>minimumChild:
                #print(self.hashMap[self.heap_arr[parent]])
                indexParent=self.hashMap[self.heap_arr[parent]].index(parent)
                indexChild=self.hashMap[self.heap_arr[minimumChildIndex]].index(minimumChildIndex)
                self.hashMap[self.heap_arr[minimumChildIndex]][indexChild]=parent
                self.hashMap[self.heap_arr[parent]][indexParent]=minimumChildIndex
                self.heap_arr[parent], self.heap_arr[minimumChildIndex]= self.heap_arr[minimumChildIndex], self.heap_arr[parent]
                parent=minimumChildIndex
                
            else:
                break
    def polling(self):
        if self.root is None:
            print("Empty Heap")
        else:
            indexRoot=self.hashMap[self.heap_arr[0]].index(0)
            indexTail=self.hashMap[self.heap_arr[self.heapSize-1]].index(self.heapSize-1)
            self.hashMap[self.heap_arr[0]][indexRoot]=self.heapSize
            self.hashMap[self.heap_arr[self.heapSize-1]][indexTail]=0
            #print(self.hashMap)
            self.heap_arr[0], self.heap_arr[self.heapSize-1] = self.heap_arr[self.heapSize-1], self.heap_arr[0]
            self.heapSize-=1
            self.sinkDown(0)

    def deleteSpecificElement(self,element):
        if element in self.hashMap:
            indexElement=self.hashMap[element][0]
            
            
            if indexElement!=0:
                indexLast=self.hashMap[self.heap_arr[self.heapSize-1]].index(self.heapSize-1)
                self.hashMap[element][0]=self.heapSize-1
                self.hashMap[self.heap_arr[self.heapSize-1]][indexLast]=indexElement
                self.heap_arr[indexElement]=self.heap_arr[self.heapSize-1]
                self.heap_arr[self.heapSize-1]=element
                if self.heap_arr[indexElement]<self.heap_arr[(indexElement-1)//2]:
                    self.heapSize-=1
                    self.sinkUp((indexElement-1)//2,indexElement)
                else:
                    self.heapSize-=1
                    self.sinkDown(indexElement)
            else:
                self.polling()
            
                
    def heapSort(self):
        array=[5,6,12,8,7,14,19,13,12,11,13,1,4,0,16]
        for i in array:
            self.insert(i)
        for i in range(len(array)):
            self.polling()
        print(self.heap_arr)
        self.heap_arr.reverse()
        print(self.heap_arr)
    def printHeap(self):
        print(self.heapSize)
        for i in range(self.heapSize):
            print(self.heap_arr[i], end=" ")
        print("\n")
    def buildMaxHeap(self):
        self.heap_arr=[5,6,12,8,7,14,19,13,12,11,13,1,4,0,16]
        self.heapSize=len(self.heap_arr)
        for i in range((len(self.heap_arr)//2)-1,-1,-1):
            self.heapify(i)
    def heapify(self,i):
        leftChild=2*i+1
        rightChild=2*i+2
        minimum=i
        if leftChild<len(self.heap_arr) and self.heap_arr[leftChild]<self.heap_arr[i]:
            minimum=leftChild
        if rightChild<len(self.heap_arr) and self.heap_arr[rightChild]<self.heap_arr[minimum]:
            minimum=rightChild
        if minimum!=i:
            self.heap_arr[minimum], self.heap_arr[i] = self.heap_arr[i], self.heap_arr[minimum]
            self.heapify(minimum)
        
        


"""heap.deleteSpecificElement(8)
heap.printHeap()
print("\n\n")
print(heap.hashMap)"""

heap=Heap()
#heap.heapSort()
heap.buildMaxHeap()
heap.printHeap()





































                
            


    
   


