main = do
    let ngto = [2,3,5,7,11,13,17]
    let n = 10
    let ngto_filtered = [x | x <- ngto, x <= n]
    print(ngto_filtered)