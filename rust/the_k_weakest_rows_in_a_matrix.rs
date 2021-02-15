use std::collections::BinaryHeap;
impl Solution {
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut t: BinaryHeap<(i32, i32)> = BinaryHeap::new();
        
        for ind in 0..mat.len() {
            let val: i32 = mat[ind].iter().sum();
            t.push((val, ind as i32));
            
            if t.len() as i32 > k {
                t.pop();
            }
        }
        
        t.into_sorted_vec().into_iter().map(|x| x.1).collect()
    }
}