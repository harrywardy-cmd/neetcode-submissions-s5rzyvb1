# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#class Solution:
    #def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Start traversing from the head of the linked list
        #curr = head

        # Store visited nodes in a set
        # If we encounter the same node again, a cycle exists
        #seen = set()

        # Traverse the linked list until we reach the end
        #while curr:
            # If the current node has already been visited,
            # we've found a cycle
            #if curr in seen:
                #return True

            # Mark the current node as visited
            #seen.add(curr)

            # Move to the next node
            #curr = curr.next

        # If we reach None, the list ends normally,
        # so there is no cycle
        #return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the head of the linked list
        # Slow moves one step at a time, fast moves two steps at a time
        slow, fast = head, head

        # Continue while there are enough nodes for the fast pointer
        while fast and fast.next:
            # Move the slow pointer forward by one node
            slow = slow.next

            # Move the fast pointer forward by two nodes
            fast = fast.next.next

            # If the two pointers meet, a cycle exists
            if slow == fast:
                return True

        # If the fast pointer reaches the end of the list,
        # there is no cycle
        return False
        