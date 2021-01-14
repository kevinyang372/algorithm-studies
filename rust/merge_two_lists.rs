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


// Alternative - create new node
impl Solution {
    pub fn merge_two_lists(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy_head = ListNode::new(0);
        let mut current = &mut dummy_head;
        
        let mut p = l1;
        let mut q = l2;
        
        while p != None && q != None {
            
            let mut p_val = p.as_mut().unwrap().val;
            let mut q_val = q.as_mut().unwrap().val;
            
            if p_val < q_val {
                current.next = Some(Box::new(ListNode::new(p_val)));
                p = p.unwrap().next;
            } else {
                current.next = Some(Box::new(ListNode::new(q_val)));
                q = q.unwrap().next;
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