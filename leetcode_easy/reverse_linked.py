def reverseList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if not head:
        return None

    pre = None
    cur = head

    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    return pre
