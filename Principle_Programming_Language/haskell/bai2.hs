app :: (a->a) -> a -> a
app f x = f (f x)
add1 :: Int -> Int
add1 x = x + 1
main = do
    print(app add1 4)
    print(app (++ "Hello") "My name is Anna")
    print(app ("Hello" ++) "My name is Anna")