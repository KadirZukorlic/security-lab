# Password cracking

Practice on how password hashing works and why it can be broken.

## Concept

A hash is one-way, so cracking means hashing guesses and comparing. Fast hashes like
MD5 or SHA-256 can be tried billions of times per second. This is exactly why production
systems should use slow hashes (bcrypt, argon2) with a per-user salt.

## Scripts

- `crack.py` — [short description of what it does]

## Run

python crack.py

Tested only on hashes I generated myself.