impl Solution {
    pub fn broken_calc(x: i32, y: i32) -> i32 {
        let mut res = 0;
        let mut x = x;
        let mut y = y;
        
        while x != y {
            if x > y {
                x -= 1;                
            } else if y % 2 == 1 {
                y += 1;
            } else {
                y /= 2;
            }
            res += 1;
        }
        
        res
    }
}