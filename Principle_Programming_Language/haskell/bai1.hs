app :: (a->a) -> a -> a
app f x = f x

main = do
    print(app (++ "Hello") "My name is Anna")
    print(app ("Hello" ++) "My name is Anna")