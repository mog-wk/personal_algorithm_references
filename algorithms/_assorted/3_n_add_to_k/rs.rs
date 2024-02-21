fn main() {
    let mut arr1: [i32; 5] = [3, 6, -9, -12, 15];
    let mut arr2: [i32; 5] = [2, -5, 8, 13, 17];
    let mut arr3: [i32; 5] = [1, -3, 5, -10, 15];

    let mut arr1: [i32; 2] = [8, -3];
    let mut arr2: [i32; 2] = [2, -5];
    let mut arr3: [i32; 2] = [1, -3];

    let res = has_triplets(&mut arr1, &mut arr2, &mut arr3, 0);
    //println!("inputs:\n{:?}\n{:?}\n{:?}\n", &arr1, &arr2, &arr3);

    println!("{:?}", res);
}
fn has_triplets(arr1: &mut [i32], arr2: &mut [i32], arr3: &mut [i32], s: i32) -> Option<(usize, usize, i32)> {
    arr1.sort(); // n log n
    arr2.sort(); // n log n


    for n in arr3.iter() {
        let (mut i, mut j) = (0, 0);
        let n = *n;
        while i < arr1.len() && j < arr2.len() {

            println!("{} {} {}", arr1[i], arr2[j], n);
            let sum = arr1[i] + arr2[j];
            if n == sum * -1 {
                return Some((i, j, n));
            } 
            if n > sum {
                i += 1; 
            } else {
                j += 1;
            }
        }
    }
    None
}

fn _has_triplets(arr1: &[i32], arr2: &[i32], arr3: &[i32], s: i32) -> Option<()> {
    let mut bunk: Vec<i32> = Vec::with_capacity(arr1.len() + arr2.len());
    for i in arr1.iter() {
        for j in arr2.iter() {
            bunk.push(i + j);
        }
    }

    bunk.sort();

    let mut res: Vec<(usize, usize, usize)> = Vec::new();
    for j in 0..arr3.len() {
        /*
        for i in 0..bunk.len() {
            if arr3[j] + bunk[i] == 0 {
                let r = i % arr1.len();
                res.push(((i - r) / arr2.len(), r, j));
            }
        }
        */

        match bin_search(&bunk, arr3[j] * -1, 0) {
            Some(i) => return Some(()),
            None => (),
        }
    }


    Some(())
}

fn bin_search(arr: &[i32], el: i32, i: usize) -> Option<usize> {
    if arr.len() == 0 {
        return None
    }
    let mid = arr.len() / 2;

    if arr[mid] == el {
        return Some(mid + i)
    } else if arr[mid] > el {
        return bin_search(&arr[0..mid], el, i);
    } else {
        let inc = mid + i + 1;
        return bin_search(&arr[mid+1..arr.len()], el, inc);
    }
    None
}

fn _bin_search(arr: &[i32], el: i32) -> Option<usize> {
    let length = arr.len() - 1;
    let mut stack: Vec<_> = vec![(0, length, 0)];

    while stack.len() != 0 {
        let cur = stack.pop().unwrap();
        if cur.1 >= cur.0 {
            return None
        }
        let mid = (cur.1 - cur.0) / 2;
        println!("{:?} {:?}", stack, cur);

        let i = cur.2;

        if el == arr[mid] {
            return Some(mid + i)
        } else if el > arr[mid] {
            stack.push((mid+1+i, length, i + mid));
        } else {
            stack.push((0, mid-i, i));
        }
    }
    None
}
