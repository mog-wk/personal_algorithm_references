

fn main() {
    let data: [i32; 12] = [1, 1, 2, 3, 5, 7, 12, 13, 17, 21, 25, 28];

    let ans = binary_search(&data, 28).unwrap();

    println!("{:?} {}", data, ans);

}

fn _binary_search(arr: &[i32], n: i32, i: usize) -> Result<usize, String> {
    println!("{:?}", arr);
    if arr.len() == 0 { return Err(format!("cold not find {}", n)); }
    let mid = (arr.len()) / 2;

    let elt = arr[mid];
    if elt == n {
        return Ok(mid + i);
    } else if elt > n {
        return _binary_search(&arr[0..mid], n, i);
    } else if elt < n {
        let i = i + mid;
        return _binary_search(&arr[mid..arr.len()], n, i);
    }
    Err(format!("cold not find {}", n))
}
pub fn binary_search(arr: &[i32], n: i32) -> Result<usize, String> {
    _binary_search(arr, n, 0)
}
