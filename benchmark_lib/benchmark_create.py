from shutil import copytree, rmtree, copy
import os

from benchmark_lib.benchmark_helper import *

# def copy_folder(config):
#     folders = get_folder_array(config)
#     src_root = config["root"]
#     for folder in folders:
#         dst_path = "./" + benchmark_dir + "/" + base_dir + "/" + folder
#         src_path = src_root + "/" + folder
#         if os.path.exists(dst_path):
#             rmtree(dst_path)
#             copytree(src_path, dst_path)
#
#     return

# def copy_files(config):
#     files = get_files_array(config)
#     src_root = config["root"]
#     for file in files:
#         dst_path = "./" + benchmark_dir + "/" + base_dir
#         src_path = src_root + "/" + file
#         if os.path.exists(dst_path):
#
#             copy(src_path, dst_path)
#     return
#
# def get_files_array(config):
#     return config["files"]
#
# def get_folder_array(config):
#     return config["folders"]

#
# def compile(config):
#     root = get_root(config)
#     cmake_command = get_cmake(config)
#     combined_command = "cd " + root + " && " + cmake_command
#     message("execute cmake")
#     print(combined_command)
#     os.system(combined_command)
#     message("finished cmake")
#     return

# def copy_executable(config):
#     src_root = config["root"]
#     cmake_dir = get_cmake_dir(config)
#     executable = get_executable(config)
#     dst_path = "./" + benchmark_dir + "/" + base_dir + "/" + executable
#     src_path = src_root + "/" + cmake_dir + "/" + executable
#     copy(src_path, dst_path)
#     return



def replace_parameters(config, parameter_config):
    template_files = config["template_files"]
    file_list = []
    for template_file in template_files:
        parameter_names = config["parameters"][template_file]
        current_file = open(get_root(config) + template_file, "rt")
        file_content = current_file.read()
        file_list.append(file_content)
        for parameter in parameter_names:
            print("replace " + parameter + " with " + str(parameter_config[parameter]))
            file_content = file_content.replace(parameter, str(parameter_config[parameter]))
        current_file.close()
        current_file = open(get_root(config) + template_file, "wt")
        current_file.write(file_content)
        current_file.close()
    return file_list

def reset_to_default(config, files_list):
    template_files = config["template_files"]
    for idx, template_file in enumerate(template_files):
        current_file = open(get_root(config) + template_file, "wt")
        current_file.write(files_list[idx])
        current_file.close()
    return



def make(config):
    command = "cd ./" + benchmark_dir + "/" + base_dir + " &&  make " + get_executable(config)
    print(command)
    os.system(command)
    return


def copy_executable_to_execute_dir(config, plot_name, graph_dir, run_dir):
    src = "./" + benchmark_dir + "/" + plot_name + "/" + graph_dir + "/" + get_executable(config)
    dest = "./" + benchmark_dir + "/" + plot_name + "/" + graph_dir + "/" + run_dir + "/" + get_executable(config)

    return

def copy_executable(config, graph_dir,  parameter_set):
    dir_name = get_dir_name(parameter_set)
    # path_new_dir = "./" + benchmark_dir + "/" + dir_name
    path_executable = "./" + benchmark_dir + "/" + base_dir + "/" + get_executable(config)
    # if not os.path.exists(path_new_dir):
    #     os.mkdir(path_new_dir)
    copy(path_executable, graph_dir + "/" + get_executable(config))
    # if not os.path.exists(path_new_dir + "/time.txt"):
    #     with open(path_new_dir + "/time.txt", 'w'):
    #         pass
    return




def create_plot_benchmark(config, plot_name, plot_config):
    plot_dir = "./" + benchmark_dir + "/" + plot_name
    if not os.path.exists(plot_dir):
        os.mkdir(plot_dir)
    for graph_config in plot_config:
        graph_dir = "./" + benchmark_dir + "/" + plot_name + "/" + graph_config["graph_name"]
        if not os.path.exists(graph_dir):
            os.mkdir(graph_dir)
        message("replace parameter with values")
        file_list = replace_parameters(config, graph_config["compile_time_parameters"])
        message("call cmake")
        message("call make target")
        make(config)
        message("copy created executable to new directory")
        copy_executable(config, graph_dir,  graph_config["compile_time_parameters"])
        message("replace values with parameters")
        reset_to_default(config, file_list)
        print(graph_config["run_time_parameters"])
        for run_config in graph_config["run_time_parameters"]:
            execute_dir_path = get_run_dir(plot_name, graph_config["graph_name"], run_config)
            if not os.path.exists(execute_dir_path):
                os.mkdir(execute_dir_path)
            dest_execute = execute_dir_path + "/" + get_executable(config)
            copy(graph_dir + "/" + get_executable(config), dest_execute)
            if not os.path.exists(execute_dir_path + "/time.txt"):
                with open(execute_dir_path + "/time.txt", 'w'):
                    pass
    return



def for_each_config(config):
    for plot_name, plot_config in config["plots"].items():
        print("create execution folders for: " + plot_name)
        create_plot_benchmark(config, plot_name, plot_config)
    return

def benchmark_create(config):
    for_each_config(config)
    return