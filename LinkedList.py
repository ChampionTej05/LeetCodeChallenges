
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class LinkedList:

    def __init__(self) :
        self.head = None

    def print_list(self):
        ptr = self.head 
        while ptr != None:
            print(ptr.value, end= ' -> ')
            ptr = ptr.next
        print("None")

    def insert_at_end(self, value):

        node = Node(value)

        if self.head == None:
            self.head = node 
            return 
        ptr = self.head 

        while ptr.next != None:
            ptr = ptr.next 

        ptr.next = node 


    def insert_at_start(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node 
            return 
        
        ptr = self.head 
        node.next = ptr 
        self.head = node 


    def is_exist(self, value):

        ptr = self.head 

        while ptr!=None:
            if ptr.value == value :
                return True 
            ptr = ptr.next 
            
        return False 
    
    def is_empty(self):
        return self.head == None 

    def remove_at_end(self):
        if self.head == None:
            return 
        
        if self.head.next == None:
            self.head = None 
            return 
        
        ptr = self.head 
        while ptr.next.next != None:
            ptr = ptr.next 

        ptr.next = None 

    def remove_at_start(self):
        if self.head == None:
            return 
        
        if self.head.next == None:
            self.head = None
            return 
        
        ptr = self.head.next.next 
        self.head.next = None 
        self.head = ptr 

    def remove_specific_element(self,value):

        if self.head == None:
            return 
        
        if self.head.value == value:
            self.head = None 
            return 
        
        slowPtr = self.head 
        ptr = self.head.next 
        while ptr.next != None:
            if ptr.value == value:
                temp = ptr.next 
                ptr.next = None 
                slowPtr.next = temp 
            slowPtr = slowPtr.next 
            ptr = ptr.next 

        






    
    @classmethod
    def create_from_list(cls, list_arr):
        linked_list = cls() #create an instance of the class 
        for item in list_arr:
            linked_list.insert_at_end(item)

        return linked_list
    



    

    


arr = [1,2,3,4,5]

linked_list= LinkedList.create_from_list(arr)
linked_list.print_list()
linked_list.insert_at_start(0)
linked_list.print_list()

linked_list.insert_at_end(6)
linked_list.print_list()

linked_list.remove_at_end()
linked_list.print_list()

linked_list.remove_at_start()
linked_list.print_list()

linked_list.remove_specific_element(3)
linked_list.print_list()

arr1 = [1,2]
linked_list1 = LinkedList.create_from_list(arr1)
linked_list1.print_list()
linked_list1.remove_at_end()
linked_list1.print_list()
linked_list1.remove_at_end()
linked_list1.print_list()
linked_list1.remove_at_end()
linked_list1.print_list()


                
