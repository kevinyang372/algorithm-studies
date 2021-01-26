// TLE
use std::collections::HashSet;

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let mut cost = 0;
        let dir: [i32; 5] = [0, -1, 0, 1, 0];
        
        let len_x = heights.len() as i32;
        let len_y = heights[0].len() as i32;
        
        if len_x == 1 && len_y == 1 { return cost; }
        
        loop {
            let mut stack = vec![(0, 0)];
            let mut visited = HashSet::<(i32, i32)>::new();
            
            while stack.len() > 0 {
                let (x, y) = stack.pop().unwrap();
                
                for k in 0..4 {
                    let new_x = x + dir[k];
                    let new_y = y + dir[k + 1];
                    
                    if 0 <= new_x && new_x < len_x && 0 <= new_y && new_y < len_y {
                        let diff = (heights[new_x as usize][new_y as usize] - heights[x as usize][y as usize]).abs();
                        if diff <= cost && !visited.contains(&(new_x, new_y)) {
                            if new_x == len_x - 1 && new_y == len_y - 1 { return cost; }
                            stack.push((new_x, new_y));
                            visited.insert((new_x, new_y));
                        }
                    }
                }
            }
            
            cost += 1;
        }
        
        0
    }
}

// Dijkstra
use std::collections::BinaryHeap;
use std::cmp::max;

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let mut cost = 0;
        let dir: [i32; 5] = [0, -1, 0, 1, 0];
        
        let len_x = heights.len() as i32;
        let len_y = heights[0].len() as i32;
        
        if len_x == 1 && len_y == 1 { return cost; }
        
        let mut dist = vec![vec![std::i32::MAX; len_y as usize]; len_x as usize];
        let mut heap = BinaryHeap::<(i32, i32, i32)>::new();
        
        heap.push((0, 0, 0));
        dist[0][0] = 0;
        
        while heap.len() > 0 {
            let (d, x, y) = heap.pop().unwrap();
            
            if x == len_x - 1 && y == len_y - 1 {
                return -d;
            }

            for k in 0..4 {
                let new_x = x + dir[k];
                let new_y = y + dir[k + 1];

                if 0 <= new_x && new_x < len_x && 0 <= new_y && new_y < len_y {
                    let diff = max(-d, (heights[new_x as usize][new_y as usize] - heights[x as usize][y as usize]).abs());
                    if diff < dist[new_x as usize][new_y as usize]  {
                        heap.push((-diff, new_x, new_y));
                        dist[new_x as usize][new_y as usize] = diff
                    }
                }
            }
        }
        
        0
    }
}