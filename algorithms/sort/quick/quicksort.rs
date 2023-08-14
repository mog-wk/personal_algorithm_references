use rand::Rng;


fn main() {
    println!("Hello Wrold");
    //let mut arr: [u32; 10] = [6, 4, 1, 9, 0, 7, 3, 2, 5, 8];
    let mut arr: [u32; 4] = [4, 3, 2, 1];
    //let mut arr: [(u32, u8); 6] = [(4, 0), (2, 0), (1, 0), (3, 0), (3, 1), (2, 1)];
    let mut b_arr: [u32; 100] = [
        45, 23, 55, 46, 47, 66, 93, 55, 12, 30, 44, 77, 17, 96, 27, 61, 18, 14, 22, 90, 47, 3, 74,
        17, 86, 4, 43, 53, 32, 55, 54, 92, 54, 80, 74, 7, 53, 18, 38, 25, 69, 96, 33, 48, 8, 58,
        31, 52, 0, 3, 10, 46, 94, 92, 63, 44, 0, 4, 41, 18, 52, 64, 44, 82, 79, 99, 60, 0, 51, 12,
        81, 30, 26, 86, 0, 24, 95, 59, 21, 47, 81, 36, 55, 22, 28, 90, 33, 86, 71, 89, 40, 20, 25,
        97, 29, 11, 20, 31, 87, 84,
    ];
    println!("---{:?}", arr);
    quick_sort(&mut arr, 0, 4);
    println!("---{:?}", arr);
}

//fn quick_sort(arr: &mut [(u32, u8)], stt: usize, end: usize) {
fn quick_sort(arr: &mut [u32], stt: usize, end: usize) {
    if stt < end {
        //let p = partition_rand_unstable(arr, stt, end);
        let p = partition_end(arr, stt, end);
        quick_sort(arr, stt, p - 1);
        quick_sort(arr, p, end);
    } else {
        println!("DONE ======================");
    }
}

fn partition_start(arr: &mut [u32], stt: usize, end: usize) -> usize {
    let p = stt;

    println!("   {:?}", arr);
    let mut j: usize = stt + 1;
    for i in stt+1..end {
        if arr[i] < arr[p] {
            arr.swap(j, i);
            j += 1;
        }
    }
    arr.swap(stt, j - 1);
    j
}

fn partition_end(arr: &mut [u32], stt: usize, end: usize) -> usize {
    let p = end - 1;
    println!("{:?} ", &arr[stt..end]);

    let mut j: usize = stt;
    for i in stt..end-1 {
        if arr[i] < arr[p] {
            arr.swap(j, i);
            j += 1;
        }
    }
    arr.swap(p, j);
    println!("{:?}", &arr[stt..end]);
    println!("====");
    j + 1
}

fn partition_rand(arr: &mut [u32], stt: usize, end: usize) -> usize {
    arr.swap(rand::thread_rng().gen_range(stt..end), stt);
    let p = stt;

    //println!("   {:?}", arr);
    let mut j = stt + 1;
    for i in stt+1..end {
        if arr[i] < arr[p] {
            arr.swap(i, j);
            j += 1;
        }
    }
    arr.swap(p, j-1);
    j
}

fn partition_rand_unstable(arr: &mut [(u32, u8)], stt: usize, end: usize) -> usize {
    /// demostration of quicksort non-stability
    arr.swap(rand::thread_rng().gen_range(stt..end), stt);
    let p = stt;

    //println!("   {:?}", arr);
    let mut j = stt + 1;
    for i in stt+1..end {
        if arr[i].0 <= arr[p].0 {
            arr.swap(i, j);
            j += 1;
        }
    }
    arr.swap(p, j-1);
    j
}
