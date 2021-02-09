use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn convert_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let (_, node) = Self::post_order_traversal(root, 0);
        node
    }
    
    fn post_order_traversal(node: Option<Rc<RefCell<TreeNode>>>, prev: i32) -> (i32, Option<Rc<RefCell<TreeNode>>>) {
        if let Some(n) = node {
            let (result, right_node) = Self::post_order_traversal(n.borrow().right.clone(), prev);
            let mut total = result + n.borrow().val;
            let mut current = TreeNode::new(total);
            current.right = right_node;
            let (result, left_node) = Self::post_order_traversal(n.borrow().left.clone(), total);
            current.left = left_node;
            return (result, Some(Rc::new(RefCell::new(current))));
        }
        
        (prev, None)
    }
}