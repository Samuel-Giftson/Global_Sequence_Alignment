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

        # Indexs it shouldn't pivot around

        self.main_list, self.no_pivot_index = self.form_table()
        # print(self.no_pivot_index)
        self.main_list = self.populate_table_gap_penalty_value()

        self.calculate_table_values()

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
            # print(i, loop_amount)
            x_ = x_ + loop_variant
            y_ = x_ + 1
            # no_pivot_index.append(x_)
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

        side_pivot1 = main_pivot + side_pivot
        temp_gap_penalty = 0
        print("pivot main_pivot side_pivot side_pivot1")
        if (len(self.first_strand) < len(self.second_strand)):
            for j in range(side_pivot - 1):
                print(pivot, main_pivot, side_pivot, side_pivot1)
                self.main_list[side_pivot1] = temp_gap_penalty + gap_penalty
                # print(side_pivot1, temp_gap_penalty, gap_penalty)
                side_pivot1 = side_pivot1 + side_pivot
                temp_gap_penalty = temp_gap_penalty + gap_penalty
            return self.main_list
        elif (len(self.first_strand) > len(self.second_strand)):
            for j in range(side_pivot - 3):
                print(pivot, main_pivot, side_pivot, side_pivot1)
                self.main_list[side_pivot1] = temp_gap_penalty + gap_penalty
                # print(side_pivot1, temp_gap_penalty, gap_penalty)
                side_pivot1 = side_pivot1 + side_pivot
                temp_gap_penalty = temp_gap_penalty + gap_penalty
            return self.main_list

    def calculate_table_values(self):
        #Necessary Basic values needed for calaculation
        gap_penalty = -1 * self.gap_penalty  #Used only for box 1 depends on situation
        mismatch = self.mismatch        #messes with both box 2 and box 3
        any_match = self.any_match           #Used only for box 1 depends on situation

        loop_main_pivot = self.main_pivot
        value_calculated = 0
        f_strand = list(self.first_strand)
        s_strand = list(self.second_strand)
        f_strand.insert(0, "*")
        f_strand.insert(0, "S")
        s_strand.insert(0, "*")
        s_strand.insert(0, "S")

        f_strand_index = 0
        s_strand_index = 0

        #        f_strand_index = 0
        #        s_strand_index = 0
        no_index_index_value = self.no_pivot_index[0]

        #temp list of value to put all box values and get the greatest value out for box 4 value
        temp_list_box_value = []

        for i in range(len(self.main_list)):
            if loop_main_pivot <= (len(self.main_list) - 1):
                if self.main_list[loop_main_pivot] == " ":
                    temp_list_box_value = []
                    print(loop_main_pivot, f_strand_index, s_strand_index, f_strand, s_strand)
                    ###f_strand_index = f_strand_index + 1
                    # ________________
                    # | box1  | box2 |
                    # |-------|------|
                    # | box3  | box4 |
                    # ---------------|

                    box1_value = self.main_list[loop_main_pivot - self.main_pivot]
                    box1_value_to_sum = 0
                    print(f_strand[f_strand_index], s_strand[s_strand_index])
                    if f_strand[f_strand_index+1] == (s_strand[s_strand_index+1]):
                        box1_value_to_sum = any_match
                    elif(f_strand[f_strand_index+1] != s_strand[s_strand_index+1]):
                        box1_value_to_sum = mismatch

                    box1_value_summed = box1_value + box1_value_to_sum
                    f_strand_index = f_strand_index + 1



                    # Diagonal Boxes only sumed with Gap penalty
                    box2_value = self.main_list[loop_main_pivot - (self.main_pivot - 1)]
                    box3_value = self.main_list[loop_main_pivot - 1]
                    box2_value_summed = box2_value + gap_penalty
                    box3_value_summed = box3_value + gap_penalty
                    temp_list_box_value=[box1_value_summed, box2_value_summed, box3_value_summed]
                    box4_value = max(temp_list_box_value)
                    #print("loop_main_pivot: "+str(loop_main_pivot),"f_s_index: "+str(f_strand_index),"s_s_index: "+str(s_strand_index), f_strand, s_strand)
                    #print(temp_list_box_value)
                    #print("box 1 value: "+str(box1_value), "box1 value to sum: "+str(box1_value_to_sum), "box1 value summed"+str(box1_value_summed))
                    #print(box2_value_summed)
                    #print(box3_value_summed)
                    self.main_list[loop_main_pivot] = box4_value

                if ((loop_main_pivot in self.no_pivot_index) and (loop_main_pivot > no_index_index_value)):
                    no_index_index_value = loop_main_pivot
                    f_strand_index = 1
                    s_strand_index = s_strand_index + 1

            loop_main_pivot = loop_main_pivot + 1

        print(self.main_list)
