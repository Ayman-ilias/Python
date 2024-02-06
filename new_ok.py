class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def book_seats(self, id, seat_list):
        if id not in self.seats:
            print("Invalid show ID")
        
        seats_available = True
        for seat in seat_list:
            row, col = seat
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print("Invalid seat")
            
            if self.seats[id][row][col] == 1:
                seats_available = False
                break
        
        if not seats_available:
            print("Seat already booked")
        
        for seat in seat_list:
            row, col = seat
            self.seats[id][row][col] = 1

    def view_show_list(self):
        return self.show_list

    def view_available_seats(self, id):
        if id not in self.seats:
            print("Invalid show ID")
        
        return self.seats[id]