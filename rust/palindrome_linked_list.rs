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
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        let mut vals = Vec::new();
        let mut head = head;
        
        while head.is_some() {
            let node = head.unwrap();
            vals.push(node.val);
            
            head = node.next;
        }
        
        let range: Vec<usize> = (0..vals.len() / 2).collect();
        range.iter().all(|x| vals[*x] == vals[vals.len() - *x - 1])
    }
}