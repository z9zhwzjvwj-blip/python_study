def middleNode(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head == None:
        return None

    if head.next == None:
        return head

    if head.next.next == None:
        return head.next

    slow = head
    fast = head

    while fast:
        if fast.next == None:
            return slow
        slow = slow.next
        fast = fast.next.next

    return slow
