if __name__ == "__main__":
    student_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        student_list.append(student)

    score_list = []
    for item in student_list:
        score_list.append(item[1])

    score_list = list(set(score_list))
    score_list.sort()

    output_list = []
    target_score = score_list[1]

    for item in student_list:
        if item[1] == target_score:
            output_list.append(item[0])

    output_list.sort()
    for item in output_list:
        print(item)
