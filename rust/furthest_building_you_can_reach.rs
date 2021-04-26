use std::collections::BinaryHeap;
impl Solution {
    pub fn furthest_building(heights: Vec<i32>, bricks: i32, ladders: i32) -> i32 {
        let mut b: BinaryHeap<i32> = BinaryHeap::new();
        let mut sum: i32 = 0;
        
        for i in 1..heights.len() {
            if heights[i] > heights[i - 1] {
                let diff = heights[i] - heights[i - 1];
                
                if ladders != 0 && b.len() as i32 == ladders && -b.peek().unwrap() < diff {
                    sum += -b.pop().unwrap();
                    b.push(-diff);
                } else if ladders == 0 || b.len() as i32 == ladders {
                    sum += diff;
                } else {
                    b.push(-diff);
                }
                
                if sum > bricks {
                    return (i - 1) as i32;
                }
            }
        }
        
        (heights.len() - 1) as i32
    }
}