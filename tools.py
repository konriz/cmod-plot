import glob


def gather_all(input_dir='input/'):

    files = glob.glob(input_dir + '*.ASC')
    names = []

    for name in files:
        names.append(name[len(input_dir):-4])

    print("Gathered %d files" % len(names))

    return names


def average(datas):
    return
