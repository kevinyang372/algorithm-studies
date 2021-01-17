impl Solution {
    pub fn count_vowel_strings(n: i32) -> i32 {
        fn count(n: i32, last_char: i32) -> i32 {
            if n == 0 { return 1; }
            let mut total_count = 0;
            for num in 0..last_char + 1 {
                total_count += count(n - 1, num);
            }
            total_count
        }
        count(n, 4)
    }
}