class bookmymovie:
    print("\033[1m""Hello User \n")
    print("Proceed further for tickets and other stuff")
#for the option list
    def option(self):

        while True:
            print("\nChoose a no :")
            self.choice = int(input(
                "\n1. Show the seats\n2. buytickets a Ticket\n3. Statistics\n4. Show booked ticket's user info\n0. Exit\n"))

            # while(self.choice!=0):
            if self.choice == 1:
                self.available()

            elif self.choice == 2:
                self.buytickets()

            elif self.choice == 3:
                self.statistics()

            elif self.choice == 4:
                self.info()

            elif self.choice == 0:

                ans = False

                self.ex()
            else:
                print("\n HEY USER ! Invalid Input,Please try again ")

    def __init__(self):
        self.rows = int(input("       Enter the number of rows :-  "))

        self.coloumn = int(input("Enter the number of coloumns :- "))

        self.no_of_seats = self.rows * self.coloumn

        self.matrix = []

        self.scount = 0

        self.income = 0

        self.Total = 0

        self.userinfo = {}

        for i in range(self.rows):

            a = []

            for j in range(self.coloumn):

                a.append("S")

            self.matrix.append(a)

        print(end="  ")

#To show the seats available
    def available(self):
        print("\n   Cinema :\n")
        a = 0
        b = 0
        print(end="  ")
        #we need to print the updated matrix so....
        for j in range(1, self.coloumn + 1):
            b = b + 1
            print(b, end=" ")
        print()
        for i in self.matrix:
            a = a + 1
            print(a, end=" ")
            print(" ".join(i), sep=",")
#To buyy tickets (no2)
    def buytickets(self):
        a = int(input("Enter the seat no (in rows) you want to book  :- "))

        b = int(input("Enter the seat no (in coloumns) you want to book :-"))

        if self.matrix[a - 1][b - 1] == "B":

            print("The seat is already booked,please try another")

            self.option()

        elif self.no_of_seats < 60:  #will check available seats and then decide the value
            self.price = 10

            print("Ticket is for $10, do you want to buy ? Press Y/y")

        elif a < self.rows / 2:

            self.price = 10

            print("Ticket is for $10, do you want to buy? Press Y/y")

        elif a > self.rows / 2:

            self.price = 8

            print("Ticket per person is $8, do you want to buy? Press Y/y")

        self.pr = input()

        if self.pr == 'Y' or self.pr == 'y':
            dict0 = {}

            Name = input(" Enter your name\n")
            Gen = input("Enter your gender\n")
            Age = input("Enter your age\n")
            Contact = input("Enter your Contact Number\n")

            self.rows1 = a - 1

            self.coloumn1 = b - 1

            self.matrix[self.rows1][self.coloumn1] = "B"

            self.scount = self.scount + 1
            self.income = self.income + self.price

            dict0[(self.rows1 + 1), (self.coloumn1 + 1)] = list((Name, Gen, Age, Contact , self.price))
            self.userinfo.update(dict0)

            print("You've been successfully booked,Enjoy your show\n")

        else:
            print("OOPS.Booking Failed!\n")

    # To get total revenue genrated
    def total_revenue(self):

        if self.no_of_seats < 60:

            self.Total = self.no_of_seats * 10

        elif self.no_of_seats >= 60:

            for i in range(0, int(self.rows / 2)):

                c = int(self.rows / 2) * self.coloumn * 10

            for j in range(int(self.rows / 2), self.rows):

                d = int(self.rows / 2) * self.coloumn * 8

            self.Total = c + d
        return self.Total


    #  statistics(3)
    def statistics(self):

        print("Number of purchased tickets : ", self.scount)

        self.percentage = (self.scount / self.no_of_seats) * 100

        print("Percentage of Tickets Booked : ", "{:.2f}".format(self.percentage), "%") #(2f is for 2 decimal points)

        print("Current Income : $", self.income)

        k = self.total_revenue()

        print("Total Income : $", k)

    # TO GET INFO OF THE PERSON( 4)
    def info(self):
        self.check_a = int(input("Enter the row you booked\n"))

        self.check_b = int(input("Enter the coloumn you booked\n"))

        if self.matrix[self.check_a - 1][self.check_b - 1] == 'B':

            c = self.userinfo[(self.check_a, self.check_b)]

            print('Name:', c[0])
            print('Gender:', c[1])
            print('Age:', c[2])
            print('Phone no.:', c[3])
        else:
            print("This seat is not booked yet!")

    def ex(self):  # to exit press 0
        return None


bmw_obj = bookmymovie()
bmw_obj.option()

