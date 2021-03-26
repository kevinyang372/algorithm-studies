use std::collections::HashMap;
impl Solution {
    pub fn word_subsets(a: Vec<String>, b: Vec<String>) -> Vec<String> {
        let count = |s: &str| {
            let mut m = vec![0; 26];
            s.chars().for_each(|w| m[w as usize - 'a' as usize] += 1);
            m
        };
        
        let b_count = b.into_iter().map(|bs| count(&bs)).fold([0; 26], |mut bm, m| {
            m.iter().enumerate().for_each(|(i, &n)| bm[i] = bm[i].max(n));
            bm
        });
        
        a.into_iter().map(|m| (count(&m), m)).filter(|(mc, _)|
            mc.iter().enumerate().all(|(i, &n)| b_count[i] <= n)
        ).map(|(_, m)| m).collect()
    }
}