
fn main() {
    println!("======== Basic Patten Matching ========");

    let test = "books are to be tasted, others to be swallowed, books and some few to be chewed and digested.";

    println!("{:?}", match_all(&test, &"books"));
    //println!("{:?}", match_all(&test, &"to"));
}

fn r#match_all(st: &str, patten: &str) -> Vec<usize> {
    // TODO: check if st is UTF-8
    let st: Vec<u8> = st.bytes().collect();
    let patten: Vec<u8> = patten.bytes().collect();
    let mut matches = Vec::new();
    for i in 0..st.len() {
        let b = st[i];
        if b == patten[0] {
            let mut count = 1;
            for j in 1..patten.len() {
                if st[i+j] == patten[j] {
                    count += 1;
                } else {
                    break;
                }
            }
            if count == patten.len() {
                matches.push(i);
            }
        }
    }
    matches
}
