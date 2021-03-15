use std::cell::RefCell;
use std::collections::hash_map::DefaultHasher;
use std::{
    collections::HashMap,
    hash::{Hash, Hasher},
};

#[derive(Default)]
struct Codec {
    map: RefCell<HashMap<String, String>>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Default::default()
    }
    
    // Encodes a URL to a shortened URL.
    fn encode(&self, longURL: String) -> String {
        let hashed = {
            let mut s = DefaultHasher::new();
            longURL.hash(&mut s);
            let s = s.finish();
            format!("{:x}", s)
        };
        
        self.map.borrow_mut().insert(hashed.clone(), longURL);
        format!("http://tinyurl.com/{}", hashed)
    }
    
    // Decodes a shortened URL to its original URL.
    fn decode(&self, shortURL: String) -> String {
        let hashed = shortURL.replace("http://tinyurl.com/", "");
        
        if let Some(val) = self.map.borrow().get(&hashed) {
            return val.clone();
        }
        
        return "".to_string()
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let s: String = obj.encode(strs);
 * let ans: VecVec<String> = obj.decode(s);
 */