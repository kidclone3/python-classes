data Shape = Circle {radius :: Float}
            | Rectangle {height :: Float, width :: Float}
            | Square {edge :: Float}
    deriving (Eq)
getArea :: Shape -> Float
getArea (Circle r)  = r * r * 3.14
getArea (Rectangle h w) = h * w 
getArea (Square e) = e*e

isRound :: Shape -> Bool
isRound (Circle r ) = True
isRound c = False