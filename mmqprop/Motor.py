import os

from .file_io import load_data


class Motor(object):
    def __init__(self, ctx, fname="default_motor"):
        self.name, self.rdata = load_data(fname)
        self.dlines = len(self.rdata)

    def read_error(self, msg):
        print("Read error:", msg)

    def parse(self):
        nlines = self.dlines
        dlines = self.rdata
        if nlines < 4:
            self.read_error("Type 1 insuffucuent data lines")
        try:
            self.mtype = int(dlines[0][0])  # motor type
            self.r0 = float(dlines[1][0])  # motor resistance
            self.io0 = float(dlines[2][0])  # no-load current
            self.kv = dlines[3][0]  # rpm/volt

            # set remaning properties to -1 no data
            self.kq = -1
            self.tau = -1
            self.io1 = -1
            self.io2 = -1
            self.r2 = -1

        except IndexError:
            print("data file not valid")
            return

        if self.mtype == 1:
            return

        # process type 2 motor file
        if nlines < 9:
            self.read_error("Type 2 insufficient data lines")
            return
        try:
            self.kq = dlines[4][0]  # amp/N-m
            self.tau = dlines[5][0]  # magnetic lag time
            self.io1 = dlines[6][0]  # no-load current linear term
            self.io2 = dlines[7][0]  # no-load quadratic term
            self.r2 = dlines[8][0]  # motor resistance quadratic coeff
        except IndexError:
            self.read_error("type 2 data file invalid")
            return

    def dump(self):
        print("Motor:", self.name)
        print("Motor Type:", self.mtype)
        print("R0:", self.r0)
        print("Io0:", self.io0)
        print("Kv:", self.kv)
        print("Kq:", self.kq)
        print("tau:", self.tau)
        print("Io1:", self.io1)
        print("Io2:", self.io2)
        print("R2:", self.r2)


if __name__ == "__main__":
    data_dir = "../data"
    mname = "s300-7v-dd"
    mfile = os.path.join(data_dir, mname)
    m = Motor(mfile)
    m.parse()
    m.dump()
