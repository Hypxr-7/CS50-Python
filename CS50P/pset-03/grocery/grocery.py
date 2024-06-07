def main():
    item_list = {}
    while True:
        try:
            item = input().strip().upper()
            if item in item_list:
                item_list[item] += 1
            else:
                item_list[item] = 1
        except EOFError:
            item_list = dict(sorted(item_list.items()))
            for key in item_list:
                print(item_list[key], key)
            break


if __name__ == "__main__":
    main()
