import Control.Monad (unless)

pairs :: [a] -> [(a, a)]
pairs l = zip (init l) (tail l)

diff :: (Num a) => (a, a) -> a
diff (x, y) = y - x

diffs :: (Num a) => [a] -> [a]
diffs l = map diff (pairs l)

allZeros :: (Num a, Eq a) => [a] -> Bool
allZeros = all (== 0)

nextValue :: (Num a, Eq a) => [a] -> a
nextValue seq =
  if allZeros seq then 0 else last seq + nextValue (diffs seq)

firstValue :: (Num a, Eq a) => [a] -> a
firstValue seq =
  if allZeros seq then 0 else head seq - firstValue (diffs seq)

parseLine :: (Read a) => String -> [a]
parseLine l = map read (words l)

parseInput :: String -> [[Int]]
parseInput s = map parseLine (lines s)

main = do
  tests
  input <- readFile "input.txt"
  let sequences = parseInput input
  let part_one = sum (map nextValue sequences)
  print part_one
  let part_two = sum (map firstValue sequences)
  print part_two

assertEq l r e = do
  unless (l == r) (error e)

tests = do
  assertEq (pairs [1, 2, 3]) [(1, 2), (2, 3)] "Pairs failed"
  assertEq (diff (3, 5)) 2 "diff failed"
  assertEq (diffs [1, 3, 6]) [2, 3] "diffs failed"
  assertEq (allZeros [0, 0, 0]) True "allZeros failed"
  assertEq (nextValue [0, 0, 0]) 0 "nextValue failed with sequence of zeros"
  assertEq (nextValue [0, 3, 6, 9, 12, 15]) 18 "nextValue failed with non-zero sequence"
  assertEq (nextValue [10, 13, 16, 21, 30, 45]) 68 "nextValue  failed with sample input"
  assertEq (parseLine "1 3 4") [1, 3, 4] "parseLine failed"
  assertEq (parseInput "") [] "parseInput valued with empty string"
  assertEq (parseInput "3\n4") [[3], [4]] "parseInput valued with basic string"
  assertEq (parseInput "") [] "parseInput valued with empty string"
  assertEq (firstValue [10, 13, 16, 21, 30, 45]) 5 "firstValue failed with sample input"
