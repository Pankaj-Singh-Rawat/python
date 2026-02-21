class MyLinkedList:
    def __init__(self):
        self.head = None

    # Add at the very beginning
    def addAtHead(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    # Add at the very end
    def addAtTail(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:  # Traverse to the end
            curr = curr.next
        curr.next = ListNode(val)

    # Delete by index (Classic LeetCode task)
    def deleteAtIndex(self, index):
        if not self.head: return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        # Stop one node BEFORE the one we want to delete
        for _ in range(index - 1):
            if not curr.next: return
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next