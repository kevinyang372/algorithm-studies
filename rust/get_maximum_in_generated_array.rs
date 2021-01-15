impl Solution {
    pub fn get_maximum_generated(n: i32) -> i32 {
        let mut num = vec![0; n as usize + 1];
        let mut maximum = 0;
        
        if n >= 1 {
            num[1] = 1;
            maximum = 1;
        }
        
        for l in 2..n as usize + 1 {
            if l % 2 == 0 {
                num[l] = num[l / 2];
            } else {
                let i = (l - 1) / 2;
                num[l] = num[i] + num[i + 1];
            }
            if num[l] > num[maximum] {
                maximum = l;
            }
        }
        
        num[maximum]
    }
}