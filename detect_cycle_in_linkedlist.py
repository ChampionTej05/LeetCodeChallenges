class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    aset= set()
    current = head 

    while current != None:
        mem_addr = id(current)
        if mem_addr in aset:
            return True 
        else:
            aset.add(mem_addr)
            current = current.next 
    return False 

def hasCycleFastSlowPointer(head):

    #single node 
    if not head or not head.next:
        return False 
    
    slowPtr = head 
    fastPtr = head.next 

    while fastPtr != None:
        if slowPtr == fastPtr:
            return True 
        slowPtr = slowPtr.next 
        fastPtr = fastPtr.next.next if fastPtr.next is not None else fastPtr.next 
    return False


def test_hasCycle():
    # Helper function to create a linked list with a cycle
    def create_linked_list_with_cycle(values, cycle_index):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        cycle_node = None
        for i, val in enumerate(values[1:]):
            current.next = ListNode(val)
            current = current.next
            if i == cycle_index:
                cycle_node = current  # Set the cycle node
        if cycle_node:
            current.next = cycle_node  # Create a cycle
        return head

    # Test case 1: Linked list with a cycle
    arr1 = [1, 2, 3, 4, 5]
    cycle_index1 = 2
    head1 = create_linked_list_with_cycle(arr1, cycle_index1)
    result1 = hasCycleFastSlowPointer(head1)
    assert result1 is True

    # Test case 2: Linked list without a cycle
    arr2 = [1, 2, 3, 4, 5]
    head2 = ListNode(arr2[0])
    current2 = head2
    for val in arr2[1:]:
        current2.next = ListNode(val)
        current2 = current2.next
    result2 = hasCycleFastSlowPointer(head2)
    assert result2 is False

    # Test case 3: Empty linked list
    head3 = None
    result3 = hasCycleFastSlowPointer(head3)
    assert result3 is False

    print("All test cases passed!")

# Run the test function
test_hasCycle()
