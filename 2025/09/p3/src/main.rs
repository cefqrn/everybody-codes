use std::fs;
use std::iter::repeat_n;
use std::collections::BTreeMap;
use std::time::Instant;

#[derive(Clone, Copy, Debug, PartialEq)]
enum DNASymbol {
    A, T, C, G
}

type DnaIdentifier = Box<[DNASymbol]>;

struct Dsu {
    reps:  Box<[usize]>,
    ranks: Box<[usize]>,
}

impl Dsu {
    fn new(n: usize) -> Dsu {
        Dsu {
            reps:  (0..n).collect(),
            ranks: repeat_n(0, n).collect()
        }
    }

    fn find(&mut self, mut i: usize) -> usize {
        let rep = self.reps[i];
        if i != rep {
            let root = self.find(rep);

            self.reps[i] = root;
            i = root;
        }

        i
    }

    fn merge(&mut self, i: usize, j: usize) -> bool {
        let mut i = self.find(i);
        let mut j = self.find(j);
        if i == j {
            return false;
        }

        if self.ranks[j] > self.ranks[i] {
            (i, j) = (j, i);
        }

        self.reps[j] = i;
        if self.ranks[i] == self.ranks[j] {
            self.ranks[i] += 1;
        }

        true
    }
}

fn parse_dna(dna: &str) -> Box<[DNASymbol]> {
    dna.chars().map(|c| match c {
        'A' => DNASymbol::A,
        'T' => DNASymbol::T,
        'C' => DNASymbol::C,
        'G' => DNASymbol::G,
        _ => { panic!("invalid dna identifier") }
    }).collect()
}

fn similarity(a: &DnaIdentifier, b: &DnaIdentifier) -> usize {
    a.iter().zip(b).filter(|(a, b)| a == b).count()
}

fn main() {
    let now = Instant::now();

    let ducks: Box<[(usize, DnaIdentifier)]> = fs::read_to_string("../everybody_codes_e2025_q09_p3.txt")
        .expect("couldn't read input")
        .trim()
        .lines()
        .map(|x| {
            let (scale_number, dna) = x.split_once(":").expect("invalid input");
            (scale_number.parse().expect("invalid scale number"), parse_dna(dna))})
        .collect();

    let dna_size = ducks[0].1.len();
    let duck_count = ducks.len();

    let mut families = Dsu::new(duck_count);
    for (scale_i, child_dna) in &ducks {
        let mut possible_parents: Box<[(usize, &usize, &DnaIdentifier)]> = ducks.iter()
            .map(|(scale_number, dna)| (similarity(child_dna, dna), scale_number, dna))
            .collect();
        possible_parents.sort_by(|a, b| a.0.cmp(&b.0));

        for (similarity_a, scale_j, dna_a) in &possible_parents {
            for (similarity_b, scale_k, dna_b) in possible_parents.iter().rev() {
                if similarity_a + similarity_b < dna_size {
                    break;
                }

                if scale_i == *scale_j || scale_i == *scale_k || scale_j == scale_k {
                    continue;
                }

                if child_dna.iter().zip(*dna_a).zip(*dna_b).all(|((c, a), b)| c == a || c == b) {
                    families.merge(scale_i-1, *scale_j-1);
                    families.merge(scale_i-1, *scale_k-1);
                }
            }
        }
    }

    let mut scale_sums: BTreeMap<usize, (usize, usize)> = BTreeMap::new();
    for i in 0..duck_count {
        let (count, sum) = scale_sums.entry(families.find(i)).or_insert((0, 0));
        *count += 1;
        *sum += i + 1;
    }

    let (_, result) = scale_sums.into_values().max_by(|(a, _), (b, _)| a.cmp(b)).unwrap();

    let elapsed = now.elapsed();

    println!("found {result:?} in {elapsed:?}");
}
