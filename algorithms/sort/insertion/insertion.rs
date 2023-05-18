

fn main() {
    println!("Hello, world!");

    let test = vec![5, 2, 3, 4, 1];
    println!("{:?}", issort(&test));
}

fn issort(arr: &[u32]) -> Vec<u32> {
    let mut sorted = arr.to_vec();
    println!("{:?}", sorted);
    for i in 1..arr.len() {
        let mut j = i;
        while j > 0 && &sorted[j] < &sorted[j-1] {
            sorted.swap(j, j-1);
            j-=1;
        }
    }
    sorted
}
