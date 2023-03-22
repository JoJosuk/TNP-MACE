
n = int(input())
k = int(input())

balls = [int(x) for x in input().split(' ')]
ts, count = 0, 0

#Sliding Window 

# l = -1

# for r in range(len(balls)):
#     ts += balls[r]
#     if ts == k:
#         count += 1
#     while ts > k and l < r:
#         l += 1
#         ts -= balls[l]
#         if ts == k:
#             count += 1
            
# print(count)


#Hashing

d = {0: 1}


for ball in balls:
    
    ts += ball

    # The value that must be eliminated inorder to get the required sum = k
    req = ts - k

    count += d.get(req, 0)

    d[ts] = 1 + d.get(ts, 0)

print(count)
