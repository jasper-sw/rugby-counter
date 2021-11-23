import csv


class Person:
    name = None
    phone_number = None
    grey_ball_count = None
    tan_ball_count = None
    contacted_once = None
    has_paid = None
    amount_paid = None
    contacted_twice = None

    def __init__(self, columns_dict, row):
        self.name = row[columns_dict["Name"]]
        self.phone_number = row[columns_dict["Number"]]
        self.grey_ball_count = row[columns_dict["Grey Ball Count"]]
        self.tan_ball_count = row[columns_dict["Tan Ball Count"]]
        if row[columns_dict["Contacted Once"]] == "yes":
            self.contacted_once = True
        elif row[columns_dict["Contacted Once"]] == "no":
            self.contacted_once = False
        if row[columns_dict["Contacted Twice"]] == "yes":
            self.contacted_once = True
        elif row[columns_dict["Contacted Twice"]] == "no":
            self.contacted_once = False
        if row[columns_dict["Paid"]] == "yes":
            self.contacted_once = True
        elif row[columns_dict["Paid"]] == "no":
            self.contacted_once = False


class RugbyCounter:
    filepath: str
    data_entries = []
    players_list = []
    venmo_payments = {}
    total_line_count = 0
    hoodies_dict = None
    t_shirts_dict = None
    sweatpants_dict = None
    polos_dict = None
    rugby_shorts_dict = None

    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):
        with open(self.filepath, 'r', encoding="utf-8") as csv_file:
            file_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            columns_dict = {}
            for row in file_reader:
                if line_count == 0:
                    for column in row:
                        columns_dict[column] = list(row).index(column)
                    line_count += 1
                    self.total_line_count += 1
                else:
                    self.data_entries.append(row)
                    self.players_list.append(Person(columns_dict=columns_dict, row=row))
                    self.venmo_payments[row[columns_dict["Venmo payment name"]]] = row[columns_dict["Venmo payment amount"]]
                    line_count += 1
                    self.total_line_count += 1


c = RugbyCounter(filepath="updated/ball_order_updated.csv")
c.read_file()

for person in c.players_list:
    if person.tan_ball_count != '':
        person.tan_ball_count = int(person.tan_ball_count)
    if person.grey_ball_count != '':
        person.grey_ball_count = int(person.grey_ball_count)

    try:
        venmo_payment = c.venmo_payments[person.name]
        if venmo_payment == '':
            venmo_payment = "NOT PAID"
        else:
            venmo_payment = int(venmo_payment)
            if person.grey_ball_count != '' and person.tan_ball_count != '':
                total_owed = ((person.grey_ball_count + person.tan_ball_count) * 23) - venmo_payment
            else:
                total_owed = ""
    except KeyError:
        venmo_payment = "NOT PAID"
        total_owed = (int(person.grey_ball_count) + int(person.tan_ball_count)) * 23

    if total_owed > 1:
        print("[{}] ordered [{}] grey balls and [{}] tan balls, "
              "they owe $[{}] and have paid $[{}]. They still owe $[{}]".format(person.name,
                                                                                person.grey_ball_count,
                                                                                person.tan_ball_count,
                                                                                ((person.grey_ball_count+person.tan_ball_count) * 23),
                                                                                venmo_payment, total_owed))

