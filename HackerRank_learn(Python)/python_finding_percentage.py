if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    
    keys_list = list(student_marks)
    
    values = student_marks.values()
    values_list = list(values)

    queryIndex = keys_list.index(query_name)

    soma = 0

    for k in range(0, len(values_list[queryIndex])):
        soma += values_list[queryIndex][k]
    
    print("{:.2f}".format(soma / len(values_list[queryIndex]), 2))
