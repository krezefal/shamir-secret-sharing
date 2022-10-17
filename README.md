# Shamir's Secret Sharing

Shamir's Secret Sharing (SSS) is an efficient secret sharing 
algorithm for distributing private information (the "secret") in such
a way that no individual holds intelligible information about the 
secret. To achieve this, the secret is converted into parts (the 
"shares") from which the secret can be reassembled when a sufficient
number of shares are combined but not otherwise. SSS has the unusual
property of information theoretic security, meaning an adversary 
without enough shares cannot reconstruct the secret even with infinite
time and computing capacity. A standard SSS specification for 
cryptocurrency wallets has been widely implemented.