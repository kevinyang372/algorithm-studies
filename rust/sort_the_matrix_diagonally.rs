impl Solution {
    pub fn diagonal_sort(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
        let mut res = vec![vec![0; mat[0].len()]; mat.len()];
        
        for i in 0..mat.len() {
            let mut v = Vec::new();
            let mut y = 0;
            let mut x = i;
            
            while x < mat.len() && y < mat[0].len() {
                v.push(&mat[x][y]);
                x += 1;
                y += 1;
            }
            
            v.sort();
            x = i;
            y = 0;
            let mut count = 0;
            
            while x < mat.len() && y < mat[0].len() {
                res[x][y] = *v[count];
                x += 1;
                y += 1;
                count += 1;
            }
        }
        
        for j in 0..mat[0].len() {
            let mut v = Vec::new();
            let mut y = j;
            let mut x = 0;
            
            while x < mat.len() && y < mat[0].len() {
                v.push(&mat[x][y]);
                x += 1;
                y += 1;
            }
            
            v.sort();
            x = 0;
            y = j;
            let mut count = 0;
            
            while x < mat.len() && y < mat[0].len() {
                res[x][y] = *v[count];
                x += 1;
                y += 1;
                count += 1;
            }
        }
        
        res
    }
}