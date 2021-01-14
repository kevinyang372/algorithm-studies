use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn merge_trees(t1: Option<Rc<RefCell<TreeNode>>>, t2: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        
        if t1.is_none() && t2.is_none() {
            return None;
        }
        
        let mut node = match (&t1, &t2) {
            (Some(t1), Some(t2)) => TreeNode::new(t1.borrow().val + t2.borrow().val),
            (None, Some(t2)) => TreeNode::new(t2.borrow().val),
            (Some(t1), None) => TreeNode::new(t1.borrow().val),
            (None, None) => TreeNode::new(-1)
        };
        
        
        node.left = match(&t1, &t2) {
            (Some(t1), Some(t2)) => Self::merge_trees(t1.borrow().left.clone(), t2.borrow().left.clone()),
            (None, Some(t2)) => Self::merge_trees(None, t2.borrow().left.clone()),
            (Some(t1), None) => Self::merge_trees(t1.borrow().left.clone(), None),
            (None, None) => Some(Rc::new(RefCell::new(TreeNode::new(-1))))
        };
        node.right = match(&t1, &t2) {
            (Some(t1), Some(t2)) => Self::merge_trees(t1.borrow().right.clone(), t2.borrow().right.clone()),
            (None, Some(t2)) => Self::merge_trees(None, t2.borrow().right.clone()),
            (Some(t1), None) => Self::merge_trees(t1.borrow().right.clone(), None),
            (None, None) => Some(Rc::new(RefCell::new(TreeNode::new(-1))))
        };
        
        Some(Rc::new(RefCell::new(node)))
    }
}