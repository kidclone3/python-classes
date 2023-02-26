with open('in', 'r') as f:
    for x in f.read().split():
        print("\"" + x.rstrip(",") + "\",", end = "")

