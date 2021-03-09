use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn add_one_row(root: Option<Rc<RefCell<TreeNode>>>, v: i32, d: i32) -> Option<Rc<RefCell<TreeNode>>> {
        Self::traverse(root, v, d, true)
    }
    
    fn traverse(node: Option<Rc<RefCell<TreeNode>>>, v: i32, d: i32, is_left: bool) -> Option<Rc<RefCell<TreeNode>>> {
        if d == 1 {
            let mut new_node = TreeNode::new(v);

            if is_left {
                new_node.left = node;
            } else {
                new_node.right = node;
            }

            return Some(Rc::new(RefCell::new(new_node)));
        }
        
        if let Some(n) = node {
            let left_node = Self::traverse(n.borrow().left.clone(), v, d - 1, true);
            let right_node = Self::traverse(n.borrow().right.clone(), v, d - 1, false);
            
            let mut new_node = TreeNode::new(n.borrow().val);
            new_node.left = left_node;
            new_node.right = right_node;
            
            return Some(Rc::new(RefCell::new(new_node)));
        }
        
        None
    }
}