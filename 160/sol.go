func getIntersectionNode(headA, headB *ListNode) *ListNode {
	a, b := Len(headA), Len(headB)
	if a > b {
		b, a = a, b
		headB, headA = headA, headB
	}
	for a != b {
		headB = headB.Next
		b--
	}
	for headA != headB {
		headA = headA.Next
		headB = headB.Next
	}
	return headA
}