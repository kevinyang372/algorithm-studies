impl Solution {
    pub fn maximum_score(a: i32, b: i32, c: i32) -> i32 {
        let mut a = a;
        let mut b = b;
        let mut c = c;
        
        let mut points = 0;
        while (a > 0 && b > 0) || (a > 0 && c > 0) || (b > 0 && c > 0) {
            if a >= b && c >= b {
                a -= 1;
                c -= 1;
            } else if b >= a && c >= a {
                b -= 1;
                c -= 1;
            } else {
                a -= 1;
                b -= 1;
            }
            points += 1;
        }
        
        points
    }
}