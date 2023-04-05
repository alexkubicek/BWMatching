import sys


def add_indices_last(raw):
    last_indices = []
    a = c = t = g = 0
    for char in raw:
        if char == 'A':
            new_char = (char, a)
            a += 1
        elif char == 'C':
            new_char = (char, c)
            c += 1
        elif char == 'T':
            new_char = (char, t)
            t += 1
        elif char == 'G':
            new_char = (char, g)
            g += 1
        else:
            new_char = ('$', 0)
        last_indices.append(new_char)
    return last_indices


def get_num_matches(last_col, last_to_first_col, string):
    top = 0
    bottom = len(last_col)-1
    while top <= bottom:
        # print("top: " + str(top) + " bottom: " + str(bottom))
        if len(string) > 0:
            symbol = string[len(string)-1]
            # print(symbol)
            string = string[:len(string)-1]
            top_index = bottom_index = None
            temp = top
            while temp <= bottom:
                # print("last col: " + last_col[temp][0])
                if str(last_col[temp][0]) == symbol:
                    if top_index is None:
                        top_index = last_col[temp]
                    bottom_index = last_col[temp]
                temp += 1
            if top_index is not None:
                # print("reassigning top and bottom")
                # print(str(top) + " " + str(bottom))
                # print(str(top_index) + " " + str(bottom_index))
                top = last_to_first_col[top_index]
                bottom = last_to_first_col[bottom_index]
                # print(str(top) + " " + str(bottom))
                # print(str(top_index) + " " + str(bottom_index))
            else:
                return 0
        # print(str(top) + " " + str(bottom))
        else:
            return (bottom - top) + 1


def bwt_matching(bwt, patterns):
    last_column = add_indices_last(bwt)
    first_column = sorted(last_column)
    last_to_first = dict()
    for tup in first_column:
        last_to_first[tup] = first_column.index(tup)
    pattern_matches = []
    for string in patterns:
        pattern_matches.append(get_num_matches(last_column, last_to_first, string))
    return pattern_matches


if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    file_input = inFile.readline()
    to_match = []
    for line in inFile:
        to_match.extend(line.split(" "))
    while file_input.endswith("\n"):
        file_input = file_input[:len(file_input)-1]
    inFile.close()
    # print(file_input)
    # print(to_match)
    answer = bwt_matching(file_input, to_match)
    f = open("output.txt", "w")
    sys.stdout = f
    for num in answer:
        print(num, end=" ")
    f.close()
