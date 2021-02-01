impl Solution {
    pub fn hammingWeight (n: u32) -> i32 {
        let mut count = 0;
        let mut mask = 1;
        
        for _ in 0..32 {
            if (n & mask) != 0 {
                count += 1;
            }
            mask <<= 1;
        }
        
        count
    }
}