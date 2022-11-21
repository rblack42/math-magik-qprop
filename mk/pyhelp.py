import sys
import re


help_re = re.compile(r"^([a-zA-Zi_-]*:).*?##(.*)$")

def main():

    modules = sys.argv
    del modules[0]
    for m in modules:
        lines = []
        with open(m) as fin:
            lines = fin.readlines()
        for l in lines:
            m = help_re.match(l)
            if m:
                item = m.group(1).strip()
                defn = m.group(2).strip()
                print("%-20s %s" %(item,defn))


if __name__ == '__main__':
    main()
