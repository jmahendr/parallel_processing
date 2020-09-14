import re
import time

SOURCE_FILE = "./resources/source.txt"
INPUT_FILE = "./resources/input.txt"


def handler():
    source_names = get_name_list(SOURCE_FILE)
    input_names = get_name_list(INPUT_FILE)

    # print(f"{source_names=}")
    # print(f"{input_names=}")

    join_names_in_list(source_names)
    join_names_in_list(input_names)
    # print(f"{source_names=}")
    # print(f"{input_names=}")

    input_dict = {i: 'N' for i in input_names}
    source_dict = {i: 'N' for i in source_names}
    source_approx_dict = {
        re.sub(r"[\s-]", "", i): i for i in source_names}

    # exact match
    for key in input_dict:
        # check exact match in source_names
        if(key in source_dict):
            input_dict[key] = 'E'
            source_dict[key] = 'M'
        else:
            # approximate match
            approx_input = re.sub(r"[\s-]", "", key)
            if approx_input in source_approx_dict:
                source_key = source_approx_dict[approx_input]
                input_dict[key] = 'A'
                source_dict[source_key] = 'M'

    unmatched_source_dic = {key: value for (
        key, value) in source_dict.items() if (value) == 'N'}
    if(len(unmatched_source_dic) > 0):
        complete_match = False
    else:
        complete_match = True

    print(complete_match)
    print(input_dict)


def get_name_list(file_name):
    name_list = []
    with open(file_name) as reader:
        for line in reader:
            fragments = line.upper().split(',')
            name_list.append((
                fragments[0],
                re.sub(r"[\n]", "", fragments[1])
            ))
    # remove duplicates and return
    return list(set(name_list))


def join_names_in_list(input_list):
    for x in range(len(input_list)):
        input_list[x] = input_list[x][0] + input_list[x][1]


if __name__ == "__main__":
    st = time.perf_counter()
    handler()
    ed = time.perf_counter()
    print(ed-st)
