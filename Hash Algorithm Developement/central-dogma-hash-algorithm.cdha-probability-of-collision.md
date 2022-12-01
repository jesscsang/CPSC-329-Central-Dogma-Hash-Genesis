---
id: 5vv5ke9cgbdfbt1w9eptrdi
title: Cdha Probability of Collision
desc: ''
updated: 1669867833530
created: 1667948857565
---

# Single Thread Brute Force Attack Time Analysis
$$
\begin{align}
&\text{Number of Hashes Computed: } 526044 \text{~~hashes} \\
&\text{Time Elapsed: } 21660.5585421999 \text{~~sec} \\
&\text{Average Time Per Hash } = \frac{21660.5585421999}{526044} = 
0.0411763246842468 \text{~~sec/hash} \\
&\text{Time to Hash All 8 character Passwords } = \frac{21660.5585421999}{526044} \times \frac{95^8}{60 \cdot 60 \cdot 24 \cdot 365} \\
&~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~= 8662232.1 \text{~~ years} \\
\end{align}
$$


# Hashing Similar Messages
```py
# Base message
genesisHash("The quick brown fox jumps over the lazy dog")
PRGSIAVAAGRRDVRVRPAISCS_QFVLLKLAILRGSMLSERRLAHCVWGVSLMLIYPRSGSVVFLKSSLT_DVRAWSPIGSIGYVCPSYPPTRPRRRCCDAEKCSSLGTFFKTE_IVTRGCPQTRLYY_AAHMHVVLSPAVSMRRVIRPDYVSPGTMKRQYSSNTISHSL_RHEIVS_AYFQLLSSWIDGLLLGRREQLLAGENMRLYQIYSMKGL_YAPIRVERVSEIIKGRNWTTTGQD_GTPRKPRYRLCFH

# Adding a period to the message
genesisHash("The quick brown fox jumps over the lazy dog.")
QSQRIREASCSSSCSLIR_WQDN_L_RCPRPLSHGCSCVPK_IR_RTCTQREQGLLAKVGKLLSKRSSSGMAAQMYFMLASFMANVIRSLASISDGSNSTFSFVPTKVAEPRHG_CIIMPVKNTITRVITTLPGRHQSISRGVSMKDNSCNTRVQTDAVEGLPYAFDS_YLWIPYPPDNKPTWIAHIFP_HWDWCFTMNVERIHRVETATTEALASRKISELPRSQRVRTATSSYRHINSLFPLTPGERTHTHGNY
```

    
# Probability of Collision Assuming Uniform Distribution
- Suppose we have $n$ possible $8$ character passwords and $m$ possible $256$ character hashes. What is the probability that at least two passwords will collide and have the same hash?
    - $\text{n passwords}$
        - ASCII has $95$ printable characters.
        - Since there are $8$ character is a password $n = 95^8$.
    - $\text{m hashes}$
        - There are $20$ different amino acids and $1$ nonsense codon thus there are $21$ possible characters that can be used in the hash.
            - $\text{char in hash} \in \{A,R,N,D,C,E,Q,G,H,I,L,K,M,F,P,S,T,W,Y,V,\_\}$ 
        - Since there are 256 characters in a hash $m = 21^{256}$.
    - Suppose the passwords are labeled from $1...n$.
    - Let $E_{i,j}:\text{``password i and j collide", } (i \ne j)$
        - $E_{i,j} = E_{j,i}$
    - Assuming uniform distribution:
        - $p(E_{i,j}) = \frac{1}{m}:$ as regardless of what the hash of the first password is the second password must have the same hash.
    - $E: \text{"at least two passwords collide"}$
        - In other words a collision.
        - The event $E$ that at least two passwords collide also includes the cases where more than two passwords collide.
$$E = \bigcup_{1 \le i \lt j \le n}E_{i,j}$$

$$
\begin{align}
p(E) = p(\bigcup_{1 \le i \lt j \le n}E_{i,j}) &\le \sum_{1 \le i \lt j \le n}p(E_{i,j}) \quad \text{(by the Union Bound)}\\
&\le \sum_{1 \le i \lt j \le n}\frac{1}{m} \\
&\le {n \choose 2} \cdot \frac{1}{m} \\
&\le \frac{n!}{2!(n-2)!} \cdot \frac{1}{m} \\
&\le \frac{n(n-1)(n-2)!}{2(n-2)!} \cdot \frac{1}{m} \\
&\le \frac{n(n-1)}{2} \cdot \frac{1}{m} \\
&\le \frac{n(n-1)}{2m} \\
&\lt \frac{n^2}{2m} \\
&\lt \frac{(95^8)^2}{2 \cdot 21^{256}} \approx 7.1517 \times 10^{-308}
\end{align}
$$
