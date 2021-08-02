import xlwt


class DisplayTable:
    def __init__(self, data, f_strand, s_strand):

        self.data = data
        self.f_strand = f_strand
        self.s_strand = s_strand

        self.add_data_to_file()

    def add_data_to_file(self):
        f_strand = list(self.f_strand)
        s_strand = list(self.s_strand)
        f_strand.insert(0, "*")
        f_strand.insert(0, "S")
        s_strand.insert(0, "*")
        s_strand.insert(0, "S")

        workbook = xlwt.Workbook(encoding="utf-8")
        Data_sheet = workbook.add_sheet("Data Sheet")

        max_columns = len(f_strand) #+ 1

        max_row = len(s_strand)

        rows = 0
        columns = 0
        main_index = 0
        while rows < max_row:
            while columns < max_columns:
                Data_sheet.write(rows, columns, self.data[main_index])
                columns = columns + 1
                main_index = main_index + 1
            columns = 0
            rows = rows + 1

        workbook.save("Python Data Sheet.xls")
        print("Done, look in the directory where you ran the code,  you should have an excel sheet that contains the "
              "table.")
