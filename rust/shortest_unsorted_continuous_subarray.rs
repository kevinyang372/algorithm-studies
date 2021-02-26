impl Solution {
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
        let mut nums2 = nums.clone();
        nums2.sort();
        
        let mut st: i32 = -1;
        let mut ed: i32 = -2;
        
        for i in 0..nums.len() {
            if nums[i] != nums2[i] {
                if st < 0 {
                    st = i as i32;
                }
                ed = i as i32;
            }
        }
        
        return ed - st + 1;
    }
}