
fn selection_sort(arr: &mut [i32]) {
    let mut changed = false;
    for i in 0..arr.len()-1 {
        for j in i+1..arr.len() {
            println!("- {:?} {} {}", arr, i, j);
            if arr[i] > arr[j] {
                (arr[i], arr[j]) = (arr[j], arr[i]);
                changed = true;
            }
        }
        println!("========================");
        if !changed {
            break
        } else {
            changed = false;
        }
    }
}

fn bubble_sort(arr: &mut [i32]) {
    for l in 0..arr.len()-1 {
        let mut changed = false;
        for i in 0..arr.len()-1-l {
            let j = i + 1;
            println!("- {:?} {} {}", arr, i, j);
            if arr[i] > arr[j] {
                (arr[i], arr[j]) = (arr[j], arr[i]);
                changed = true;
            }
        }
        println!("========================");

        if !changed {
            break
        }
    }
}

fn insertion_sort(arr: &mut [i32]) {
    for i in 1..arr.len() {
        let mut j = i;
        while j != 0 && arr[j-1] > arr[j] {
            (arr[j], arr[j-1]) = (arr[j - 1], arr[j]);
            j -= 1;
        }
        println!("- {:?} {}", arr, i);
    }
}


fn main() -> () {
    //let mut arr = [5, 2, 1, 4, 2, 3, 7, 6];
    let mut arr = [16, 5, 13, 1, 2, 5];
    //let mut arr = [7, 6, 5, 4, 3, 2, 2, 1];
    //let mut arr = [1, 2, 2, 3, 4, 5, 6, 7];

    println!("Bubble:");
    println!("->> {:?}", arr);
    bubble_sort(&mut arr);
    println!("->> {:?}", arr);

    println!("Selection:");
    let mut arr = [16, 5, 13, 1, 2, 5];
    println!("->> {:?}", arr);
    selection_sort(&mut arr);
    println!("->> {:?}", arr);

    println!("Insertion:");
    let mut arr = [16, 5, 13, 1, 2, 5];
    println!("->> {:?}", arr);
    insertion_sort(&mut arr);
    println!("->> {:?}", arr);
}

#[cfg(test)]
mod tests {
    #[test]
    fn bubble_sort() {
        let mut arr = [5, 2, 1, 4, 2, 3, 7, 6];
        bubble_sort(&mut arr);

        let ans = [1, 2, 2, 3, 4, 5, 6, 7];

        assert_eq!(ans, arr);
    }
    #[test]
    fn selection_sort() {
        let mut arr = [5, 2, 1, 4, 2, 3, 7, 6];
        selection_sort(&mut arr);

        let ans = [1, 2, 2, 3, 4, 5, 6, 7];

        assert_eq!(ans, arr);
    }
    #[test]
    fn insertion_sort() {
        todo!();
        let mut arr = [5, 2, 1, 4, 2, 3, 7, 6];
        insertion_sort(&mut arr);

        let ans = [1, 2, 2, 3, 4, 5, 6, 7];

        assert_eq!(ans, arr);
    }
}
