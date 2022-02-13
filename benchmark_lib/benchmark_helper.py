benchmark_dir = "benchmark_dir"
base_dir = "cmake_folder"

def message(m):
    print("---------- " + m + " ----------")

def get_root(config):
    return config["root"]

def get_executable(config):
    return config["executable"]

def get_abbreviation(name):
    abbreviation = name.replace("#", "")
    abbreviation_list = abbreviation.split("_")
    abbreviation = ""
    for a in abbreviation_list:
        abbreviation += a[0]
    return abbreviation


def get_dir_name(parameter_set):
    dir_name = ""
    for key, value in parameter_set.items():
        dir_name += get_abbreviation(key) + "_" + str(value) + "-"
    return dir_name

def get_run_dir(plot_name, graph_dir, run_config):
    path = "./" + benchmark_dir + "/" + plot_name + "/" + graph_dir + "/"
    for parameter, value in run_config.items():
        path += parameter + str(value)
    return path