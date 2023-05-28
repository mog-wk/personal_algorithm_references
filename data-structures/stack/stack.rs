use std::ops::Add;
use std::fmt::{ Display, Debug };
use std::clone::Clone;

struct Stack<T> {
    list: Vec<T>,
    len: usize,
}

impl<T: Clone> Stack<T> {
    fn new(list: &[T]) -> Stack<T> {
        Stack {list: list.to_vec(), len: list.len()}
    }

    fn push(&mut self, elt: T) {
        self.len += 1;
        self.list.push(elt);
    }

    fn extend() {

    }

    fn peek(&self) -> Result<&T, &str> {
        if self.len < 1 {
            return Err("can not peek empty stack")
        } else {
            Ok(&self.list[self.len - 1])
        }
    }

    fn pop(&mut self) -> Option<T> {
        if self.len == 0 {
            return None
        }
        self.len -= 1;
        self.list.pop()
    }

}

//push
impl<T> Add for Stack<T> where Vec<T>: Add<Output = Vec<T>> {
    type Output = Stack<T>;
    fn add(self, other: Stack<T>) -> Self::Output {
        Stack {list: self.list + other.list, len: self.len + other.len}
    }
}

impl<T: std::fmt::Display> Display for Stack<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "Stack: [")?;

        for i in self.list.iter() {
            write!(f, "{}", i)?;
        }
        write!(f, "]")
    }
}

impl<T: std::fmt::Debug> Debug for Stack<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{:?}", self.list)
    }
}


fn main() {

    let tests = [
        Stack::new(&[1, 2, 3, 4]),
        Stack::new(&[5, 2, 3, 1]),
        Stack::new(&[6, 2, 1, 12]),
        Stack::new(&[5, 2]),
        Stack::new(&[]),
    ];

    println!("data set: {:?}\n", tests);

    for mut t in tests {
        println!("init => {:?}", t);
        t.push(123);
        println!("{}", t.peek().unwrap());
        t.pop();
        println!("{}", t.peek().unwrap());
        println!("end => {:?}\n", t);
    }

}

