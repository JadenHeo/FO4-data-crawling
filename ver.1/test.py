m = "afdsafsdafsdafsdafsdafaasdadadssdds"
k = "asfdasdadaasdasd"
k_index = 0
answer = ""

for s in m:
    if k_index < len(k):
        if s != k[k_index]:
            answer += s
        else:
            k_index += 1
    else:
        answer += s
print(answer)


