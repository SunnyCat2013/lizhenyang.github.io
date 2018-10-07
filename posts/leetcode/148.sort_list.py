# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            first = head
            second = head.next
            if first.val <= second.val:
                return head
            else:
                second.next = first
                first.next = None
                return second
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        ln = n / 2
        rn = n - ln
        left = p = head
        k = 1
        pre_right = ListNode(None)
        while p:
            if k == rn:
                pre_right.next = head
            if k > rn:
                pre_right = pre_right.next
            p = p.next
            k += 1
        right = pre_right.next
        pre_right.next = None
        print('right')
        print_list(right)
        print('\n')
        print('left')
        print_list(left)
        print('\n')
        right = self.merge(right)
        left = self.merge(left)
        print('next -------------------------')
        print('right')
        print_list(right)
        print('\n')
        print('left')
        print_list(left)
        print('\n')
        pre_pre_head = ListNode(None)
        pre_head = ListNode(None)
        pre_pre_head.next = pre_head
        pre_head.next = None

        while left and right:
            print_list(pre_pre_head.next.next)
            if left.val <= right.val:
                pre_head.next = left
                left = left.next
                pre_head = pre_head.next
                pre_head.next = None
            else:
                pre_head.next = right
                right = right.next
                pre_head = pre_head.next
                pre_head.next = None

        pre_head.next = left if left else right

        return pre_pre_head.next.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge(head)


solver = Solution()

def print_list(head):
    while head:
        print '-> %d ' % head.val,
        head = head.next
    print('')
def return_list(array):
    pre_head = ListNode(None)
    head = ListNode(None)
    pre_head.next = head
    head.next = None
    for a in array:
        new_point = ListNode(a)
        head.next = new_point
        new_point.next = None
        head = head.next
    print(pre_head)
    return pre_head.next.next


def get_solution(array):
    print_list(solver.merge(return_list(array)))


# get_solution([1, 2, 4, 5])
get_solution([4,2,1,3])
