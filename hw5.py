import pandas as pd
import matplotlib.pyplot as plt


def load_dataset(filename):
    table = pd.read_csv(filename)
    id_list = table['id'].to_list()
    virus_list = table['virus count'].to_list()
    print(table.head(4))
    print(f'The number of citizens in the database is: {len(id_list)}')
    return id_list, virus_list


def virus_count_histogram(lst, high_bound=100, low_bound=0):
    # Health Ministry informed that value range is [0,100]
    hist = [0 for _ in range(high_bound - low_bound + 1)]  # actually range(101) ☝.
    for persons_v_antibodies_count in lst:
        hist[persons_v_antibodies_count] += 1
    names = [i for i in range(len(hist))]
    plt.bar(names, hist)
    #print(names)
    plt.show()


def custom_histogram(lst, high_bound=101, low_bound=0, step=10):
    hist = [0] * ((high_bound - low_bound) // step + 1)
    for y in lst:
        hist[y // step] += 1
    names = [''] * len(hist)
    for i in range(len(hist) - 1):
        names[i] = str(i * step) + '-' + str((i + 1) * step - 1)
    names[-1] = (str((len(hist) - 1) * step) + '-') * (high_bound % step != 0) + str(high_bound)
    plt.bar(names, hist)
    plt.xticks(rotation='vertical')
    plt.show()


def sick_families(id_list, virus_list, virus_count):
    hist = [[0, [], []] for _ in range(100)]
    out = []
    # sort = [0 for _ in range(100)]
    for i, idtt in enumerate(id_list):
        hist[(idtt % 1000) // 10][1].append(virus_list[i])
        hist[(idtt % 1000) // 10][2].append(idtt)
        if virus_list[i] >= virus_count:
            hist[(idtt % 1000) // 10][0] += 1
    for i in range(100):
        if hist[i][0] == 0:
            continue
        elif hist[i][0] == 1:
            for j in range(len(hist[i][2])):
                if j == 0:
                    print(f'Sick citizen found: {hist[i][2][j]}, number of virus: {hist[i][1][j]}')
                else:
                    print(f'        Family member: {hist[i][2][j]}, number of virus: {hist[i][1][j]}')
        else:
            out.append(i)
            for j in range(len(hist[i][2])):
                if j == 0:
                    print(f'Sick citizen found: {hist[i][2][j]}, number of virus: {hist[i][1][j]}')
                else:
                    print(f'        Family member: {hist[i][2][j]}, number of virus: {hist[i][1][j]}')
            print("                 QUARANTINE REQUIRED!")
    return out


def cure_families(id_lst, virus_lst, family_nums, high_bound, low_bound):
    cured = 0
    hist = [0] * ((high_bound - low_bound) + 1)
    for i in family_nums:
        hist[i] += 1
    for index, idtt in enumerate(id_lst):
        check = idtt % 1000 // 10
        if hist[check] == 0:
            continue
        else:
            virus_lst[index] = 0
            cured += 1
            # hist[check].append(id_lst[index])
    print(f'{cured} citizens have bean cured!')


def main():
    idtt, vi_l = load_dataset('virus.csv')
    virus_count_histogram(vi_l, 100, 0)
    step = int(input('Please insert histogram range step: '))
    custom_histogram(vi_l, 100, 0, step)
    virus_lim = int(input("Please insert virus count limit: "))
    family_nums = sick_families(idtt, vi_l, virus_lim)
    cure_families(idtt, vi_l, family_nums, 100, 0)
    custom_histogram(vi_l, 100, 0, step)


if __name__ == '__main__':
    main()
