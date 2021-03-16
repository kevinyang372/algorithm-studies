impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let mut cash = 0i32;
        let mut hold: Option<i32> = None;
        
        for price in prices {
            cash = cash.max(hold.unwrap_or(-price) + price - fee);
            hold = Some(hold.unwrap_or(-price).max(cash - price));
        }
        
        cash
    }
}