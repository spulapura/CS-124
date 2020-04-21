line1 = map(int, raw_input().split())
line2 = map(int, raw_input().split())
line3 = map(int, raw_input().split())

def find_nsquare(str1, ten, maj):
    valid_pair = 0
    for i in range(0, str1[0]):
        for j in range(i, str1[0]):
            if(ten[j] < ten[i]):
                if(maj[j] != maj[i]):
                    valid_pair+=1
    return valid_pair


def bst(tree, score, pairs):
    if(tree[0]== None):
        tree = [score, [], 0, [], 0]
        return tree, score, pairs
    else:
        if(score >= tree[0]):
            if(tree[3] == []):
                tree[3] = [score, [], 0, [], 0]
                tree[4] += 1
                return tree, score, pairs
            else:
                tree[3], score, pairs= bst(tree[3], score, pairs)
                tree[4]+= 1
                return tree, score, pairs
        else:
            if(tree[1] == []):
                tree[1] = [score, [],0, [], 0]
                tree[2] += 1
                return tree, score, pairs+tree[4]+1
            else:
                tree[1], score, pairs = bst(tree[1], score, pairs)
                tree[2]+= 1
                return tree, score, pairs+tree[4]+1


if(line1[0] == line1[1]):
    tree = [None, None, None]
    pairs = 0
    for score in line2:
        tree, score, pairs = bst(tree, score, pairs)
    print pairs

else:
    print find_nsquare(line1, line2, line3)
                



