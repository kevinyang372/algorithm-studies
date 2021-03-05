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
use std::collections::VecDeque;

impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut v = VecDeque::new();
        let mut level: Vec<(i64, usize)> = vec![];
        v.push_back((1, root.unwrap()));
        
        while v.len() > 0 {
            let (l, node) = v.pop_front().unwrap();
            
            if l > level.len() {
                level.push((node.borrow().val as i64, 1));
            } else {
                level[l - 1].0 += node.borrow().val as i64;
                level[l - 1].1 += 1;
            }
            
            let left = &node.borrow().left.clone();
            let right = &node.borrow().right.clone();
            
            if let Some(left_node) = left {
                v.push_back((l + 1, left_node.clone()));               
            }
            
            if let Some(right_node) = right {
                v.push_back((l + 1, right_node.clone()));               
            }
        }
        
        level.into_iter().map(|x| x.0 as f64 / x.1 as f64).collect()
    }
}