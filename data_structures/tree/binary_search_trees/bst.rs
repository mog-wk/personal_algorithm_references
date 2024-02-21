use std::rc::Rc;
use std::mem::drop;

#[derive(Debug, PartialEq)]
enum NodePtr {
    Node(Rc<Node>),
    Null,
}

#[derive(Debug, PartialEq)]
struct Node {
    data: i32,
    l_ptr: NodePtr,
    r_ptr: NodePtr,
}

impl Node {
    fn new(data: i32, l_ptr: NodePtr, r_ptr: NodePtr) -> Self {
        Self { data, l_ptr: l_ptr, r_ptr: r_ptr }
    }
    fn default(data: i32) -> Self {
        Self { data, l_ptr: NodePtr::Null, r_ptr: NodePtr::Null }
    }
}

impl Drop for Node {
    fn drop(&mut self) {
        //println!("dropped node {:?}", self);
    }
}

#[derive(Debug)]
struct BinarySearhTree {
    root: Node,
}

impl BinarySearhTree {
    fn new(root: Node) -> Self {
        Self { root }
    }

    fn add(&mut self, node: &mut Node) {
        let mut stack: Vec<&mut Node> = Vec::new();
        stack.push(&mut self.root);

        while stack.len() != 0 {
            let cur = stack.pop().unwrap();
            if node.data <= cur.data {

            } else {

            }
        }
    }
}

fn main() {
    /*
    let l1 = Node::new(1, NodePtr::Null, NodePtr::Null);
    let l2 = Node::new(3, NodePtr::Null, NodePtr::Null);
    let r = Node::new(2, NodePtr::Node(Rc::new(l1)), NodePtr::Node(Rc::new(l2)));
    */

    let mut tree  = BinarySearhTree::new(Node::default(10));
    let mut l2 = Node::new(3, NodePtr::Null, NodePtr::Null);

    tree.add(&mut l2);

    println!("{:?}", tree);
}
