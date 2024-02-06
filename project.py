class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)

class Hall(Star_Cinema):
    def __init__(self):
        self.entry_hall()
        self.show_list=[]
        self.seats={}

    def entry_show(self, id, movie_name, time):
        hall.show_list.append(id, movie_name, time)

        self.seats[id] = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]

    def book_seats(self, id, seat_list):
        for seat in seat_list:
            row, col = seat
            seats[id][row][col] = 1

    def view_show_list(self):
        for show in show_list:
            id, movie_name, time = show
            print(f"ID: {id}, Movie Name: {movie_name}, Time: {time}")

    def view_available_seats(self, id):
        for row in range(len(seats[id])):
            for col in range(len(seats[id][row])):
                seat_status = "Booked" if seats[id][row][col] == 1 else "Available"
                print(f"Row: {row}, Col: {col}, Status: {seat_status}")

# Example usage:
hall = Hall()
hall.entry_show(1, "Movie A", "10:00 AM")
hall.entry_show(2, "Movie B", "1:00 PM")

hall.view_show_list()

hall.book_seats(1, [(0, 0), (1, 2)])
hall.book_seats(2, [(2, 1), (0, 3)])

hall.view_available_seats(1)
hall.view_available_seats(2)