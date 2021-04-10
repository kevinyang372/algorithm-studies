impl Solution {
    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        let h = matrix.len();
        let w = matrix[0].len();
        
        let mut dp: Vec<Vec<i32>> = vec![vec![-1; w]; h];
        
        fn dfs(mat: &Vec<Vec<i32>>, i: usize, j: usize, d: &mut Vec<Vec<i32>>) -> i32 {
            if d[i][j] < 0 {
                let mut mx: i32 = 0;
                let direction: Vec<i32> = vec![1, 0, -1, 0, 1];
                
                let h = d.len();
                let w = d[0].len();
                
                for ind in 1..direction.len() {
                    let di: usize = (i as i32 + direction[ind - 1]) as usize;
                    let dj: usize = (j as i32 + direction[ind]) as usize;
                    
                    let temp: i32 = if di >= 0 && di < h && dj >= 0 && dj < w && mat[di][dj] > mat[i][j] { dfs(mat, di, dj, d) + 1 } else { 0 };
                    mx = mx.max(temp);
                }
                
                d[i][j] = mx;
            }
            
            d[i][j]
        }
        
        let mut res = 0i32;
        for ii in 0..h {
            for jj in 0..w {
                res = res.max(dfs(&matrix, ii, jj, &mut dp));
            }
        }
        
        res + 1
    }
}