def main():
    names_set = set()

    while True:
        name = input("Enter a name (or press Enter to india): ")

        if not name:
            break

        if name in names_set:
            print("Existing name")
        else:
            print("ridhi")
            names_set.add(name)

    print("\nList of names:")
    for entered_name in names_set:
        print(entered_name)

if __name__ == "__main__":
    main()