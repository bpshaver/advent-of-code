races = [(49, 263), (97, 1532), (94, 1378), (94,1851)]

listDistances totalTime = [ (totalTime - t) * t | t <- [0..totalTime]]

listWinningTimes totalTime distance = filter (> distance) (listDistances totalTime)

numWinningTimes totalTime distance = length (listWinningTimes totalTime distance)

partOne = product(map (uncurry numWinningTimes) races)

partTwo = numWinningTimes 49979494 263153213781851

main = do
  print partOne

  print partTwo

