import csv


class Player:
    name = None
    a_number = None
    email = None
    sweatpants_size = None
    rugby_shorts_size = None
    hoodie_size = None
    polo_size = None
    t_shirt_size = None
    time_answered = None

    def __init__(self, columns_dict, row):
        self.email = row[columns_dict["Email"]]
        self.name = row[columns_dict["Name"]]
        self.a_number = row[columns_dict["A-Number"]]
        self.hoodie_size = row[columns_dict["Hoodie Size"]]
        self.sweatpants_size = row[columns_dict["Sweatpants Size"]]
        self.polo_size = row[columns_dict["Polo Size"]]
        self.rugby_shorts_size = row[columns_dict["Rugby Shorts Size"]]
        self.t_shirt_size = row[columns_dict["T-Shirt Size"]]


class RugbyCounter:
    filepath: str
    data_entries = []
    players_list = []
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
                    self.players_list.append(Player(columns_dict=columns_dict, row=row))
                    line_count += 1
                    self.total_line_count += 1

    def count_stuff(self):
        hoodies_dict = {}
        t_shirts_dict = {}
        sweatpants_dict = {}
        polos_dict = {}
        rugby_shorts_dict = {}

        for player in self.players_list:
            if not hoodies_dict.keys().__contains__(player.hoodie_size):
                hoodies_dict[player.hoodie_size] = 1
            else:
                hoodies_dict[player.hoodie_size] += 1

            if not t_shirts_dict.keys().__contains__(player.t_shirt_size):
                t_shirts_dict[player.t_shirt_size] = 1
            else:
                t_shirts_dict[player.t_shirt_size] += 1

            if not sweatpants_dict.keys().__contains__(player.sweatpants_size):
                sweatpants_dict[player.sweatpants_size] = 1
            else:
                sweatpants_dict[player.sweatpants_size] += 1

            if not polos_dict.keys().__contains__(player.polo_size):
                polos_dict[player.polo_size] = 1
            else:
                polos_dict[player.polo_size] += 1

            if not rugby_shorts_dict.keys().__contains__(player.rugby_shorts_size):
                rugby_shorts_dict[player.rugby_shorts_size] = 1
            else:
                rugby_shorts_dict[player.rugby_shorts_size] += 1

        self.hoodies_dict = hoodies_dict
        self.sweatpants_dict = sweatpants_dict
        self.t_shirts_dict = t_shirts_dict
        self.polos_dict = polos_dict
        self.rugby_shorts_dict = rugby_shorts_dict

    def print_count(self):
        print("Processed [{}] total lines from file [\'{}\']".format(self.total_line_count, self.filepath))
        print("Totals: ")
        print("Hoodies: ")
        for size in self.hoodies_dict.keys():
            print("\tSize: [\'{}\'], count: [{}]".format(size, self.hoodies_dict[size]))
        print("---------------------------------------")
        print("Sweatpants: ")
        for size in self.sweatpants_dict.keys():
            print("\tSize: [\'{}\'], count: [{}]".format(size, self.sweatpants_dict[size]))
        print("---------------------------------------")
        print("T-Shirts: ")
        for size in self.t_shirts_dict.keys():
            print("\tSize: [\'{}\'], count: [{}]".format(size, self.t_shirts_dict[size]))
        print("---------------------------------------")
        print("Polos: ")
        for size in self.polos_dict.keys():
            print("\tSize: [\'{}\'], count: [{}]".format(size, self.polos_dict[size]))
        print("---------------------------------------")
        print("Rugby Shorts: ")
        for size in self.rugby_shorts_dict.keys():
            print("\tSize: [\'{}\'], count: [{}]".format(size, self.rugby_shorts_dict[size]))
        print("---------------------------------------")

rc = RugbyCounter(filepath="Rugby_Gear_Form.csv")
rc.read_file()
rc.count_stuff()
rc.print_count()






