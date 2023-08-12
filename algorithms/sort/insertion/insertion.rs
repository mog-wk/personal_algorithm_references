
fn main() {
    println!("Hello, world!");

    let mut test = vec![5, 2, 3, 4, 1];
    issort(&mut test, 5);
    println!("{:?}", test);
}

fn issort(arr: &mut [u32], sz: usize) {
    println!("{:?} {}", arr, sz);
    for i in 1..sz {
        let mut j = i;
        while j > 0 && arr[j] < arr[j - 1] {
            println!("{} {}", i, j);
            arr.swap(j, j - 1);
            j-=1;
        }
    }
}
