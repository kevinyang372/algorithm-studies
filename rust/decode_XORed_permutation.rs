impl Solution {
    pub fn decode(encoded: Vec<i32>) -> Vec<i32> {
        let x = (1..=encoded.len() + 1).fold(0i32, |x, t| x ^ t as i32);
        let y = (1..encoded.len()).fold(0, |y, t| if t % 2 == 1 { y ^ encoded[t] } else { y });
        
        let mut start = x ^ y;
        let mut res = vec![start];
        
        for e in encoded {
            res.push(e ^ start);
            start ^= e;
        }
        
        res
    }
}