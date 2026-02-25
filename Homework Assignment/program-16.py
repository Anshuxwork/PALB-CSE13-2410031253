"""Problem 16: Merge K Sorted Lists

Merge k sorted linked lists into one sorted list.

Time Complexity: O(n log k) where n is total elements
Space Complexity: O(k) for heap
"""

# Simple Node class for linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """Merges k sorted linked lists.
    
    Args:
        lists: List of linked list heads
    
    Returns:
        Head of merged sorted linked list
    """
    import heapq
    
    # Min heap to keep track of smallest elements
    heap = []
    dummy = ListNode(0)
    current = dummy
    
    # Add first element from each list to heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    node_id = len(lists)
    
    while heap:
        val, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, node_id, node.next))
            node_id += 1
    
    return dummy.next


def _print_list(head):
    """Helper to print linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # Test Case 1: Merge 3 sorted lists
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    
    result = mergeKLists([list1, list2, list3])
    print(f"Test 1 - Merged list: {_print_list(result)}")
    print()
    
    # Test Case 2: Empty input
    result2 = mergeKLists([])
    print(f"Test 2 - Merged list (empty): {_print_list(result2)}")
    print()
    
    # Test Case 3: Single list
    list4 = ListNode(1, ListNode(2, ListNode(3)))
    result3 = mergeKLists([list4])
    print(f"Test 3 - Merged list (single): {_print_list(result3)}")
