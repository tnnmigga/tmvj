def minimum_edit_distance(code_1: str, code_2: str):
    '''
    最短编辑距离计算，参数为将要计算的两端代码，返回两段代码的最短编辑距离
    '''
    dp = [[0 for i in range(len(code_1) + 5)] for j in range(len(code_2) + 5)]
    for i in range(len(code_1) + 1): dp[0][i] = i
    for i in range(len(code_2) + 1): dp[i][0] = i
    for i in range(1, len(code_2) + 1):
        for j in range(1, len(code_1) + 1):
            dp[i][j]=min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+(0 if code_1[j-1]==code_2[i-1] else 1))

    return dp[len(code_2)][len(code_1)]


def calc_similarity(code_1: str, code_2: str):
    '''
    返回0-1之间的一个浮点数代表相似度，1为百分百相似
    '''
    code_1.replace(' ', '')
    code_1.replace('\t', '')
    code_1.replace('\r', '')
    code_1.replace('\n', '')
    code_2.replace(' ', '')
    code_2.replace('\t', '')
    code_2.replace('\r', '')
    code_2.replace('\n', '')
    return 1 - minimum_edit_distance(code_1, code_2) / max(len(code_1), len(code_2))
    
