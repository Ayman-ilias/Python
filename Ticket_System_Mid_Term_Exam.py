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
        for i in range(self.rows):
            for j in range(self.cols):
                self.seats[(i, j)] = 0
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        id_name_time = (id, movie_name, time)
        self.show_list.append(id_name_time)
        self.seats[id] = [[0] * self.cols for i in range(self.rows)]

    def book_seats(self, id, seat_list):
        if id not in self.seats:
            print(f"ID {id} is Invalid!!")
        else:
            seats_available = True
            for seat in seat_list:
                row, col = seat
                if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    print(f"Invalid seat {seat}")
                    seats_available = False
                    break

                if self.seats[id][row][col] == 1:
                    seats_available = False
                    print(f"Sorry..seat {seat} already booked")
                    break

            if seats_available:
                for seat in seat_list:
                    row, col = seat
                    self.seats[id][row][col] = 1
                    print(f"Seat {seat} booked successfully")

    def view_show_list(self):
        for i in self.show_list:
            print(f"ID: {i[0]}, Movie Name: {i[1]}, Time: {i[2]}")

    def view_available_seats(self, id):
        if id not in self.seats:
            print("Invalid ID!!!")
        else:
            print("Seat allocations:")
            print("0 = available   1 = booked")
            for i in self.seats[id]:
                print(i)


cinema = Star_Cinema()
hall1 = Hall(5, 5, 1)
cinema.entry_hall(hall1)

hall1.entry_show("1", "hehe", "10:00 AM")
hall1.entry_show("2", "huhu", "3:00 PM")
hall1.entry_show("3", "haha", "6:00 PM")

while True:
    print("Options:\n")
    print("1: View All Shows Today")
    print("2: View Available Seats")
    print("3: Book Tickets")
    print("4: Exit")
    ch = int(input("\nEnter Option: "))
    
    if ch == 1:
        hall1.view_show_list()
    elif ch == 2:
        d = input("\nEnter Movie ID: ")
        hall1.view_available_seats(d)
    elif ch == 3:
        c = input("\nEnter Movie ID: ")
        n = int(input("\nEnter the quantity: "))
        data = []
        for i in range(n):
            x = int(input("Enter Seat Row: "))
            y = int(input("Enter Seat Col: "))
            data.append((x, y))
        hall1.book_seats(c, data)
    elif ch ==4:
        break
    
