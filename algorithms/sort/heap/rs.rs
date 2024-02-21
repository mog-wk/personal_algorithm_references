
fn main() {
    let mut test_arr = [3, 1, 2, 13, 15, 12, 6, 8];
    println!("{:?}", test_arr);

    let mut heap = Heap::from(Vec::from(test_arr));
    println!("creation: {:?}", heap);

    heap.insert(52);
    println!("insertion: {:?}", heap);
    let f2 = heap.remove().unwrap();
    println!("remove: {:?} {}", heap, f2);
}

#[derive(Debug)]
struct Heap {
    nodes: Vec<i32>,
    len: usize,
}

impl Heap {
    fn new() -> Self {
        Self { nodes: Vec::<i32>::new(), len: 0 }
    }

    fn insert(&mut self, el: i32) {
        self.nodes.push(el);
        self.len += 1;
        let ended = self.heapfy();
        match ended {
            Some(v) => println!("{:?} {:?}", el, v),
            None => ()
        }
    }
    fn heapfy(&mut self) -> Option<usize> {
        if self.len <= 1 {
            return None
        }

        let last_ind = self.len-1;

        let mut stack = vec![last_ind];

        while stack.len() > 0 {
            let mut cur = stack.pop().unwrap();
            if cur == 0 {
                return Some(0)
            }
            let parent_ind = if cur % 2 == 0 {
                (cur-2) / 2
            } else {
                (cur-1) / 2
            };

            let parent = self.nodes[parent_ind];
            let last = self.nodes[cur];

            //println!("{} {} {} {}", last, cur, parent, parent_ind);


            if parent < last {
                self.swap(parent_ind, cur);
                stack.push(parent_ind);
            }
            println!("{:?}", self.nodes);
        }

        return Some(last_ind);
    }
    fn heapfy_down(&mut self) -> Option<usize> {
        if self.len <= 1 {
            return None
        }

        let last_ind = 0_usize;

        let mut stack = vec![last_ind];

        while stack.len() > 0 {
            let mut cur = stack.pop().unwrap();

            let ci0 = cur * 2 + 1;
            let ci1 = cur * 2 + 2;

            if ci0 >= self.len {
                return Some(cur)
            }

            let cv0 = self.nodes[ci0];

            let choosen_index = if ci1 >= self.len {
                ci0
            } else {
                if cv0 > self.nodes[ci1] {
                    ci0
                } else {
                    ci1
                }
            };

            let value = self.nodes[cur];

            if value < self.nodes[choosen_index] {
                self.swap(cur, choosen_index);
                stack.push(choosen_index);
            }
            println!("{:?}", self.nodes);
        }

        return Some(last_ind);
    }

    fn remove(&mut self) -> Result<i32, Box<dyn std::error::Error>> {
        self.swap(self.len-1, 0);
        let el = self.nodes.pop().ok_or(std::fmt::Error)?;
        self.len -= 1;
        self.heapfy_down();
        Ok(el)
    }

    fn peek(&self) -> i32 {
        self.nodes[0]
    }

    fn len(&self) -> usize {
        self.len
    }

    fn swap(&mut self, i: usize, j: usize) {
        (self.nodes[j], self.nodes[i]) = (self.nodes[i], self.nodes[j]);
    }
}

impl std::convert::From<Vec<i32>> for Heap {
    fn from(arr: Vec<i32>) -> Self {
        let mut proto_heap = Self::new();

        for v in arr.into_iter() {
            proto_heap.insert(v);
        }

        proto_heap
    }
}
