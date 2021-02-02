use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn trim_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root {
            let node_val = node.borrow().val;
            
            if node_val < low {
                return Self::trim_bst(node.borrow().right.clone(), low, high);
            } else if node_val > high {
                return Self::trim_bst(node.borrow().left.clone(), low, high);
            } else {
                let mut new_node = TreeNode::new(node_val);
                
                new_node.left = Self::trim_bst(node.borrow().left.clone(), low, high);
                new_node.right = Self::trim_bst(node.borrow().right.clone(), low, high);
                
                return Some(Rc::new(RefCell::new(new_node)));
            }
        }
        
        None
    }
}