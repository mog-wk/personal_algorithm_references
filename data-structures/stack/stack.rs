use std::ops::Add;
use std::fmt::Display;

struct Stack<T> {
    list: Vec<T>,
}

impl<T> Stack<T> {
    fn new(list: Vec<T>) -> Stack<T> {
        Stack {list: list.to_vec()}
    }

    fn push(&mut self, elt: T) {
        self.list.push(elt);
    }

}

//push
impl<T> Add for Stack<T> where Vec<T>: Add<Output = Vec<T>> {
    type Output = Stack<T>;
    fn add(self, other: Stack<T>) -> Self::Output {
        Stack {list: self.list + other.list}
    }
}

impl<T: std::fmt::Display> Display for Stack<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "Stack: [")?;

        for (i, e) in self.list.iter().enumerate() {
            write!(f, "{} {}", i, e);
        }
        write!(f, "]")
    }
}


fn main() {

    let tests = [
        Stack::new([1, 2, 3, 4]),
        Stack::new([5, 2, 3, 1]),
        Stack::new([6, 2, 1, 12]),
        Stack::new([5, 2]),
        Stack::new([]),
    ];

    println!("{:?}", stack_1.list);

}

