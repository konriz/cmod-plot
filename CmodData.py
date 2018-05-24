class CmodData:
    def __init__(self, values):
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

        self.analyse(values)

    def analyse(self, values):
        for value in values:

            # calculate mean of CMODs - stop when over 5
            cmod = (float(value[4]) + float(value[5]) + float(value[6]) + float(value[7])) / 4.0

            if cmod > 5.0:
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
