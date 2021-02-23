impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        fn binary_search(v: &Vec<i32>, t: i32) -> bool {
            let range = 0..v.len();
            match v.binary_search(&t) {
                Ok(range) => true,
                _ => false,
            }
        }
        
        for i in 0..matrix.len() {
            if matrix[i][0] <= target && matrix[i][matrix[i].len() - 1] >= target && binary_search(&matrix[i], target) {
                return true;
            }
        }
        
        false
    }
}