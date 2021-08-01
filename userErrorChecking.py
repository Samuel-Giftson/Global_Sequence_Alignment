class UserErrorChecking:

    def __init__(self):
        self.DNA_strand = ["A", "T", "C", "G"]
        pass

    def check_strand(self, strand):
        value = True
        for i in range(len(strand)):
            if strand[i] not in self.DNA_strand:
                return False
            else:
                value = True

        return value

