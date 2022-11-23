# cmd_set_propfile.py
import os

class Plugin:
    '''iset user propfile name command plugin'''
    help = "set user input propfile name"
    name = "set_propfile"

    def process(self, ctx):
        '''get user propfile name, update context'''
        propfile = input("Propname: ")
        fname = os.path.join(ctx.data_dir, propfile)
        print("opening:", fname)
        if not os.path.isfile(fname):
            print("file not found")
            return
        else:
            print("loading...")
        ctx.argcount += 1
