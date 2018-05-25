class SadFile:

    def __init__(self, name, input_dir="input/", output_dir="output/"):
        self.name = name
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.value_types = []
        self.values = []
        self.read()

    def read(self):

        print("Reading file : " + self.name)
        self.value_types.clear()
        self.values.clear()

        try:
            input_file = open(self.input_dir + self.name + ".asc", "r")

        except IOError:
            print("No file named " + self.name)
            return

        for line in input_file:
            measure = line.split(",")[:-1]
            if len(measure) > 0:
                self.values.append(measure)

        self.value_types = self.values.pop(0)

        input_file.close()

