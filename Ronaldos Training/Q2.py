'''
Ronaldo was training Bruno Fernandes to make equipped for Euro cup 2020, after giving him physical training Ronaldo decided to teach Bruno Fernandes techniques and tactics. For that to check his IQ he prepared a question for him. Ronaldo asked Bruno Fernandes to remove finite number of footballs of different size from a heap from the top or bottom. Bruno Fernandes was asked to calculate the number of ways in which he can take the football such that the final heap that is left has a total sum of size of footballs instructed by Ronaldo.

(hey try to solve this problem in time complexity O(n) if you can)

Input Format

First line must contain T (number of football) Second line contains the value specified by Ronaldo (k) The third line contains N space separated positive integers (F1 -> Fn) : the size of the football from top to bottom.

Constraints

1<=T<=10^5 1<=k<=10^10 1<=Fi<=10^5

Output Format

A single positive integer: the number of ways he can remove football from the top and bottom such that the sum of the size of remaining football size = k.

Sample Input 0

5
3
1 2 3 1 2
Sample Output 0

3
Explanation 0

Here we remove {1,2} from bottom and {1,2} from top, {3,1,2} from top, {1,2,3} from bottom. Therefore 3
'''

input()
k=int(input())

ball=[int(x) for x in input().split()]
len_ball=len(ball)

ballsum=0
left,right=0,0
count=0

while right<len_ball:
    #print(left,right,ballsum)
    if ballsum == k:
        count+=1
        ballsum+=ball[right]-ball[left]
        right+=1
        left+=1
    elif ballsum<k:
        ballsum+=ball[right]
        right+=1
    else:
        ballsum-=ball[left]
        left+=1
print(count+(ballsum == k))