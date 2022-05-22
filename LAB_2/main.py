from func import enter_mode, creating_first_file, creating_second_file, read_cars, output_used_cars


def main():
    first_path = "Allcars.bin"
    second_path = "Recentcars.bin"
    mode = enter_mode()
    creating_first_file(first_path, mode)
    creating_second_file(first_path, second_path)
    print("\nAll cars:")
    read_cars(first_path)
    print("\nRecent cars:")
    read_cars(second_path)
    output_used_cars(first_path)


if __name__ == "__main__":
    main()
