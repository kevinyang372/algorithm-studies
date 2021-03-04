use std::collections::VecDeque;
impl Solution {
    pub fn highest_peak(is_water: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = is_water.len();
        let m = is_water[0].len();
        let mut water: VecDeque<(usize, usize, i32)> = VecDeque::new();
        let mut res: Vec<Vec<i32>> = vec![vec![-1; m]; n];
        let direction: Vec<i32> = vec![0, 1, 0, -1, 0];
        
        for i in 0..n {
            for j in 0..m {
                if is_water[i][j] == 1 {
                    res[i][j] = 0;
                    water.push_back((i, j, 0));
                }
            }
        }
        
        while water.len() > 0 {
            let (x, y, h) = water.pop_front().unwrap();
            
            for i in 0..direction.len() - 1 {
                let nx = x as i32 + &direction[i];
                let ny = y as i32 + &direction[i + 1];
                
                if 0 <= nx && nx < n as i32 && 0 <= ny && ny < m as i32 && res[nx as usize][ny as usize] < 0 {
                    res[nx as usize][ny as usize] = h + 1;
                    water.push_back((nx as usize, ny as usize, h + 1));
                }
            }
        }
        
        res
    }
}