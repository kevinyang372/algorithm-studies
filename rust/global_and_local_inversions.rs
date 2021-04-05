impl Solution {
    pub fn is_ideal_permutation(a: Vec<i32>) -> bool {
        let mut a = a;

        for (i, x) in a.iter().enumerate() {
            if (i as i32 - *x).abs() > 1 {
                return false;
            }
        }
        
        true
    }
}