impl Solution {
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {
        let mut triangle = triangle;
        
        for idx in 1..triangle.len() {
            for i in 0..triangle[idx].len() {
                if i < 1 {
                    triangle[idx][i] = triangle[idx - 1][i] + triangle[idx][i];
                } else if i == triangle[idx].len() - 1 {
                    triangle[idx][i] = triangle[idx - 1][i - 1] + triangle[idx][i];
                } else {
                    triangle[idx][i] = triangle[idx - 1][i].min(triangle[idx - 1][i - 1]) + triangle[idx][i];
                }
            }
        }
        
        *triangle.last().unwrap().iter().min().unwrap()
    }
}