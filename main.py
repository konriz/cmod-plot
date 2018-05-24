import Calculator
import glob


def gather_all(input_dir='input/'):

    files = glob.glob(input_dir + '*.ASC')
    sad_files = []

    for sad_file in files:
        sad_files.append(sad_file[len(input_dir):-4])

    print("Gathered %d files" % len(sad_files))

    return sad_files


for file_name in gather_all():
    Calculator.plot_cmod(file_name)
