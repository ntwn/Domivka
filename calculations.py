class Calculate:

    def __init__(self, list_of_residents, area_of_resident):
        pass
        self.l_of_res = list_of_residents
        self.area = 0
        self.area_of_resident = area_of_resident

    def select_area(self):
        pass

    def calculate_percent_of_area_vote_za(self):
        for i in range(self.l_of_res):
            if i == "1":
                self.area += self.area_of_resident(i)
        return self.area
        pass

    def calculate_percent_of_residents_vote_za(self):
        pass

