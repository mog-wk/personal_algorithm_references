

fn main() {
    println!("counting");
    let mut arr: [u8; 12] = [4, 2, 1, 3, 5, 5, 8, 1, 1, 5, 2, 1];
    println!("{:?}", arr);
    counting_sort(&mut arr, 8);
    println!("{:?}", arr);
}

fn counting_sort(arr: &mut [u8], max: usize) {
    let mut counting_arr = vec![0_u8; max + 1];
    for j in 0..max+1 {
        for i in arr.iter() {
            if *i == j as u8 {
                counting_arr[j as usize] += 1;
            }
        }
    }
    println!("{:?}", counting_arr);
    let mut i = 0;
    for j in 0..=max {
        for c in 0..counting_arr[j] {
            println!("{} {}", j, i);
            arr[i] = j as u8;
            i += 1;
        }
    }
}
