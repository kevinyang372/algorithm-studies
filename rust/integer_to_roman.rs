impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        let val: [i32; 13] = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        
        let mut num = num;
        let mut i = 0;
        let mut res = "".to_string();
        
        while num > 0 {
            while val[i] > num {
                i += 1;
            }
            
            num -= val[i];
            res.push_str(symbol[i]);
        }
        
        res
    }
}