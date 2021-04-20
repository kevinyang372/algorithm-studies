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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut DUMMY_HEAD = Box::new(ListNode {val: 0, next: head } );
        let mut len = 0;
        {
            let mut temp = DUMMY_HEAD.as_ref();
            while temp.next.is_some() {
                len += 1;
                temp = temp.next.as_ref().unwrap();
            }
        }
        
        let idx = len - n;
        {
            let mut temp = DUMMY_HEAD.as_mut();
            
            for _ in 0..idx {
                temp = temp.next.as_mut().unwrap();
            }
            
            temp.next = temp.next.as_mut().unwrap().next.take();
        }
        
        DUMMY_HEAD.next
    }
}