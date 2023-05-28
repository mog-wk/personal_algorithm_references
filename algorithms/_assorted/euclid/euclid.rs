use std::io::{ Error, ErrorKind };


fn main() {
    println!("Hello, world!");
    let tests = [
        ((32, 12), 6),
        ((3, 12), -1), 
        ((12, 12), 12),
        ((2, 12), -1),
        ((124, 12), 123),
        ((32, 2), 2),
        ((11, 2), 1),
        ((36, 4), 4),
    ];

    for test in tests {
        match max_common_divider(test.0.0, test.0.1) {
            Ok(t) => println!("{} {} {} {}", test.0.0, test.0.1, t, test.1),
            Err(e) => println!("failed due to {}", e),
        };
    }
}



// euclids algorithms
fn max_common_divider(mut x: i32, mut y: i32) -> Result<u32, Error> {
    if x < y || y == 0 {
        return Err(ErrorKind::InvalidData.into());
    }
    loop {
        let r = x % y;
        if r == 0 {
            return Ok(x as u32);
        } else {
            (x, y) = (y, r);
        }
    }
}
