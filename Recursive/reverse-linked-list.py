def reverse_linked_list(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverse_linked_list(head.next)
    
    head.next.next = head
    head.next = None
    
    return new_head

