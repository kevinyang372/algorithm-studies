impl Solution {
    pub fn add_two_numbers(l1: Option < Box < ListNode >>, l2: Option < Box < ListNode>>) -> Option < Box < ListNode >> {
        let mut carry_over = 0;
        let mut dummy_head = ListNode:: new(0);
        let mut current = &mut dummy_head;

        let mut p = l1;
        let mut q = l2;

        while p != None | | q != None {
            let temp_sum = match(& p, & q) {
                (Some(l1), Some(l2)) = > l1.val + l2.val + carry_over,
                (Some(l1), None) = > l1.val + carry_over,
                (None, Some(l2)) = > l2.val + carry_over,
                (None, None) = > carry_over
            };

            current.next = Some(Box:: new(ListNode: : new(temp_sum % 10)));
            current = current.next.as_mut().unwrap();

            carry_over = temp_sum / 10;

            if p != None {
                p = p.unwrap().next;
            }

            if q != None {
                q = q.unwrap().next;
            }
        }

        if carry_over > 0 {
            current.next = Some(Box: : new(ListNode: : new(carry_over)));
        }

        dummy_head.next
    }
}
