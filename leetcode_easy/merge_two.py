class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node11 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(4)
node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)

node11.next = node12
node12.next = node13
node21.next = node22
node22.next = node23


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if not list1 and not list2:
        return None

    head = ListNode(-1)
    cur = head

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next

    cur.next = list1 if list1 else list2

    return head.next


def traverse(head):
    cur = head
    while cur:
        print(cur.val, end="->")
        cur = cur.next
    print("null")


traverse(node11)
traverse(node21)
traverse(mergeTwoLists(node11, node21))
