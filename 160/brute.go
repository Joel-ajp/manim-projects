func getIntersectionNode(headA, headB *ListNode) *ListNode {
	for headA != nil {
		tmp := headB
		for tmp != nil {
			if tmp == headA {
				return tmp
			} else {
				tmp = tmp.Next
			}
		}
		headA = headA.Next
	}
	return nil
}