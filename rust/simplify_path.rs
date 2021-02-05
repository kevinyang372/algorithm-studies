impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut final_path = vec![];
        let mut ans = "/".to_string();
        
        for s in path.split("/") {
            if s.len() > 0 && s != "." {
                if s == ".." && final_path.len() > 0 {
                    final_path.pop();
                } else if s != ".." {
                    final_path.push(s);
                }
            }
        }
        
        ans.push_str(&final_path.join("/"));
        ans
    }
}