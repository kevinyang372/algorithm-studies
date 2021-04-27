impl Solution {
    pub fn is_power_of_three(n: i32) -> bool {
        if n == 1 { return true };
        if n > 0 && n % 3 == 0 {
            return Self::is_power_of_three(n / 3);
        }
        false
    }
}