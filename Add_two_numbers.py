#You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of
# their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1=[str(x) for x in my_generater(l1) ]
        list2=[str(x) for x in my_generater(l2)]
        list1=int("".join(list1[::-1]))
        list2=int("".join(list2[::-1]))
        list_last=str(list1+list2)#需要转换为str对象因为，int对象不可以迭代无法变回到list
        #list_last=list(list_last)
        list_last=list(map(int,list_last))#先map再list



        return  list_last




def my_generater(link_list):
    generator_list=link_list
    while generator_list:
        yield generator_list.val
        generator_list=generator_list.next

head=ListNode(1)
p1=ListNode(2)
p2=ListNode(3)
head.next=p1
p1.next=p2

head2=ListNode(1)
l1=ListNode(2)
l2=ListNode(3)
head2.next=l1
l1.next=l2

solution=Solution()
print(solution.addTwoNumbers(head,head2))


