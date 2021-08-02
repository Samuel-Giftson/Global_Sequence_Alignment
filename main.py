from displayTable import DisplayTable as display
from userErrorChecking import UserErrorChecking as error_check
from tableCalculation import TableCalculation as table_calculate


def main():
    print("Welcome to Global Sequence Alignment")
    print("Information I need from you. Two strands, gap penalty, mismatch, and any match scores.")

    error_check_ = error_check()
    value = ""
    while (True):
        try:
            print(" ")
            first_strand = input("Please type in your first strand: ")
            value = error_check_.check_strand(first_strand)
            if not value:
                print("Strand should contain letters A T C G only.")
                print("Please Re-enter strands.")
                print(" ")
                continue

            second_strand = input("Please type in your second strand: ")
            value = error_check_.check_strand(second_strand)
            if not value:
                print("Strand should contain letters A T C G only.")
                print("Please Re-enter strands.")
                print(" ")
                continue

            elif value:
                break
        except Exception as err:
            print("Unexpected Error Occurred, Please Re-type strand")

    print()
    while (True):
        print(" ")
        print("Type in scores.")
        try:
            gap_penalty = int(input("Gap Penalty: "))
            # print(" ")
        except ValueError:
            print("Gap Penalty must be a integer")
            # print(" ")
            continue
        try:
            mismatch = int(input("Mismatch: "))
            # print(" ")
        except ValueError:
            print("Mismatch must be a integer")
            # print(" ")
            continue

        try:
            any_match = int(input("Any match: "))
            # print(" ")
        except ValueError:
            print("Any match must be a integer")
            print(" ")
            continue

        break
    main_table = table_calculate(first_strand, second_strand, gap_penalty, mismatch, any_match)
    main_table_ = main_table.get_main_list()
    saving_work = display(main_table_, first_strand, second_strand)

    print("S in the first cell signifies the start of the table, and asterisk signifies the gap.")
    print(" ")
    final_decision = ""
    while (final_decision != "y"):
        print("You can redo the table, if you enter exact same details again. If you wanted to use different strands, "
              "move the current excel sheet that contains data to a different directory or rename it. When you redo it "
              "using different strands it will save as a excel sheet with same default name.")
        print("")
        print("If you want to do another table or redo the table, type n, if not type y.")
        final_decision = str(input("Type y/n to exit: "))
        final_decision = final_decision.lower()
        if(final_decision == "n"):
            main()
        if(final_decision=="y"):
            exit()

        if(final_decision!="y" and final_decision != "n"):
            print(" ")
            print("Please type y or n.")
            print(" ")
            continue



main()
