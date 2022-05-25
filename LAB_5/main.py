from func import Parallelogram, Rectangle, Square, enter_points

def main():
    n = int(input("Number of quadrangles: "))
    s_sum = 0
    p_sum = 0
    for i in range(n):
        choice = (input("Enter 'p' for parallelogram, 'r' for rectangle or 's' for square: "))
        while choice not in ['p', 'r', 's']:
            choice = (input("Incorrect input. Enter 'p' for parallelogram, 'r' for rectangle or 's' for square: "))
        print("Enter coordinates clockwise, starting with the left upper corner.")
        points = enter_points()
        if choice == 'p':
            obj = Parallelogram(points)
            p_sum += obj.get_p()
        elif choice == 'r':
            obj = Rectangle(points)
            s_sum += obj.get_s()
        else:
            obj = Square(points)
            s_sum += obj.get_s()
        print(f"P: {obj.get_p()}\nS: {obj.get_s()}")
    print(f"Sum of P of all the parallelograms: {p_sum}")
    print(f"Sum of S of all the squares and rectangles: {s_sum}")


if __name__ == "__main__":
    main()