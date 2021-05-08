# global n_range
n_range = range(3, 12)

def compile_field():
    # compile all vickrey mod
    for i in n_range:
        fin = open("Programs/Source/vickrey_mod.mpc", "rt")
        fout = open("Programs/Source/vickrey_mod{}.mpc".format(i), "wt")
        for line in fin:
            fout.write(line.replace("n_inputs = 11", "n_inputs = {}".format(i)))
        fin.close()
        fout.close()

    # compile all baseline
    for i in n_range:
        fin = open("Programs/Source/vickrey_baseline.mpc", "rt")
        fout = open("Programs/Source/vickrey_baseline{}.mpc".format(i), "wt")
        for line in fin:
            fout.write(line.replace("n_inputs = 11", "n_inputs = {}".format(i)))
        fin.close()
        fout.close()

    from subprocess import Popen, PIPE
    import sys

    cmds_list = [["./compile.py", "-C", "vickrey_mod{}".format(i)] for i in n_range]
    cmds_list += [["./compile.py", "-C", "vickrey_baseline{}".format(i)] for i in n_range]
    proc_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
    for proc in proc_list:
        proc.wait()

def compile_ring():
    # compile all vickrey mod
    for i in n_range:
        fin = open("Programs/Source/vickrey_mod.mpc", "rt")
        fout = open("Programs/Source/vickrey_mod{}.mpc".format(i), "wt")
        for line in fin:
            fout.write(line.replace("n_inputs = 11", "n_inputs = {}".format(i)))
        fin.close()
        fout.close()

    # compile all baseline
    for i in n_range:
        fin = open("Programs/Source/vickrey_baseline.mpc", "rt")
        fout = open("Programs/Source/vickrey_baseline{}.mpc".format(i), "wt")
        for line in fin:
            fout.write(line.replace("n_inputs = 11", "n_inputs = {}".format(i)))
        fin.close()
        fout.close()

    from subprocess import Popen, PIPE
    import sys

    cmds_list = [["./compile.py", "-R 64", "-C", "vickrey_mod{}".format(i)] for i in n_range]
    cmds_list += [["./compile.py", "-R 64", "-C", "vickrey_baseline{}".format(i)] for i in n_range]
    proc_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
    for proc in proc_list:
        proc.wait()


if __name__ == "__main__":
    compile_field()