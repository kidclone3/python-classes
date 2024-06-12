main = do
    let adjs = ["red", "blue", "black", "yellow"]
    let nouns = ["car", "bicycle"]
    let new = [(x,y) | x <- adjs, x /= "red", y <- nouns, y /= "car"]
    print(new)