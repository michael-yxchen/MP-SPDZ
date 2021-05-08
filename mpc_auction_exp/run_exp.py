from generate_input import *
from compile_exp import *
# from subprocess import Popen, PIPE
import subprocess
import os
from collect_data import * 


def run_all(mpc_algo, baseline=False):
    for i in n_range:
        os.environ["PLAYERS"] = str(i)
        cmd = ["./Scripts/{}.sh".format(mpc_algo), "vickrey_mod{}".format(i)]
        subprocess.call(cmd, stdout=open("Results/" + cmd[1] + ".result", "w"))
        if baseline:
            cmd = ["./Scripts/{}.sh".format(mpc_algo), "vickrey_baseline{}".format(i)]
            subprocess.call(cmd, stdout=open("Results/" + cmd[1] + ".result", "w"))

if __name__ == "__main__":
    mpc_algo = ["semi2k", "semi", "shamir", "mascot"]
    for algo in mpc_algo:
        if algo ==mpc_algo[0]:
            compile_ring()
        elif algo == mpc_algo[1]:
            compile_field()

        writer_file = [init_csv(algo, metric) for metric in metrics]
        gen_input_1()
        run_all(algo, baseline=True)
        for m in range(len(metrics)):
            collect_data(writer_file[m][0], "vickrey_baseline", "baseline", metrics[m])
            collect_data(writer_file[m][0], "vickrey_mod", "avg_col_1", metrics[m])
        gen_input_2()
        run_all(algo)
        for m in range(len(metrics)):
            collect_data(writer_file[m][0], "vickrey_mod", "avg_col_2", metrics[m])
        gen_input_n()
        run_all(algo)
        for m in range(len(metrics)):
            collect_data(writer_file[m][0], "vickrey_mod", "avg_col_n", metrics[m])
        for w, f in writer_file:
            f.close()
        # break
