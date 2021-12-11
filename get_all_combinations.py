import copy
def get_all_combinations(matrix, paths, path=[], x=0):

    if len(matrix) > x:
        for y_index, e in enumerate(matrix[x]):
            new_path = copy.deepcopy(path)
            new_path.append(matrix[x][y_index])
            get_all_combinations(matrix, x=x + 1, path=new_path, paths=paths)

    elif x == len(matrix):
        paths.append(path)



if __name__ == '__main__':
    m = [[1,2,3], [1,2], [1,2,3,4,5]]
    paths = []

    get_all_combinations(m, paths)

    print('Combinations returned by get_all_combinations: ' + str(len(paths)))
    print('actual possible combinations: ' + str(3 * 2 * 5))

    m = [[1,2], [1,2]]
    paths = []
    get_all_combinations(m, paths)

    print('Combinations returned by get_all_combinations: ' + str(len(paths)))
    print('actual possible combinations: ' + str(2 * 2))


    m = [[1,2,3,4,5,6], [1,2,3], [1,2,3,4,5,6,7,8], [1,2,3,4,5], [1,2,3,4,5,6,7,8,9]]
    paths = []
    get_all_combinations(m, paths)

    print('Combinations returned by get_all_combinations: ' + str(len(paths)))
    print('actual possible combinations: ' + str(6*3*8*5*9))