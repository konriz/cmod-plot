import Plotter


class CmodData:
    def __init__(self):

        # source file
        self.source = None
        self.valid = False

        # store every step of measurement
        self.total_force = []
        self.total_cmod = []

        # points for CMOD calculations
        self.cmod_limits = [0.5, 1.5, 2.5, 3.5]

        # difference between current CMOD and limit
        self.cmod_diff = [10, 10, 10, 10]

        # CMOD force
        self.cmod_force = [0, 0, 0, 0]
        # CMOD for step
        self.cmod_value = [0, 0, 0, 0]
        # Limit of Proportionality
        self.lop = 0

    def analyse(self, sad_file):
        self.source = sad_file

        if len(self.source.value_types) != 8:
            print("Invalid CMOD file")
            return

        self.valid = True

        last_cmod = -1.0
        for value in self.source.values:

            # calculate mean of CMODs - stop when over 5
            cmod = (float(value[4]) + float(value[5]) + float(value[6]) + float(value[7])) / 4.0

            # deletes measurement flaws
            if cmod < last_cmod:
                continue
            last_cmod = cmod

            # cuts plot at 5 mm
            if cmod > 5.0:
                print(self.source.name + " calculated to 5 mm")
                return

            self.total_cmod.append(cmod)

            # calculate force as sum of reactions
            force = float(value[1]) + float(value[2])
            self.total_force.append(force)

            # calculate lop
            if (cmod < 0.05) and (force > self.lop):
                self.lop = force

            # check if CMOD limit is reached
            for i in range(4):
                diff = abs(cmod - self.cmod_limits[i])
                if diff < self.cmod_diff[i]:
                    self.cmod_diff[i] = diff
                    self.cmod_force[i] = force
                    self.cmod_value[i] = cmod
        return self

    def report(self):
        if not self.valid:
            print("No data to report")

        results = "LOP = {1}\n" \
                  "CMOD1 = {0[0]}\n" \
                  "CMOD2 = {0[1]}\n" \
                  "CMOD3 = {0[2]}\n" \
                  "CMOD4 = {0[3]}\n".format(self.cmod_force, self.lop)

        output_file = open(self.source.output_dir + self.source.name + "_result.asc", "w+")
        output_file.write(results)
        output_file.close()
        print(self.source.name + " saved to file\n")

    def plot(self):
        Plotter.plot([self.total_cmod, self.total_force])
