import os

from benchmark_lib.benchmark_helper import *




def for_each_config(config):
    for plot_name, plot_config in config["plots"].items():
        for graph_config in plot_config:
            for run_config in graph_config["run_time_parameters"]:
                time_output_file = get_run_dir(plot_name, graph_config["graph_name"], run_config) + "/time.txt"
                file = open(time_output_file, "w")
                file.close()
    return



def benchmark_clear(config):
    for_each_config(config)
    return
