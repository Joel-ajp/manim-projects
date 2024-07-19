func Len(head *ListNode) int {
	l := 0
	for ; head != nil; head = head.Next {
		l++
	}
	return l
}