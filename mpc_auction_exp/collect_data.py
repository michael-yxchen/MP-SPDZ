import csv
from compile_exp import n_range
import re

metrics = ["Time", "Data sent", "Global data sent"]

def init_csv(mpc_algo, metric : str):
    f = open("Results/{}_{}.csv".format(mpc_algo, metric.lower().replace(" ", "_")), 'w', newline='\n')
    # field_names = ["party", "baseline", "avg_col_1", "avg_col_1/2n", "avg_col_n"]
    field_names = ["collusion_type"]
    field_names += ["party_" + str(i) for i in n_range]
    writer = csv.writer(f)
    writer.writerow(field_names)
    return writer, f


def collect_data(writer : csv.writer, filename_prefix, row_name, metric):
    rgx = re.compile(metric + " = (\\d*[\.]?\\d*).*")
    row = [row_name]
    for i in n_range:
        fn =  "Results/" + filename_prefix + str(i) + ".result"
        with open(fn, 'r') as f:
            for l in f:
                m = rgx.search(l)
                if m:
                    row.append(m.group(1))
    writer.writerow(row)


if __name__ == "__main__":
    writer, f = init_csv("shamirtset", metrics[1])
    collect_data(writer, "vickrey_baseline", "baseline", metrics[1])
    f.close()

