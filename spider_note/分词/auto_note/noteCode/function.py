# ´òÓ¡×Öµä
def print_dic(dic):
    for key, value in dic.items():
        print(str(key) + ": ")
        if isinstance(value,list):
            for item in value:
                print(item)
        else:
            print(str(value))