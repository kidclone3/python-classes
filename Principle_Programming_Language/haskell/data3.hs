data BinaryTree a = Empty | Node (BinaryTree a) a (BinaryTree a)
                    deriving (Eq, Ord, Show)
depthTree :: BinaryTree a -> Int
depthTree (Empty) = 0
-- depthTree (Node left _ right) = 1 + maximum([depthTree left, depthTree right])
depthTree (Node left _ right) = 1 + max (depthTree left) (depthTree right)

preorderTree :: BinaryTree a -> [a]
preorderTree Empty = []
preorderTree (Node left val right) = val : preorderTree left ++ preorderTree right
inorderTree :: BinaryTree a -> [a]
inorderTree Empty = []
inorderTree (Node left val right) =  inorderTree left ++ [val] ++ inorderTree right
postorderTree :: BinaryTree a -> [a]
postorderTree Empty = []
postorderTree (Node left val right) =  postorderTree left ++ postorderTree right ++ [val]