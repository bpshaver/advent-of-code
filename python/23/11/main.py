"""
Because you're not supposed to commit the input text, send the input text to this script
on stdin: 

```bash
$ cat input.txt | python main.py
```
"""
import itertools
import sys
from pathlib import Path
from typing import Iterator


def count(iter: Iterator) -> int:
    """Consume the iterator and returns the number of elements it contained.

    Because Python doesn't have this built in? Sometimes you don't care about what the
    iterator actually contains. (And you don't want to initialize an intermediate list.)
    """
    c = 0
    for element in iter:
        c += 1
    return c


def parse_input(input: str) -> tuple[list[tuple[int, int]], list[int], list[int]]:
    idxes = []
    empty_rows = []
    for row_idx, row in enumerate(input.strip().split("\n")):
        if row_idx == 0:
            empty_cols = list(range(len(row)))
        if "#" not in row:
            empty_rows.append(row_idx)
        else:
            for col_idx, char in enumerate(row):
                if char == "#":
                    idxes.append((row_idx, col_idx))
                    empty_cols = [idx for idx in empty_cols if idx != col_idx]

    return (idxes, empty_rows, empty_cols)


def get_true_distance(
    coords: tuple[tuple[int, int], tuple[int, int]],
    empty_rows: list[int],
    empty_cols: list[int],
    multiplier: int,
) -> int:
    (ra, ca), (rb, cb) = coords
    ra, rb = sorted((ra, rb))
    ca, cb = sorted((ca, cb))
    multiplier = multiplier - 1

    vdist = rb - ra + multiplier * count(filter(lambda n: ra < n < rb, empty_rows))
    hdist = cb - ca + multiplier * count(filter(lambda n: ca < n < cb, empty_cols))

    return vdist + hdist


def solution(input: str, multiplier: int) -> int:
    idxes, empty_rows, empty_cols = parse_input(input)
    pairs = filter(lambda pair: pair[0] < pair[1], itertools.product(idxes, idxes))

    return sum(
        map(
            lambda pair: get_true_distance(pair, empty_rows, empty_cols, multiplier),
            pairs,
        )
    )


def main():
    with (Path(__file__).parent / "sample.txt").open("r") as f:
        sample_str = f.read()
    assert (
        res := solution(sample_str, 2)
    ) == 374, f"Part one failed on sample input with result {res}"
    assert (
        res := solution(sample_str, 10)
    ) == 1030, f"Part two failed on sample input with multiplier 10 and result {res}"
    assert (
        res := solution(sample_str, 100)
    ) == 8410, f"Part two failed on sample input with multiplier 100 and result {res}"

    input_str = sys.stdin.read()

    print("Part One: ", solution(input_str, 2))
    print("Part Two: ", solution(input_str, 1_000_000))


if __name__ == "__main__":
    main()
