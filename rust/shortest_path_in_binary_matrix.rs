use std::collections::BinaryHeap;

impl Solution {
    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        if grid[0][0] == 1 {
            return -1;
        } else if grid.len() == 1 && grid[0].len() == 1 {
            return 1;
        }
        
        let mut h: BinaryHeap<(i32, usize, usize)> = BinaryHeap::new();
        let mut d = vec![vec![std::i32::MAX; grid[0].len()]; grid.len()];
        
        let len_x = grid.len();
        let len_y = grid[0].len();
        
        h.push((-1, 0, 0));
        d[0][0] = 1;
        
        while h.len() > 0 {
            let (c, x, y) = h.pop().unwrap();
            
            for dx in 0..=2 {
                let new_x = dx + x - 1;
                for dy in 0..=2 {
                    let new_y = dy + y - 1;
                    
                    if 0 <= new_x && new_x < len_x && 0 <= new_y && new_y < len_y && grid[new_x][new_y] == 0 {
                        let new_c = -c + 1;
                        
                        if new_x == len_x - 1 && new_y == len_y - 1 {
                            return new_c;
                        }
                        
                        if new_c < d[new_x][new_y] {
                            d[new_x][new_y] = new_c;
                            h.push((-new_c, new_x, new_y));
                        }
                    }
                }
            }
        }
        
        -1
    }
}