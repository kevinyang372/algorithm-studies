// #[derive(Debug, PartialEq, Eq)]
// pub enum NestedInteger {
//   Int(i32),
//   List(Vec<NestedInteger>)
// }
struct NestedIterator {
    l: Vec<NestedInteger>,
    next_node: Option<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NestedIterator {

    fn new(nestedList: Vec<NestedInteger>) -> Self {
        let mut s = Self {
            l: nestedList.into_iter().rev().collect::<Vec<_>>(),
            next_node: None,
        };
        s.expand_next();
        s
    }
    
    fn next(&mut self) -> i32 {
        let res = self.next_node.unwrap();
        self.expand_next();
        res
    }
    
    fn has_next(&self) -> bool {
        self.next_node.is_some()
    }
    
    fn expand_next(&mut self) {
        while let Some(node) = self.l.pop() {
            match node {
                NestedInteger::Int(n) => {
                    self.next_node = Some(n);
                    return;
                },
                NestedInteger::List(l) => {
                    self.l.extend(l.into_iter().rev().collect::<Vec<_>>());
                }
            };
        }
        
        self.next_node = None;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * let obj = NestedIterator::new(nestedList);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */