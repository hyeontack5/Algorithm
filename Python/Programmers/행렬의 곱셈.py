def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))] # arr1의 행과 arr2의 열을 행렬로 만듬
    
    for i in range(len(arr1)):  # arr1의 행 갈아만큼 반복
        for j in range(len(arr2[0])): # arr2의 열 길이만큼 반복
            for k in range(len(arr1[0])): # arr1의 열 길이만큼 반복
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer