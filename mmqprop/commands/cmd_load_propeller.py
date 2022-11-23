# cmd_load_propeller.py
import os

from mmqprop.Propeller import Propeller


class Plugin:
    '''debug command plugin'''
    help = "load speficied propeller file"
    name = "load_propeller"

    def process(self, ctx):
        '''process ctx.propfile'''
        debug = ctx.debug
        data_dir = ctx.data_dir
        propfile = ctx.propfile
        if propfile is None:
            propfile = "default_prop"
        fname = os.path.join(data_dir, propfile)
        p = Propeller(ctx, fname)
        p.parse()
        p.dump()
        ctx.argcount += 1
