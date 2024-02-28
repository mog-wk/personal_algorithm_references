#![allow(unused)]

#[derive(Debug)]
struct LSP_table {
    patten: Vec<u8>,
    table: Vec<u8>,
}

impl LSP_table {
    fn new(patten: &str) -> Self {
        let patten: Vec<u8> = patten.bytes().collect();

        let mut table = vec![];
        for _ in 0..patten.len() {
            table.push(0)
        }

        let (mut i, mut j) = (0_usize, 1_usize);

        for _ in 0..patten.len() {
            if (patten[i] != patten[j]) {
                if i == 0 {
                    table[i] = 0;
                    j += 1;
                } else {
                    i = table[i-1] as usize;
                }
            } else {
                table[j] = (i + 1) as u8;
                j += 1;
                i += 1;
            }
        }
        Self {
            patten,
            table,
        }
    }

    fn search(&self, st: &str) -> Vec<usize> {
        let st = st.bytes().collect::<Vec<u8>>();
        let mut match_arr: Vec<usize> = Vec::new();

        let (mut patten_ind, mut i) = (0_usize, 0_usize);

        while i < st.len() {
            let b = st[i];
            let patten_b = self.patten[patten_ind];
            println!("{}: {} {} {}", i, b, patten_b, patten_ind);
            if b == patten_b {
                patten_ind += 1;
            } else {
                if patten_ind != 0 {
                    patten_ind = self.table[patten_ind-1] as usize;
                }
            }
            if patten_ind == self.patten.len() {
                // match occured 
                match_arr.push(i-self.patten.len() + 1);
                patten_ind = 0;
            }
            i += 1;
        }

        match_arr
    }
}

fn main() {
    // test I
    let p = "ABCDABD";
    let lsp = LSP_table::new(&p);
    println!("{:?}", lsp);

    let test_str = "ABC ABCDAB ABCDABCDABDE";
    println!("{:?} | {} | {}", lsp.search(&test_str), &p, &test_str); // 15

    // test II
    let p = "ABABCABAB";
    let lsp = LSP_table::new(&p);


    let test_str = "ABABDABACDABABCABAB";
    println!("{:?} {}", lsp, test_str.len());
    println!("{:?} | {} | {}", lsp.search(&test_str), &p, &test_str); // 10
}
