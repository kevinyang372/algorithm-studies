// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        let mut less_head = Box::new(ListNode::new(0));
        let mut more_head = Box::new(ListNode::new(0));
        
        let mut less = less_head.as_mut();
        let mut more = more_head.as_mut();
        
        let mut head = head;
        
        while let Some(node) = head {
            if node.val < x {
                less.next = Some(Box::new(ListNode::new(node.val)));
                less = less.next.as_mut().unwrap();
            } else {
                more.next = Some(Box::new(ListNode::new(node.val)));
                more = more.next.as_mut().unwrap();
            }
            
            head = node.next;
        }
        
        less.next = more_head.next;
        less_head.next
    }
}