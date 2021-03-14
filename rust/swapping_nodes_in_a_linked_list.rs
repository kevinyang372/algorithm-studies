impl Solution {
    pub fn swap_nodes(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut arr = Vec::new();
        let mut head = head;
        
        while head.is_some() {
            let node = *head.unwrap();
            arr.push(node.val);
            head = node.next;
        }
        
        let len = arr.len();
        let k = k as usize;
        let temp = arr[k - 1];
        arr[k - 1] = arr[len - k];
        arr[len - k] = temp;
        
        let mut i = (len - 1) as i32;
        let mut new_head = None;
        
        while i >= 0 {
            let mut node = ListNode::new(arr[i as usize]);
            node.next = new_head;
            new_head = Some(Box::new(node));
            i -= 1;
        }
        
        new_head
    }
}