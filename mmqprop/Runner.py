# Runner.py
from mmqprop import version
from mmqprop.Context import Context


class Runner(object):
    """run qprop test case and display output"""

    def __init__(self, ctx):
        """constructor needs current context"""
        self.ctx = ctx

    def run(self):
        """run command starts test run"""
        print("# QPROP Version", version())
        print("#")
        pfile = ctx.model_data["propfile"]
        pname = ctx.model_data["propname"]
        print(f"# {pname}\t({pfile})")


if __name__ == "__main__":
    ctx = Context()
    ctx.model_data["propfile"] = "kagan"
    ctx.model_data["propname"] = "F1D prop"
    r = Runner(ctx)
    r.run()
