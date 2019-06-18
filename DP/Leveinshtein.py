#求编辑距离


'''
1,递归实现
'''
# def levenshteinDistance(str1, str2):
#     i = len(str1)
#     j = len(str2)
#     if min(i,j)== 0:
#         return max(i, j)
#     elif str1[-1] == str2[-1]:
#         return levenshteinDistance(str1[:-1],str2[:-1])
#     else:
#         return min(levenshteinDistance(str1[:-1],str2),
#                    levenshteinDistance(str1,str2[:-1]),
#                    levenshteinDistance(str1[:-1],str2[:-1])) + 1




'''
2,动态规划实现
'''

def levenshteinDistance(str1,str2):
    i = len(str1)
    j = len(str2)
    dp= [[0 for k in range(j+1)] for c in range(i+1)]
    #初始化
    for k in range(j + 1):
        dp[0][k] = k
    for c in range(i + 1):
        dp[c][0] = c



    for k in range(1, j + 1):
        for c in range(1, i + 1):
            if str1[c-1] == str2[k-1]:
                dp[c][k] = dp[c-1][k-1]
            else:
                dp[c][k] = min(dp[c-1][k],dp[c][k-1],dp[c-1][k-1]) + 1
    return dp[i][j]








print(levenshteinDistance('zhuo','zhouhui'))