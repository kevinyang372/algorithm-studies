impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n == 0 { return 0; }
        if n == 1 { return 1; }
        
        (2..n + 1).fold((0i32, 1i32), |(n0, n1), _| (n1, n0 + n1)).1
    }
}