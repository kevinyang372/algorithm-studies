use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res = Vec::new();
        
        if let Some(node) = root {
            let mut d = VecDeque::new();
            d.push_back((0, node));
            
            while d.len() > 0 {
                if let Some((i, n)) = d.pop_front() {
                    match &n.borrow().left {
                        Some(node) => { d.push_back((i + 1, node.clone())) },
                        _ => (),
                    }
                    
                    match &n.borrow().right {
                        Some(node) => { d.push_back((i + 1, node.clone())) },
                        _ => (),
                    }
                    
                    if d.len() == 0 || d.front().unwrap().0 > i {
                        res.push(n.borrow().val);
                    }
                }
                
            }
        }
        
        res
    }
}