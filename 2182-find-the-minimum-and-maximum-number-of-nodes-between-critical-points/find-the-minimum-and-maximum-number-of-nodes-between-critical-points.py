# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None or head.next.next is None:
            return[-1,-1]
        prev = head
        curr = head.next
        pos = 1
        first = -1
        last = -1
        min_distance = float('inf')
        max_distance = 0

        while curr.next is not None:
            next_node = curr.next
            is_critical = (
                (curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)
            )
            if is_critical:
                if first == -1:
                    first = pos
                else:
                    distance = pos - last
                    min_distance = min(min_distance, distance)
                    max_distance = max(max_distance, pos - first)
                last = pos
            prev = curr
            curr = curr.next
            pos += 1
        if first == -1 or first == last:
            return [-1,-1]
        return [min_distance, max_distance]

        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        