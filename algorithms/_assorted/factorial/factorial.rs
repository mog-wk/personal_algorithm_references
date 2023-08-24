

fn main() {
    for i in 0..=12 {
        println!("{} {} {}", i, factorial(i), factorial_tail(i, 1));
    }
}


// O(n)
// x | x -1 | x-2 | x-3 |...| 1
pub fn factorial(x: u32) -> u32 {
    if x <= 1 {
        return 1;
    }
    x * factorial(x-1)
}


/// tail recursive factorial

pub fn factorial_tail(x: u32, a: u32) -> u32 {
    if x <= 1{
        return a;
    }
    factorial_tail(x - 1, x * a)
}
