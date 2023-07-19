use std::fmt::Display;


enum List {
    // tuple for node in list ( data, pointer )
    Cons(u32, Box<List>),
    // end of list
    NIL,
}

impl List {
    fn new() -> Self {
        Self::NIL
    }

    fn prepend(self, data: u32) -> List {
        List::Cons(data, Box::new(self))
    }
}

impl Display for List {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match *self {
            List::Cons(head, ref tail) => {
                write!(f, "{} {}", head, tail)
            },
            List::NIL => write!(f, "NIL")
        }

    }
}


fn main() {
    let mut list = List::new();
    list = list.prepend(32);
    list = list.prepend(32);
    println!("{}", list);

}


