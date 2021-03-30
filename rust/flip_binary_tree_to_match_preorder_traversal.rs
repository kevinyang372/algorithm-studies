// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn flip_match_voyage(root: Option<Rc<RefCell<TreeNode>>>, voyage: Vec<i32>) -> Vec<i32> {
        let node = root.unwrap();
        let mut stack = vec![];
        let mut res = vec![];
        
        stack.push(node);
        let mut i = 0;
        
        while stack.len() > 0 && i < voyage.len() {
            let n = stack.pop().unwrap();
            
            if n.borrow().val != voyage[i] {
                return vec![-1];
            }
            
            let left_node = n.borrow().left.clone();
            let right_node = n.borrow().right.clone();
            
            let left_val: i32 = if let Some(ln) = &left_node {
                ln.borrow().val
            } else {
                -1
            };
            
            let right_val: i32 = if let Some(rn) = &right_node {
                rn.borrow().val
            } else {
                -1
            };
            
            if left_val < 0 && right_val < 0 || i + 1 == voyage.len() {
                i += 1;
                continue;
            }
            
            match voyage[i + 1] {
                _ if voyage[i + 1] == left_val || (voyage[i + 1] == right_val && left_val < 0) => {
                    if right_node.is_some() { stack.push(right_node.unwrap()); }
                    if left_node.is_some() { stack.push(left_node.unwrap()); }
                },
                _ if voyage[i + 1] == right_val => {
                    if left_node.is_some() { stack.push(left_node.unwrap()); }
                    if right_node.is_some() { stack.push(right_node.unwrap()); }
                    res.push(n.borrow().val);
                },
                _ => {
                    return vec![-1];
                }
            }
            
            i += 1;
        }
        
        res
    }
}