impl Solution {
    pub fn moves_to_stamp(stamp: String, target: String) -> Vec<i32> {
        let (stamp, mut target) = (stamp.into_bytes(), target.into_bytes());
        let check_pass = |s: &mut [u8], t: &Vec<u8>| {
            s.iter().zip(t.iter()).all(|(x, y)| *x == b'?' || x == y)
        };
        let mut res = vec![];
        
        while target.iter().any(|b| *b != b'?') {
            let mut replaced = false;
            for i in 0..target.len() - stamp.len() + 1 {
                let s = &mut target[i..i + stamp.len()];
                
                if !s.into_iter().all(|x| *x == b'?') && check_pass(s, &stamp) {
                    res.push(i as i32);
                    replaced = true;
                    s.iter_mut().for_each(|c| *c = b'?');
                    break;
                }
            }
            
            if !replaced || res.len() == 10 * target.len() { return vec![]; }
        }
        
        res.reverse();
        res
    }
}