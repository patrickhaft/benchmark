
import os
import pickle


from benchmark_lib.benchmark_helper import *

def execute_for_plot(config, plot_name, plot_config):
    for graph_config in plot_config:
        # graph_dir = "./" + benchmark_dir + "/" + plot_name + "/" + graph_config["graph_name"]
        for run_config in graph_config["run_time_parameters"]:
            executable_path = get_run_dir(plot_name, graph_config["graph_name"], run_config)
            executable_path = executable_path.replace(" ", "\\ ")
            execute_parameters = ""
            for parameter, value in graph_config["default_parameter"].items():
                execute_parameters += " " + str(value)
            for parameter, value in run_config.items():
                execute_parameters += " " + str(value)
            execute_command = "cd " + executable_path + " && ./" + get_executable(config) + execute_parameters
            print(execute_command)
            for i in range(config["number_runs"]):
                os.system(execute_command)




    return

def execute_for_each(config):
    # for parameter_set in config["parameter_values"]:
    #     dir_name = get_dir_name(parameter_set)
    #     message("call executable")
    #     command = "cd " + "./" + benchmark_dir + "/" + dir_name
    #     command += " && ./" + get_executable(config) + " " + config["execute_parameter"]
    #     print(command)
    #     for i in range(config["number_runs"]):
    #         os.system(command)
    for plot_name, plot_config in config["plots"].items():
        execute_for_plot(config, plot_name, plot_config)
    return



def benchmark_execute(config):
    execute_for_each(config)
    return