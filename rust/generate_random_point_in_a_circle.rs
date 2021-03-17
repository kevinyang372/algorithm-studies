use rand::distributions::{Distribution, Uniform};

struct Solution {
    radius: f64,
    x_center: f64,
    y_center: f64,
    x1: f64,
    x2: f64,
    y1: f64,
    y2: f64,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(radius: f64, x_center: f64, y_center: f64) -> Self {
        Self {
            radius,
            x_center,
            y_center,
            x1: x_center - radius,
            x2: x_center + radius,
            y1: y_center - radius,
            y2: y_center + radius,
        }
    }
    
    fn rand_point(&self) -> Vec<f64> {
        let x_sampler = Uniform::from(self.x1..=self.x2);
        let y_sampler = Uniform::from(self.y1..=self.y2);
        
        let mut rng = rand::thread_rng();
        
        let mut x = x_sampler.sample(&mut rng);
        let mut y = y_sampler.sample(&mut rng);
        
        while !self.contains_point(x, y) {
            x = x_sampler.sample(&mut rng);
            y = y_sampler.sample(&mut rng);
        }
        
        vec![x, y]
    }
    
    fn contains_point(&self, x: f64, y: f64) -> bool {
        ((x - self.x_center).powf(2.) + (y - self.y_center).powf(2.)).sqrt() <= self.radius
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(radius, x_center, y_center);
 * let ret_1: Vec<f64> = obj.rand_point();
 */