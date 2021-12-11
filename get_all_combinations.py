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
    x = 0

    get_all_combinations(m, paths)

    print(paths)