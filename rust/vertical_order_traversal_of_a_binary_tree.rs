use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn vertical_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut d = HashMap::new();
        
        Self::traverse(root, 0, 0, &mut d);
        let mut i = d.keys().min().unwrap().clone();
        
        let mut result = vec![];
        while d.contains_key(&i) {
            let mut value = d.get_mut(&i).unwrap();
            value.sort();
            
            let mut temp = vec![];
            
            for (_, val) in value {
                temp.push(*val);
            }
            
            result.push(temp);
            i += 1;
        }
        
        result
    }
    
    pub fn traverse(node: Option<Rc<RefCell<TreeNode>>>, x: i32, y: u32, d: &mut HashMap<i32, Vec<(u32, i32)>>) {
        if let Some(n) = node {
            match d.get_mut(&x) {
                Some(v) => v.push((y, n.borrow().val)),
                _ => (),
            }
            
            if !d.contains_key(&x) {
                d.insert(x, vec![(y, n.borrow().val)]);
            }
            
            Self::traverse(n.borrow().left.clone(), x - 1, y + 1, d);
            Self::traverse(n.borrow().right.clone(), x + 1, y + 1, d);
        }
    }
}