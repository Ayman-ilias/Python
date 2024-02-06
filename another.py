class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.Star.__hall_list.append(hall)

    def view_all_shows(self):
        for hall in self.__class__.__hall_list:
            hall.view_show_list()

    def view_available_seats(self, hall_no):
        for hall in self.__class__.__hall_list:
            if hall.hall_no == hall_no:
                hall.view_available_seats()
                return print(f"Hall with number {hall_no} not found.")

    def book_tickets(self, hall_no, show_id, seats):
        for hall in self.__class__.__hall_list:
            if hall.hall_no == hall_no:
                hall.book_seats(show_id, seats)
                return print(f"Hall with number {hall_no} not found.")


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
       
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().__init__()

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)

        seats = []
        for _ in range(self.__rows):
            seats.append([0] * self.__cols)

        self.__seats[id] = seats

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print(f"Invalid show ID: {id}")
            return

        seats = self.__seats[id]

        for seat in seat_list:
            row, col = seat

            if not self.__is_seat_valid(row, col):
                print(f"Invalid seat: [{row}][{col}]")
                continue

            if seats[row][col] == 1:
                print(f"Seat [{row}][{col}] is already booked")
            else:
                seats[row][col] = 1

    def view_show_list(self):
        print(f"Hall Number: {self.__hall_no}")
        for show in self.__show_list:
            id, movie_name, time = show
            print(f"ID: {id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self):
        for id, seats in self.__seats.items():
            print(f"Show ID: {id}")
            for row in range(len(seats)):
                for col in range(len(seats[row])):
                    if seats[row][col] == 0:
                        print(f"Seat [{row}][{col}]: Available")
                    else:
                        print(f"Seat [{row}][{col}]: Booked")

    def __is_seat_valid(self, row, col):
        return 0 <= row < self.__rows and 0 <= col < self.__cols


# Replica System
cinema = Star_Cinema()

# Create halls
hall1 = Hall(5, 5, 1)
hall2 = Hall(6, 4, 2)
hall3 = Hall(7, 6, 3)

# Add halls to <link>Star_Cinema</link>
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)
cinema.entry_hall(hall3)

# Entry shows
hall1.entry_show("S1", "Movie 1", "10:00 AM")
hall1.entry_show("S2", "Movie 2", "2:00 PM")

hall2.entry_show("S3", "Movie 3", "5:00 PM")
hall2.entry_show("S4", "Movie 4", "8:00 PM")

hall3.entry_show("S5", "Movie 5", "11:00 AM")
hall3.entry_show("S6", "Movie 6", "4:00 PM")

# View all shows
cinema.view_all_shows()

# View available seats in a show
cinema.view_available_seats(2)

# Book tickets
cinema.book_tickets(1, "S1", [(0, 0), (1, 1), (2, 2)])
cinema.book_tickets(2, "S3", [(5, 1), (1, 3), (3, 2)])
cinema.book_tickets(3, "S7", [(3, 3)])

# View available seats again
cinema.view_available_seats(2)