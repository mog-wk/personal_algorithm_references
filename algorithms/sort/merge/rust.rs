
fn merge_sort(arr: &[u32], s: usize, e: usize) -> [u32] {
    if arr.len() == 1 {
        return arr;
    }
    let mid = (e as f32 / 2.0).floor() as usize;

    let left = merge_sort(arr, s, mid);
    let right = merge_sort(arr, mid+1, e);

    merge(&left, &right)
}

fn merge(left: &[u32], right: &[u32]) -> [u32] {
    todo!()
}

fn main() {

}
