module SortedListADT (SortedList, insert,delete, member) where
    data SortedList a = SL [a]
        insert :: (Ord a) => a -> SortedList a -> SortedList a
        insert x (SL xs) = SL (insert' x xs)
            where
                    insert' x [] = [x]
                    insert' x (y:ys) | x <= y = x : y : ys
                                     | otherwise = y : insert' x ys

        delete :: (Ord a) => a -> SortedList a -> SortedList a
        member :: (Ord a) => a -> SortedList a -> Bool