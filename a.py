class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)

class Hall:
    def __init__(self):
        self.entry_hall()

    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)

class Star_Show(Hall):
    __show_list = []

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        Star_Show.__show_list.append(show_info)

        seats = {}
        seats[id] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def book_seats(self, id, seat_list):
        selected_seats = seats[id]

        for seat in seat_list:
            row, col = seat
            selected_seats[row][col] = 1

    def view_show_list(self):
        for show in Star_Show.__show_list:
            id, movie_name, time = show
            print(f"ID: {id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, id):
        selected_seats = seats[id]

        for row in range(len(selected_seats)):
            for col in range(len(selected_seats[row])):
                if selected_seats[row][col] == 1:
                    print(f"Seat [{row+1}][{col+1}]: Booked")
                else:
                    print(f"Seat [{row+1}][{col+1}]: Available")