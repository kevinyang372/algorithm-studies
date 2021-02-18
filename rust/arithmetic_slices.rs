impl Solution {
    pub fn number_of_arithmetic_slices(a: Vec<i32>) -> i32 {
        if a.len() < 3 { return 0; }
        let mut count = 1;
        let mut diff = a[1] - a[0];
        let mut res = 0;
        
        for i in 2..a.len() {
            if a[i] - a[i - 1] == diff {
                count += 1;
            } else if count > 1 {
                res += count * (count -1) / 2;
                count = 1;
                diff = a[i] - a[i - 1];
            } else {
                count = 1;
                diff = a[i] - a[i - 1];
            }
        }
        
        if count > 1 {
            res += count * (count -1) / 2;
        }
        
        res as i32
    }
}