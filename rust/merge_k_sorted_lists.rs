use std::collections::BinaryHeap;
use std::cmp::{Ordering, Reverse};

impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        if lists.len() == 0 { return None; }
        
        let mut h = BinaryHeap::new();
        let mut dummy_head = Some(Box::new(ListNode::new(0)));
        let mut curr = dummy_head.as_mut().unwrap();
        
        for l in lists {
            match l {
                Some(node) => h.push(Reverse(node)),
                _ => ()
            };
        }
        
        while h.len() > 0 {
            if let Some(Reverse(mut next_node)) = h.pop() {
                curr.next = Some(Box::new(ListNode::new(next_node.val)));
                curr = curr.next.as_mut().unwrap();
                
                match next_node.next {
                    Some(next) => h.push(Reverse(next)),
                    _ => ()
                };
            }
        }
        
        dummy_head.unwrap().next
    }
}

impl PartialOrd for ListNode {
    fn partial_cmp(&self, other: &ListNode) -> Option<Ordering> {
        self.val.partial_cmp(&other.val)
    }
}

impl Ord for ListNode {
    fn cmp(&self, other: &ListNode) -> Ordering {
        self.val.cmp(&other.val)
    }
}