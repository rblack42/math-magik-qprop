# cmd_load_motor.py
import os

from mmqprop.Motor import Motor


class Plugin:
    '''load motor data file command plugin'''
    help = "load speficied motor file"
    name = "load_motor"

    def process(self, ctx):
        '''process ctx.propfile'''
        debug = ctx.debug
        data_dir = ctx.data_dir
        motorfile = ctx.motorfile
        if motorfile is None:
            motorfile = "default_motor"
        fname = os.path.join(data_dir, motorfile)
        m = Motor(ctx, fname)
        m.parse()
        m.dump()
        ctx.argcount += 1
