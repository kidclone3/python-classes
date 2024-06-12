-- app :: (a->a) -> a -> a
-- app f x = f x

-- main = do
--     let add1 = (\x -> x+1)
--     print(add1 4)
--     print(app (\x -> x+1) 1)

-- map :: (a->b) -> [a] -> [b]
-- map _ [] = []
-- map f (x:xs) = f x : map f xs

main = do 
    print(map (\(x,y) -> x * y) [(1,2), (3,4), (5,3)])
    print(filter (\x -> x > 1) [1,2,3,4,5])
    print([x*2 | x <- [1..10], x*2 >= 12])
