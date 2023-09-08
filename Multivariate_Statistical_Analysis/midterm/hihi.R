x <- c(1:5)
y <- c(11:15)
z <- c(21:25)

# creating matrix
m <- matrix(c(x, y), ncol = 2)

# print matrix
print(t(m))

# print class of m
class(m)