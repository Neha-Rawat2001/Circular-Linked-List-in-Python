#create a node
class Node:
    def __init__(self,item = None, next = None):
        self.item = item
#create CLL class
class CLLL:
    #define a last reference variable 
    def __init__(self, last = None):
        self.last = last
    
    #define is_empty() method
    def is_empty(self):
        return self.last == None
    
    #define insert_at_first() method
    def insert_at_first(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            
    #define search() method
    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp! = self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return None
        return None
    
    #define delete_first() method
    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
    
    #define delete_last() method
    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
                
    #define delete_after() method
    def delete_after(self,temp):
        