data Signal = Red | Yellow | Green deriving (Eq, Show, Ord)
stopWhen :: Signal -> Bool
stopWhen Red = True
stopWhen c = False

stopWhen2 :: Signal -> Bool
stopWhen2 c | (c == Red) = True
            | otherwise = False

nextlight :: Signal -> Signal
nextlight Green = Yellow
nextlight Yellow = Red
nextlight Red = Green