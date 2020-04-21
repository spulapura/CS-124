line1 = map(int, raw_input().split())
line2 = map(int, raw_input().split())
line3 = map(int, raw_input().split())


class Node: 
    def __init__(self,t,p): 
        self.left = None
        self.right = None
        self.tscore = t
        self.pairs = p


def bst(tree, tscore, pairs):
	if tree == None:
		tree = Node(tscore,0)
		return tree, pairs
	else:
		if tree.tscore <= tscore:
			tree.pairs += 1
			if tree.right == None:
				tree.right = Node(tscore,0)
				return tree, pairs
			else:
				tree.right, pairs = bst(tree.right, tscore, pairs)
				return tree, pairs
		else:
			if tree.left == None:
				tree.left = Node(tscore,0)
				return tree, pairs+tree.pairs+1
			else:
				tree.left,pairs = bst(tree.left, tscore,pairs)
				return tree, pairs+tree.pairs+1


def find_nsquare(str1, ten, maj):
    valid_pair = 0
    for i in range(0, str1[0]):
        for j in range(i, str1[0]):
            if(ten[j] < ten[i]):
                if(maj[j] != maj[i]):
                    valid_pair+=1
    return valid_pair



if(line1[0] == line1[1]):
    tree = None
    pairs = 0
    for score in line2:
        tree, pairs = bst(tree, score, pairs)
    print pairs

else:
    print find_nsquare(line1, line2, line3)