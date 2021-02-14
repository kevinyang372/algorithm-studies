impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let mut colors: Vec<i32> = vec![0; graph.len()];
        
        for ind in 0..graph.len() {
            if colors[ind] == 0 {
                let mut stack = vec![ind];
                colors[ind] = 1;
                
                while stack.len() > 0 {
                    let curr = stack.pop().unwrap() as usize;
                    
                    for node in &graph[curr] {
                        let node = *node as usize;
                        if colors[node] == colors[curr] {
                            return false;
                        } else if colors[node] != -colors[curr] {
                            colors[node] = -colors[curr];
                            stack.push(node)
                        }
                    }
                }
            }
        }
        
        true
    }
}