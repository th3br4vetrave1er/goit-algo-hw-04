def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_info)
    except FileNotFoundError:
        print("File not found.")
    except Exception as error_msg:
        print("An error occurred:", error_msg)
    return cats_info


cats_info = get_cats_info("C:/Users/br4vetrave1er/Desktop/projects/goit-algo-hw-04/text2.txt")
for cat in cats_info:
    print(cat)
