grades_data = []
while True:
    i = int(input())
#                                                   finish
    if i == 7:
        print()
        break
#                                                   add new grade
    elif i == 0:
        identity = input()
        new_grade = int(input())
        grades_data += [identity, new_grade]
#                                                   remove grade
    elif i == 1:
        identity = input()
        # ii = find(grades_data[[identity:]]) | ask for using find operation.
        if identity in grades_data:
            p = 0
            while p < len(grades_data):
                if grades_data[p] == identity:
                    del grades_data[p:p + 2]
                p += 2
        else:
            print("ERROR")
#                                                   check existence
    elif i == 2:
        identity = input()
        print(identity in grades_data)
#                                                   best students
    elif i == 3:
        x = int(input())
        p = 1
        sigmas = 0
        if x == 1:
            while p < len(grades_data):
                if grades_data[p] >= 90:
                    sigmas += 1
                p += 2
        else:
            while p < len(grades_data):
                if grades_data[p] >= 80:
                    sigmas += 1
                p += 2
        print(sigmas)
#                                                   avg
    elif i == 4:
        p = 1
        avg = 0.0
        sigmas_all = 0
        while p < len(grades_data):
            sigmas_all += grades_data[p]
            p += 2
        if len(grades_data):
            avg = (2 * sigmas_all / len(grades_data))
            print(f'{avg:.2f}')
#                                                   specific identity's
    elif i == 5:
        xx = input()
        p = 0
        while p < len(grades_data):
            if grades_data[p].endswith(xx):
                print(f'{grades_data[p]} {grades_data[p + 1]}')
            p += 2
#                                                   losers
    elif i == 6:
        pracent = 0.0
        sigmas_low_grades = 0
        p = 1
        while p < len(grades_data):
            if grades_data[p] < 55:
                pracent += 1
            p += 2
        pracent = pracent and ((pracent / len(grades_data)) * 2)
        print(f'{pracent:.2f}')
# all
    print()
