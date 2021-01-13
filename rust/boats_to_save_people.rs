pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
    let mut p2 = Vec::new();
    
    for ele in people {
        p2.push(ele);
    }
    
    p2.sort();
    
    let mut i = 0;
    let mut j = p2.len() - 1;
    
    let mut count = 0;
    
    while i <= j {
        if p2[i] + p2[j] <= limit {
            i += 1;
        }
        if j == 0 {
            i += 1
        } else {
            j -= 1;   
        }
        count += 1;
    }
    count
}