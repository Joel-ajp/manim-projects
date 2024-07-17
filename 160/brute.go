func getIntersectionNode(headA, headB *ListNode) *ListNode {
	for headA != nil {
		for headB != nil {
			tmp := headB
			if tmp == headA {
				return tmp
			} else {
				headB = headB.Next
			}
		}
	}
	return nil
}
