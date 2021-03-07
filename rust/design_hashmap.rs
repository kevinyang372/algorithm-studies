const TABLE_SIZE: usize = 1000;

struct MyHashMap {
    table: Vec<Vec<(i32, i32)>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashMap {

    /** Initialize your data structure here. */
    fn new() -> Self {
        Self {
            table: vec![vec![]; TABLE_SIZE],
        }
    }
    
    /** value will always be non-negative. */
    fn put(&mut self, key: i32, value: i32) {
        let hashed = key as usize % TABLE_SIZE;
        
        for j in 0..self.table[hashed].len() {
            if self.table[hashed][j].0 == key {
                self.table[hashed][j].1 = value;
                return;
            }
        }
        
        self.table[hashed].push((key, value));
    }
    
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    fn get(&self, key: i32) -> i32 {
        let hashed = key as usize % TABLE_SIZE;
        
        for j in 0..self.table[hashed].len() {
            if self.table[hashed][j].0 == key {
                return self.table[hashed][j].1;
            }
        }
        
        -1
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    fn remove(&mut self, key: i32) {
        let hashed = key as usize % TABLE_SIZE;
        
        for j in 0..self.table[hashed].len() {
            if self.table[hashed][j].0 == key {
                self.table[hashed].remove(j);
                return;
            }
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap::new();
 * obj.put(key, value);
 * let ret_2: i32 = obj.get(key);
 * obj.remove(key);
 */