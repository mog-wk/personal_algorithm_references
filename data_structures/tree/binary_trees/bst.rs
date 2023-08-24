use std::rc::Rc;
use std::mem::drop;

#[derive(Debug)]
enum NodePtr {
    Node(Rc<Node>),
    Null,
}

#[derive(Debug)]
struct Node {
    data: i32,
    l_ptr: Box<NodePtr>,
    r_ptr: Box<NodePtr>,
}

impl Node {
    fn new(data: i32, l_ptr: NodePtr, r_ptr: NodePtr) -> Self {
        Self { data, l_ptr: Box::new(l_ptr), r_ptr: Box::new(r_ptr) }
    }
}

impl Drop for Node {
    fn drop(&mut self) {
        //println!("dropped node {:?}", self);
    }
}


fn main() {
    println!("hello world");

    let l1 = Node::new(1, NodePtr::Null, NodePtr::Null);
    let l2 = Node::new(3, NodePtr::Null, NodePtr::Null);
    let r  = Node::new(2, NodePtr::Node(Rc::new(l1)), NodePtr::Node(Rc::new(l2)));


    println!("{:?}", r);
}
