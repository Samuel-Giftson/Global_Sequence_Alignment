class TableCalculation:
    def __init__(self, first_strand, second_strand, gap_penalty, mismatch, any_match):
        self.first_strand = first_strand
        self.second_strand = second_strand
        self.gap_penalty = gap_penalty
        self.mismatch = mismatch
        self.any_match = any_match

        # Initializing pivots
        self.pivot = len(self.first_strand) - 1 + 2
        self.main_pivot = self.pivot + 2
        self.side_pivot = self.pivot + 1

        #Indexs it shouldn't pivot around

        self.main_list, self.no_pivot_index = self.form_table()
        self.main_list = self.populate_table_gap_penalty_value()

        print(self.main_list)

    def form_table(self):
        main_list = []

        # This section is to get a list of indexes it shouldn't calculate
        x_ = self.pivot
        y_ = x_ + 1
        loop_variant = self.pivot + 1
        no_pivot_index = [x_, y_]
        loop_amount = len(self.second_strand) + 1
        for i in range(loop_amount):
            #print(i, loop_amount)
            x_ = x_ + loop_variant
            y_ = x_ + 1
            no_pivot_index.append(x_)
            no_pivot_index.append(y_)

        del no_pivot_index[-1]

        # Forming the main list
        for j in range(((len(self.first_strand) + 2) * (len(self.second_strand) + 2))):
            if (j == 0):
                main_list.append("S")
            elif (j == 1):
                main_list.append("*")
            elif (j == (len(self.first_strand)) + 2):
                main_list.append("*")
            else:
                main_list.append(" ")

        # Editing the main list and adding the Letters in
        for k in range(len(self.first_strand)):
            main_list[k + 2] = self.first_strand[k]

        for j in range(len(self.second_strand)):
            main_list[(j + 2) * (self.pivot + 1)] = self.second_strand[j]

        return main_list, no_pivot_index

    def populate_table_gap_penalty_value(self):

        gap_penalty = -1 * (self.gap_penalty)
        main_pivot = self.main_pivot
        pivot = self.pivot
        side_pivot = self.side_pivot
        temp_gap_penalty = 0

        self.main_list[main_pivot + 0] = 0
        for i in range(pivot - 1):
            i = i + 1
            self.main_list[main_pivot + i] = temp_gap_penalty + gap_penalty
            temp_gap_penalty = temp_gap_penalty + gap_penalty

        side_pivot1 = main_pivot +side_pivot
        temp_gap_penalty = 0
        print("pivot main_pivot side_pivot side_pivot1")
        if(len(self.first_strand)<len(self.second_strand)):
            for j in range(side_pivot - 1):
                print(pivot, main_pivot, side_pivot, side_pivot1)
                self.main_list[side_pivot1] = temp_gap_penalty + gap_penalty
                #print(side_pivot1, temp_gap_penalty, gap_penalty)
                side_pivot1 = side_pivot1 + side_pivot
                temp_gap_penalty = temp_gap_penalty + gap_penalty
            return self.main_list
        elif(len(self.first_strand)>len(self.second_strand)):
            for j in range(side_pivot - 3):
                print(pivot, main_pivot, side_pivot, side_pivot1)
                self.main_list[side_pivot1] = temp_gap_penalty + gap_penalty
                # print(side_pivot1, temp_gap_penalty, gap_penalty)
                side_pivot1 = side_pivot1 + side_pivot
                temp_gap_penalty = temp_gap_penalty + gap_penalty
            return self.main_list

    def calculate_table_values(self):
        pass