key_list = []


def dict_keys_hash_calculator(_dict):
    for key, value in _dict.items():
        if isinstance(value, dict):
            dict_keys_hash_calculator(value)
        elif isinstance(value, list):
            for item in _dict:
                if isinstance(item, dict):
                    dict_keys_hash_calculator(item)
        key_list.append(key)


# ========================================================================================================== #

x = {"x": 50}
list_for_keys = []


def find_all_keys(k):
    dict_keys = k.keys()
    list_for_keys.extend([dict_keys])
    for i in dict_keys:
        if isinstance(k[i], dict):
            return find_all_keys(k[i])
        elif isinstance(k[i], list):
            for j in k[i]:
                if isinstance(j, dict):
                    list_for_keys.extend([j])


print(list_for_keys)
# ========================================================================================================== #

count = len(x)


def get_all_keys(dict_):
    global count
    for i in dict_:
        if isinstance(dict_[i], dict):
            count += len(dict_[i])
            get_all_keys(dict_[i])
        elif isinstance(dict_[i], list):
            for j in dict_[i]:
                if isinstance(j, dict):
                    count += len(j)
                    get_all_keys(j)
    return count

# print(get_all_keys(x))
