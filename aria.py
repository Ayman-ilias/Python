class Star_Cinema:
    hall_list = []

    def __init__(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = 
    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print("Invalid seat:", seat)
            elif self._seats[id][row][col] == 'Booked':
                print("Seat already booked:", seat)
            else:
                self._seats[id][row][col] = 'Booked'

    def view_show_list(self):
        print("Shows running in Hall", self._hall_no)
        for show in self._show_list:
            print("ID:", show[0])
            print("Movie Name:", show[1])
            print("Time:", show[2])
            print()

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        print("Available seats for show ID", id)
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[id][row][col] == 'Free':
                    print("Row:", row, "Col:", col)
        print()


# Example usage
hall1 = Hall(5, 5, 1)
hall2 = Hall(6, 4, 2)

cinema = Star_Cinema(hall1)
cinema.entry_hall(hall2)

hall1.entry_show("S1", "Movie 1", "10:00 AM")
hall1.entry_show("S2", "Movie 2", "2:00 PM")

hall2.entry_show("S3", "Movie 3", "6:00 PM")

hall1.book_seats("S1", [(0, 0), (2, 2)])
hall1.book_seats("S2", [(1, 1), (3, 3)])
hall1.book_seats("S3", [(4, 4)])

hall1.view_show_list()
hall1.view_available_seats("S2")