def find_nsquare(str1, ten, maj):
    valid_pair = 0
    for i in range(0, str1[0]):
        for j in range(i, str1[0]):
            if(ten[j] < ten[i]):
                if(maj[j] != maj[i]):
                    valid_pair+=1
                    print(i,j)
    return valid_pair

line1 = [20,20]
ten = [3, 4, 7, 4, 2, 7, 46, 12, 8, 43, 6, 2, 45, 12, 3, 32, 23, 8, 56, 1]
line3 = [3,5,1,0,3,5,2,1,0,1,2,4,3,5,5,1,2,3,2,2]
print line3
print find_nsquare(line1, ten, line3)


