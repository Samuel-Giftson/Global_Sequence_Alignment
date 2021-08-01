from displayTable import DisplayTable as display
from userErrorChecking import UserErrorChecking as error_check
from tableCalculation import TableCalculation as table_calculate


def main():
    print("Welcome to Global Sequence Alignment Simulator")
    error_check_ = error_check()
    value = ""
    while (True):
        try:
            first_strand = input("Please type in your first strand: ")
            value = error_check_.check_strand(first_strand)
            if not value:
                print("Strand should contain letters A T C G only.")
                print("Please Re-enter the strand.")
                print(" ")
                continue

            second_strand = input("Please type in your second strand: ")
            value = error_check_.check_strand(second_strand)
            if not value:
                print("Strand should contain letters A T C G only.")
                print("Please Re-enter the strand.")
                print(" ")
                continue

            elif value:
                break
        except:
            print("Unexpected Error Occured, Please Re-type strand")



    print(" ")
    while(True):
        print("Type in scores.")
        try:
            gap_penalty = int(input("Gap Penalty: "))
            print(" ")
        except ValueError:
            print("Gap Penalty must be a integer")
            print(" ")
            continue
        try:
            mismatch = int(input("Mismatch: "))
            print(" ")
        except ValueError:
            print("Mismatch must be a integer")
            print(" ")
            continue

        try:
            any_match = int(input("Any match: "))
            print(" ")
        except ValueError:
            print("Any match must be a integer")
            print(" ")
            continue

        break
    main_table = table_calculate(first_strand, second_strand, gap_penalty, mismatch, any_match)
#    x = display("e")

main()
