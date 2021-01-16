use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let res = match (&root) {
            Some(root) => [Self::inorder_traversal(root.borrow().left.clone()), vec![root.borrow().val], Self::inorder_traversal(root.borrow().right.clone())].concat(),
            _ => vec![]
        };
        res
    }
}