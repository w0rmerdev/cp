def main():
    number_students = int(input()) #numero de estudantes (tamanho do array)
    students = [] #array com os nomes dos estudantes e as respetivas notas
    grades = set() #notas dos estudantes

    for i in range(number_students):
        name = str(input()) #for loop para receber os nomes dos estudantes
        grade = float(input()) #notas dos estudantes
        grades.add(grade) #adiciona as notas ao array das notas
        students.append([name, grade]) #adiciona ao array dos estudantes o nome e a respetiva nota

    second_lowest_grade = sorted(grades)[1] #encontra a nota mais baixa
    second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_grade]) #com a segunda melhor nota encontra os alunos que tiveram essas notas e organiza os nomes destes por ordem alfabética
    for student in second_lowest_students:
        print(student) #mostra ao utilizador estes alunos

if __name__ == '__main__':
    main()
