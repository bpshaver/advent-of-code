# Advent of Code in Haskell

## 2023 Day 6

List comprehension and filter, refactored to use quadratic equation to find roots for polynomial.

- Part One: (0.01 secs, 179,912 bytes)

- Part Two: (15.36 secs, 16,523,149,904 bytes)

- Part Two (refactored): (0.00 secs, 73,224 bytes)

```ghci
GHCi, version 9.4.7: https://www.haskell.org/ghc/  :? for help
ghci> :set +s
ghci> :l 23_06
[1 of 2] Compiling Main             ( 23_06.hs, interpreted )
Ok, one module loaded.
(0.02 secs,)
ghci> partOne
4403592
(0.01 secs, 179,912 bytes)
ghci> partTwo
38017587
(0.00 secs, 73,224 bytes)
ghci> partTwo'
38017587
(15.36 secs, 16,523,149,904 bytes)
```
