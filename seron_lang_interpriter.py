import re
import sys
from textwrap import dedent

print("seron lang 0.1.1")

option_file = "options.txt"

with open(option_file) as f:
    op_data = f.readline()


def get_in_between(char_in, string, char_out, num):
    return re.findall(re.escape(char_in) + '(.*?)' + re.escape(char_out), string)[num]


with open(get_in_between("(", op_data, ")", 0)) as f:
    data = f.readlines()

mode = "none"
update_line = -1
i = 0

while i < len(data):

    line = dedent(data[i])
    command_ran = False

    # ------------------------------------------------------------------
    #                                                      func commands

    if line.startswith("func"):
        func = line.split(" ")[1].replace('\n', '')

        if func == "_start":
            mode = "_start"

        elif func == "_update":
            update_line = i
            mode = "_update"

        command_ran = True

    elif line.startswith("end"):
        mode = "none"

        command_ran = True

    # ------------------------------------------------------------------
    #                                                           commands

    elif line.startswith("with"):
        if not line.split(" ")[1].replace('\n', '') == "engine":
            exec("import " + line.split(" ")[1].replace('\n', ''), globals())
        else:
            exec("from " + line.split(" ")[1].replace('\n', '') + " import *", globals())

        command_ran = True

    elif line.startswith("if"):
        statement = get_in_between("[", line, "]", 0)

        if not eval(statement):
            i = i + int(get_in_between("[", line, "]", 1))

        command_ran = True

    # ------------------------------------------------------------------
    #                                                    engine commands

    elif "engine" in sys.modules:

        _exec = ""

        if line.startswith("drawBg"):
            _exec = str(get_in_between("[", line, "]", 0) + '.fill()')
            command_ran = True

        elif line.startswith("update"):
            _exec = str(get_in_between("[", line, "]", 0) + '.update()')
            command_ran = True

        elif line.startswith("circle"):
            _exec = str(
                get_in_between("[", line, "]", 0) + ".circle(" +
                get_in_between("[", line, "]", 1) + ","
                + get_in_between("[", line, "]", 2) + ","
                + get_in_between("[", line, "]", 3)) + ")"

            command_ran = True

        exec(_exec, globals())

    if command_ran is False:
        try:
            exec(line, globals())
        except Exception as e:
            sys.exit(e)

    if i == len(data) - 1 and not update_line == -1:
        i = update_line

    i += 1
