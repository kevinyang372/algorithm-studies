impl Solution {
    pub fn merge_two_lists(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head = ListNode::new(0);
        let mut current = &mut dummy_head;
        
        let mut p = l1;
        let mut q = l2;
        
        while p != None && q != None {
            
            let p_node = p.take();
            let q_node = q.take();
            
            if let (Some(mut l1_head), Some(mut l2_head)) = (p_node, q_node) {
                if l1_head.val < l2_head.val {
                    p = l1_head.next.take();
                    q = Some(l2_head);
                    current.next = Some(l1_head);
                } else {
                    q = l2_head.next.take();
                    p = Some(l1_head);
                    current.next = Some(l2_head);
                }   
            }
            
            current = current.next.as_mut().unwrap();
        }
        
        if p != None {
            current.next = p;
        } else {
            current.next = q;
        }
        
        dummy_head.next
    }
}