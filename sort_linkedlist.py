'''
https://leetcode.com/problems/sort-list/description/

Bubble Sort: O(n*n)
'''


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class LinkedList:

    def __init__(self):
        self.head = None 

    def append(self, data):
        node = Node(data)
        if self.head is None:
            
            self.head = node 
            return 
        
        ptr = self.head 

        while ptr.next :
            ptr = ptr.next 

        ptr.next = node 
        return 
    
    def print_list(self):

        ptr = self.head 

        while ptr :
            if ptr.next :
                print(ptr.data, end = " -> ")
            else:
                print(ptr.data)
            
            ptr = ptr.next

    def bubble_sort(self):

        # this is used to restrict the end of the list after each iteration 
        # after every single iteration, largest element would be at end, so we won't unnecessary compare elements after "end" value
        end = None

        #continue loop till end does not reach start of the loop
        while end != self.head:
            ptr = self.head 

            # traverse till END value
            while ptr.next !=end:
                qtr = ptr.next 

                if ptr.data > qtr.data:
                    ptr.data, qtr.data = qtr.data, ptr.data 
                ptr = ptr.next 

            # last element is at correct position
            end = ptr

    # given sorted list, where to insert this new node 
    def sorted_node_insert(self, sorted_list, new_node):

        # if new_node is None 
        if not new_node:
            return sorted_list
        
        # if sorted_list is None and new_node exists
        if not sorted_list :
            return new_node

        # if the new_node value is greater than first value itself 

        if new_node.data < sorted_list.data:
            new_node.next = sorted_list 
            return new_node 
        
        current = sorted_list 
        while current.next and current.next.data < new_node.data:
            current = current.next 

        new_node.next = current.next 
        current.next = new_node 
        return sorted_list
        
    def insertion_sort(self):

        current = self.head 
        sorted_list = None

        while current:
            next_node = current.next 
            node = Node(current.data)
            sorted_list = self.sorted_node_insert(sorted_list, node)
            current = next_node 

        # return copy or self.head = sorted_list
        # return sorted_list 
        self.head = sorted_list

    # splits list into two halves 
    def split_list(self, head):

        # fast and slow pointer approach 

        # might return none, so handle in the merged_sorted_list function
        if not head or not head.next:
            return head

        slow_ptr = head 
        fast_ptr = head

        while fast_ptr and fast_ptr.next and fast_ptr.next.next :
            fast_ptr = fast_ptr.next.next 
            slow_ptr = slow_ptr.next 
        
        # slow ptr will be pointing to mid 

        mid = slow_ptr.next 

        # so that two different lists can be created        
        slow_ptr.next = None

        return head, mid
    

    # recursively merge two sorted list 
    def merge_sorted_list(self, left, right):

        if not left:
            return right 
    
        if not right:
            return left 
        
        # check the first element of both lists 
        if left.data < right.data:
            left.next = self.merge_sorted_list(left.next, right)
            return left 
        else:
            right.next = self.merge_sorted_list(left, right.next)
            return right 
        
    


    # we split the list till there is single node list left
    def merge_sort(self, head):
        if not head or not head.next:
            return head
        
        # basically finding the mid of the list and creating two different lists 
        left , right = self.split_list(head)

        # recursively call merge till single node is left 
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge_sorted_list(left, right)
        

        

ll = LinkedList()

ll.append(11)

ll.append(5)
ll.append(4)
ll.append(6)
ll.append(10)
ll.append(2)
ll.append(90)

ll.print_list()
# ll.bubble_sort()
# ll.insertion_sort()

ll.head = ll.merge_sort(ll.head)

ll.print_list()