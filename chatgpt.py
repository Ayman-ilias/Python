class Star_Cinema:
    __hall_list = []

    def entry_hall(cls, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.hall_no = hall_no

        
        for i in range(rows):
            for j in range(cols):
                self.__seats[(i, j)] = 0

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)

        # Initialize seats for the show with 0 (available)
        self.__seats[id] = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]


    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print("Invalid show ID.")
            return

        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print("Invalid seat coordinates.")
            elif self.__seats[id][row][col] == 1:
                print("Seat already booked.")
            else:
                self.__seats[id][row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid show ID.")
            return

        print(f"Available seats for Show ID {id}:")
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0:
                    print(f"Row {i}, Col {j}")


# # Example usage:
if __name__ == "__main__":
    hall1 = Hall(3, 4, 1)
    hall2 = Hall(4, 5, 2)

    hall1.entry_show(1, "Movie A", "12:00 PM")
    hall2.entry_show(2, "Movie B", "3:00 PM")

    hall1.view_show_list()
    hall2.view_show_list()

    hall1.book_seats(0, [(0, 0), (0, 1), (1, 1)])
    hall1.view_available_seats(1)
