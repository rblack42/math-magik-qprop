import os
import sys

from . file_io import load_data


class Propeller(object):
    '''Load standard QPROP propeller file from data dir'''

    def __init__(self, ctx, fname='data/default_prop'):
        '''set propfile name and initial data values'''
        self.name, self.rdata = load_data(fname)
        self.debug = ctx.debug
        self.runfile = None
        self.radius = 0
        self.irdim = 81

    def read_error(self, msg):
        print("Read failed:", msg)
        sys.exit(1)

    def parse(self):

        nlines = len(self.rdata)
        if nlines == 0:
            self.read_error("not enough parameters")
        try:
            # get number of blades and optional radius
            dline = self.rdata[0]
            self.nblades = dline[0]
            if len(dline) > 1:
                self.radius = dline[1]
            pline = 0

            # load base properties -----------
            # read CL0 and CL_a
            dline = self.rdata[1]
            cl0b = dline[0]
            clab = dline[1]
            pline = 1

            # read CLMIN and CLMAX
            dline = self.rdata[2]
            clminb = dline[0]
            clmaxb = dline[1]
            pline = 2

            # read CL/CD quadratic params
            dline = self.rdata[3]
            cd0b = dline[0]
            cd2ub = dline[1]
            cd2lb = dline[2]
            clcd0b = dline[3]
            pline = 3

            # read REREF and REEXP
            dline = self.rdata[4]
            rerefb = dline[0]
            reexpb = dline[1]
            pline = 4

            # Read scaling factors (1)
            dline = self.rdata[5]
            self.rfac = dline[0]
            self.cfac = dline[1]
            self.bfac = dline[2]
            pline = 5

            # Read scaling factors (2)
            dline = self.rdata[6]
            self.radd = dline[0]
            self.cadd = dline[1]
            self.badd = dline[2]
            pline = 6

            if self.debug:
                print("base props complete")

            # read prop coordinate data
            r = []
            c = []
            beta = []
            exdata = []
            for line in self.rdata[7:]:
                pline += 1
                if self.debug:
                    print("processing line:", pline)
                r.append(line[0])
                c.append(line[1])
                beta.append(line[2])

                # check for optional element data
                props = []

                # initial values for props
                if self.debug:
                    print("initial values")
                cl0 = cl0b
                cla = clab
                clmin = clminb
                clmax = clmaxb
                cd0 = cd0b
                cd2u = cd2ub
                cd2l = cd2lb
                clcd0 = clcd0b
                reref = rerefb
                reexp = reexpb
                if self.debug:
                    print("initial base complete")
                # check for extended aero data
                if len(line) > 3:
                    if self.debug:
                        print("loading extended data", line)
                    try:
                        cl0 = line[3]
                        cla = line[4]
                        clmin = line[5]
                        clmax = line[6]
                        cd0 = line[7]
                        cd2u = line[8]
                        cd2l = line[9]
                        clcd0 = line[10]
                        reref = rerefb
                        reexp = reexpb
                        if len(line) > 11:
                            reref = line[11]
                        if len(line) == 13:
                            reexp = line[12]
                    except IndexError:
                        self.read_error("bad extended aero data")
                # save props for this bld=ade section
                if self.debug:
                    print("...done")
                props = [
                    cl0,
                    cla,
                    clmin,
                    clmax,
                    cd0,
                    cd2u,
                    cd2l,
                    clcd0,
                    reref,
                    reexp
                ]
                if self.debug:
                    print(props)
                exdata.append(props)

            self.r = r
            self.c = c
            self.beta = beta
            self.props = exdata

        except:
            msg = f"general read error on line {pline}"
            self.read_error(msg)

    def dump(self):
        print("Propeller:", self.name)
        print("Runfile:", self.runfile)
        print("Blades:", self.nblades)
        print("Initial radius:", self.radius)
        print("RFAC:", self.rfac)
        print("CFAC:", self.cfac)
        print("BFAC:", self.bfac)
        print("RADD:", self.radd)
        print("CADD:", self.cadd)
        print("BADD:", self.badd)
        print("R:", self.r)
        print("C:", self.c)
        print("BETA:", self.beta)
        print("PROPS:")
        for p in self.props:
            print('\t', p)

    def prepare(self):
        '''use splines to henerate fine grid of data'''
 

if __name__ == '__main__':
    data_dir = '../data'
    pname = 'gcam6x3f'
    pfile = os.path.join(data_dir, pname)
    p = Propeller(pfile)
    p.parse()
    p.dump()
