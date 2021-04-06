impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        let range: Vec<i32> = (0..n / 2).collect();
        range.iter().fold(0, |x, y| x + n - (2 * y + 1))
    }
}