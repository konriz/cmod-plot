class SadFile:

    def __init__(self, name, input_dir="input/", output_dir="output/"):
        self.name = name
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.values = []
        self.read()

    def read(self):

        print("Reading file : " + self.name)
        self.values.clear()

        try:
            input_file = open(self.input_dir + self.name + ".asc", "r")

        except IOError:
            print("No file named " + self.name + "\n")
            return

        for line in input_file:
            measure = line.split(",")

            if (len(measure) == 9 ) and (measure[0].strip() != 'cisn'):
                self.values.append(measure[:-1])

        input_file.close()