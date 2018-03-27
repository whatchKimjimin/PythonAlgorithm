#-*- coding: utf-8 -*-

'''

문제
세준시에는 고층 빌딩이 많다. 세준시의 서민 김지민은 가장 많은 고층 빌딩이 보이는 고층 빌딩을 찾으려고 한다. 빌딩은 총 N개가 있는데, 빌딩은 선분으로 나타낸다. i번째 빌딩 (1부터 시작)은 (i,0)부터 (i,높이)의 선분으로 나타낼 수 있다. 고층 빌딩 A에서 다른 고층 빌딩 B가 볼 수 있는 빌딩이 되려면, 두 지붕을 잇는 선분이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다. 가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 빌딩의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에 1번 빌딩부터 그 높이가 주어진다. 높이는 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째줄에 문제의 정답을 출력한다.
'''

def ccw(x1,y1,x2,y2,x3,y3):
    temp = x1*y2+x2*y3+x3*y1
    temp = temp - y1*x2-y2*x3-y3*x1
    if (temp > 0):
        return 1
    elif (temp < 0):
        return -1
    else:
        return 0



# 빌딩 개수


buildingCount = input()

# 빌딩 높이
buildingHeight = raw_input().split()

i = 0
while buildingCount > i:
    buildingHeight[i] = int(buildingHeight[i])
    i = i + 1

ViewCountArr = []
i = 0
while buildingCount > i:
    now = buildingHeight[i]
    left = i-1
    right = i+1
    ViewCount = 0
    print(i,"===========")

    max = [0,0]
    while 0 <= left:
        if max[1] < buildingHeight[left]:
            max = [ left , buildingHeight[left] ]
            ViewCount = ViewCount + 1
            print("left",0,buildingHeight[left])
        elif ccw(i , buildingHeight[i] , max[0] , max[1] , left , buildingHeight[left]) == -1 and max[1] != buildingHeight[left]:
            ViewCount = ViewCount + 1
            print("left",1,buildingHeight[left])



        left = left - 1

    max = [0,0]
    while buildingCount-1 >= right:
        if max[1] < buildingHeight[right]:
            max = [ right , buildingHeight[right]]
            ViewCount = ViewCount + 1
            print("right",buildingHeight[right])
        elif ccw(i , buildingHeight[i] , max[0] , max[1] , right , buildingHeight[right]) == 1 and max[1] != buildingHeight[right]:
            ViewCount = ViewCount + 1
            print("right",buildingHeight[right])
        right = right + 1

    print(buildingHeight[i],"ViewCount : ",ViewCount)
    ViewCountArr.append(ViewCount)
    i = i + 1

max = 0
for data in ViewCountArr:
    if max < data:
        max = data


print(max)




# 1 5 3 2 6 3 2 6 4 2 5 7 3 1 5
