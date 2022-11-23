# mmqprop/file_io.py


def load_data(fname):
    '''load a data file, strip whitespace, return data'''

    # set up for error return
    rdata = None
    name = None

    with open(fname, 'r') as fin:
        lines = fin.readlines()
        dlines = []
        for line in lines:
            line = line.rstrip()  # get rid of trailing whitespace and newlines

            # skip comment and blank lines
            if len(line) == 0 or line[0] == '#':
                continue

            # look for end line comments
            n = line.find('!')
            if n > 0:
                line = line[0:n - 1].strip()

            dlines.append(line)

        # get name line - required
        name = dlines[0].strip()

        # break out remaining data
        rdata = []
        for line in dlines[1:]:
            rline = l.split()
            rdata.append(rline)

    return name, rdata
