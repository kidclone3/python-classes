main = do
    let filtered = filter (\x -> x > 5) [x | x <- [1..6]]
    print(filtered)