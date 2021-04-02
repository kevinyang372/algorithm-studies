impl Solution {
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        let svec: Vec<(i32, i32)> = strs.iter().map(|s| s.chars().fold(
            (0, 0), |c, x| if x == '1' { (c.0, c.1 + 1) } else { (c.0 + 1, c.1) }
        )).collect();
        
        let m = m as usize;
        let n = n as usize;
        
        let mut res: Vec<Vec<i32>> = vec![vec![0; n + 1]; m + 1];
        
        for (mx, nx) in svec {
            let mx = mx as usize;
            let nx = nx as usize;
            for i in (mx..m + 1).rev() {
                for j in (nx..n + 1).rev() {
                    res[i][j] = res[i][j].max(res[i - mx][j - nx] + 1);
                }    
            }
        }
        
        *res.last().unwrap().last().unwrap()
    }
}