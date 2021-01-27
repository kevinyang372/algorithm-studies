impl Solution {
    pub fn concatenated_binary(n: i32) -> i32 {
        let to_mod = 1_000_000_007;
        let mut result: u64 = 0;
        
        for i in 1..=n as u64 {
            // 64 - i.leading_zeros() gives us the length of i's bits
            result <<= 64 - i.leading_zeros();
            result = (result + i) % to_mod;
        }
        
        result as i32
    }
}