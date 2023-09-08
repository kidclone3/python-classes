def stringMatchingHelper(text, pattern, start, end):
    if start > end:
        return -1
    if text[start:start+len(pattern)] == pattern:
        return start
    
    if start == end:
        return -1
    print(text[start:start+len(pattern)])

    mid = (start + end) // 2
    left = stringMatchingHelper(text, pattern, start, mid-1)
    right = stringMatchingHelper(text, pattern, mid+1, end)
    if left != -1:
        return left
    if right != -1:
        return right
    
    return -1

def stringMatching(text, pattern):
    """
    String matching using divide and conquer
    """
    # your code here
    return stringMatchingHelper(text, pattern, 0, len(text)-1)

text = "Algorithm Design and Analysis"
pattern = "Design"
print(stringMatching(text, pattern))