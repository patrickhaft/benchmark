import pickle

from benchmark_lib.benchmark_helper import *


def collect_execution_time(config,plot_name, plot_config):
    plot_time_dict = {}
    for graph_config in plot_config:
        graph_time_dict = {}
        graph_dir = "./" + benchmark_dir + "/" + plot_name + "/" + graph_config["graph_name"]
        for run_config in graph_config["run_time_parameters"]:
            execute_dir_path = get_run_dir(plot_name, graph_config["graph_name"], run_config)
            path_time_output_file = execute_dir_path + "/time.txt"
            time_list = []
            with open(path_time_output_file, 'r') as f:
                lines = f.readlines()
                if len(lines) == 0:
                    print("not execution time in: " + path_time_output_file)
                    last_line = 0
                else:
                    for line in lines:
                        time_list.append(float(line))
            graph_time_dict[execute_dir_path] = time_list
        plot_time_dict[graph_config["graph_name"]] = graph_time_dict

    return plot_time_dict



def safe_times(execution_time_dictionary):
    output_file_path = "./pickle_dir/time.pickle"
    open(output_file_path, 'a').close()
    output_file = open(output_file_path, 'wb')
    pickle.dump(execution_time_dictionary, output_file)
    output_file.close()

def for_each_config(config):
    diagram_time_dict = {}
    for plot_name, plot_config in config["plots"].items():
        print("create execution folders for: " + plot_name)
        diagram_time_dict[plot_name] = collect_execution_time(config, plot_name, plot_config)
    return diagram_time_dict

def benchmark_collect(config):
    execution_time_dictionary = for_each_config(config)
    print(execution_time_dictionary)
    safe_times(execution_time_dictionary)