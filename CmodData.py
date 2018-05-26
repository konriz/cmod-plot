class CmodData:
    def __init__(self):

        # source file
        self.source = None
        self.valid = False

        # store every step of measurement where [0] is cmod and [1] is force
        self.curve = [[], []]

    def analyse(self, sad_file):
        self.source = sad_file

        if len(self.source.value_types) != 8:
            print("Invalid CMOD file")
            return

        self.valid = True

        last_cmod = -1.0
        for value in self.source.values:

            # calculate mean of CMODs
            cmod = (float(value[4]) + float(value[5]) + float(value[6]) + float(value[7])) / 4.0

            # deletes measurement flaws
            if cmod < last_cmod:
                continue
            last_cmod = cmod

            # cuts plot at 5 mm
            if cmod > 5.0:
                print(self.source.name + " calculated to 5 mm")
                return self

            self.curve[0].append(cmod)

            # calculate force as sum of reactions
            force = float(value[1]) + float(value[2])
            self.curve[1].append(force)

        return self

    def calculate_cmod(self):
        limits = [0.5, 1.5, 2.5, 3.5]
        results = []
        for limit in limits:
            result = self.find_force(limit)
            results.append(result)
        return results

    def calculate_lop(self):
        for i in range(len(self.curve[0])):
            if self.curve[0][i] > 0.05:
                return max(self.curve[1][0:i])

    def extract_curve(self):

        x_data = self.curve[0]
        y_data = self.curve[1]
        name = self.source.name
        return [x_data, y_data, name]

    def report(self):
        if not self.valid:
            print("No data to report")

        results = "LOP = {lop}\n" \
                  "CMOD1 = {cmod[0]}\n" \
                  "CMOD2 = {cmod[1]}\n" \
                  "CMOD3 = {cmod[2]}\n" \
                  "CMOD4 = {cmod[3]}\n".format(lop=self.calculate_lop(), cmod=self.calculate_cmod())

        output_file = open(self.source.output_dir + self.source.name + "_result.asc", "w+")
        output_file.write(results)
        output_file.close()
        print(self.source.name + " saved to file\n")

    def find_force(self, cmod):

        for i in range(len(self.curve[0])):
            dif = abs(cmod - self.curve[0][i])

            if 0.01 > dif:
                return [self.curve[0][i], self.curve[1][i]]

        print("Value at {cmod} not found".format(cmod=cmod))
