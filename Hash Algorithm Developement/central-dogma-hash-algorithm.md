---
id: 1j2kfwcx5qfk9jycaynzl8v
title: Central Dogma Hash Algorithm
desc: ''
updated: 1669862414421
created: 1668031634889
---

# Central Dogma Hash Algorithm (CDHA1-256)
- also known as the _"Genesis Hash Algorithm"_

## Properties of CDHA1-256
1. one-way function
2. $256$ character fixed length digest
3. $prob(\text{``collision of two random 8 character passwords"}) = 7.1517 \times 10^{-308}$
4. single thread brute force attack on $8$ character passwords $5108985329.6 \text{ years}$

## Table of Contents
- [[central-dogma-hash-algorithm.cdha-step-by-step-overview]]
- [[central-dogma-hash-algorithm.cdha-python-implementation]]
- [[central-dogma-hash-algorithm.cdha-supplementary-materials]]
- [[central-dogma-hash-algorithm.cdha-probability-of-collision]]

---

# Draft Work

- The number of printable ASCII characters $95$
- All possible two 8 character password combinations 
    - $95^{16}$
- Let $A$ be the set of remapped ASCII values
    - $1 \times 12 \text{ digits}$
    - $6 \times 13 \text{ digits}$
    - $88 \times 14 \text{ digits}$
    - 
        ![](/assets/images/2022-11-11-14-51-50.png)

- Let $s_1$ and $s_2$ be the passwords where
   - $s_1 = x_1x_2...x_8$
   - $s_2 = x_9x_{10}...x_{16}$
   - $x_1,x_2,...x_{16} \in A$

- $x_i = d_{i,1}d_{i,2}...d_{i,n} \text{ where } n \in \{12,13,14\}$
- $h_{odd} = d_{1,1}d_{1,3}...d_{8,2k-1}...d_{8,2k+1} \text{ where } k \in \N$
- $h_{even} = d_{1,0}d_{1,2}...d_{8,2k-2}...d_{8,2k} \text{ where } k \in \N$
- $h = h_{odd} + h_{even}$

- there are two cases to consider:
    - **Case 1**: $|h_{even}| = |h_{odd}|$
        - Assuming the worse case each character will get mapped to a 14 digit number
        - The sum of two 14 digit numbers is at most:
            - $99~999~999~999~999 + 99~999~999~999~999 = 199~999~999~999~998$
            - $$
        - <span style=color:cyan;background:none>Separate probability by index or bundle them together?</span>
    - **Case 2**: $|h_{even}| = |h_{odd}| + 1$

---

---

## Lemma 1
- Suppose $a + b = n \text{ where } n \in N \text{ and } a,b \in \N_0 \text{ such that } 0 \le a,b \le n$
- Then the number of permutations for $a,b$ is $n+1$
    $a$ | $b$
    :---:|:---:
    $n$ | $0$
    $n-1$ | $1$
    $...$ | $...$
    $0$ | $n$

- 0.03
- $\frac{1}{95^8} = $
