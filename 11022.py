import sys

T = int(sys.stdin.readline().rstrip())
i = 0

while i < T :
    i += 1
    A,B = map(int, sys.stdin.readline().rstrip().split())
    print("Case #"+ str(i) + ": " + str(A) + " + " + str(B) + " = " + str(A + B))