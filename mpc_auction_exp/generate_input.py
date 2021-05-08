# import compile_exp.n_range as n_range
n_range = range(12)

# average collusion size = 1
def gen_input_1():
    price = [(42 + 100 * i, i) for i in n_range]
    for i in n_range:
        with open("Player-Data/Input-P{}-0".format(i), "wt") as fout:
            fout.write("{} {}\n".format(price[i][0], price[i][1]))


# average collusion size = 2
def gen_input_2():
    price = [42 + 100 * i for i in n_range]
    # TODO: maybe another way of doing so
    for i in n_range:
        with open("Player-Data/Input-P{}-0".format(i), "wt") as fout:
            if i % 2 == 0:
                fout.write("{} {}\n".format(price[i], i))
            else:
                fout.write("{} {}\n".format(price[i], i - 1))


# average collusion size = n
def gen_input_n():
    price = [42 + 100 * i for i in n_range]
    from random import shuffle

    shuffle(price)
    for i in n_range:
        with open("Player-Data/Input-P{}-0".format(i), "wt") as fout:
            fout.write("{} {}\n".format(price[i], 0))