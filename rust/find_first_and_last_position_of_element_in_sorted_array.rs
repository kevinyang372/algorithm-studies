use std::cmp::Ordering::{Less, Greater};

impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        fn search(nums: &Vec<i32>, target: i32, lesser: bool) -> i32 {
            let mut i = 0;
            let mut j = nums.len();

            while i < j {
                let mid = (i + j) / 2;

                if lesser {
                    if nums[mid] > target {
                        j = mid;
                    } else {
                        i = mid + 1;
                    }
                } else {
                    if nums[mid] < target {
                        i = mid + 1;
                    } else {
                        j = mid;
                    }
                }
            }

            if lesser { (i - 1) as i32 } else { i as i32 }
        }
        
        let l = search(&nums, target, false);
        let r = search(&nums, target, true);
        
        if l > r {
            vec![-1, -1]
        } else {
            vec![l, r]
        }
    }
}