use std::i32;

impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let mut cash = 0i32;
        let mut hold = -5 * 10i32.pow(4);
        
        for price in prices {
            cash = cash.max(hold + price - fee);
            hold = hold.max(cash - price);
        }
        
        cash
    }
}