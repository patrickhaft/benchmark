import matplotlib.pyplot as plt
import pickle
import os

from benchmark_lib.benchmark_helper import *
import benchmark_lib.plot_config as pc


def get_x(config):
    # x_values = []
    # for parameter_set in config["parameter_values"]:
    #     if parameter_set[x_plot_variable] in x_values:
    #         continue
    #     x_values.append(parameter_set[x_plot_variable])
    return  config["x_axis_values"]



def get_average(dict):
    average_list = []
    for key, value in dict.items():
        average = sum(value) / len(value)
        average_through_put = 10000000 / (average)
        average_list.append(average_through_put)
    return average_list

def get_max(dict):
    max_list = []
    for key, value in dict.items():
        max_list.append(max(value))
    return max_list

def get_min(dict):
    min_list = []
    for key, value in dict.items():
        min_list.append(min(value))
    return min_list

def plot_dict_for_num_steps(config, plot_name, execution_time_dictionary, ax, ps, label):

    average_times = get_average(execution_time_dictionary)
    # min_times = get_min(execution_time_dictionary)
    # print(label + " min array: " + str(min_times))
    # max_times = get_max(execution_time_dictionary)
    # print(label + " max_times: " + str(max_times))

    x = get_x(config)
    plt.xticks(x)
    y = average_times
    next_sytle = ps.getNextStyle()
    # ax.fill_between(x, max_times, min_times, facecolor=next_sytle["color"], alpha=0.3, linestyle="solid")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.ticklabel_format(axis="y", style="plain", scilimits=(0, 0))
    manager = plt.get_current_fig_manager()
    manager.set_window_title(plot_name)
    plt.plot(x, y, **next_sytle, label=label)


def get_abbreviation_without_x(parameter_set, x_plot_variable):
    dir_name = ""
    for key, value in parameter_set.items():
        if key == x_plot_variable:
            continue
        dir_name += get_abbreviation(key) + "_" + str(value) + "-"
    return dir_name



def sort_dict(config, x_plot_variable, time_dict):
    sorted_time_dict = {}
    for parameter_set in config["parameter_values"]:
        key = get_abbreviation_without_x(parameter_set, x_plot_variable)
        if key not in sorted_time_dict.keys():
            sorted_time_dict[key] = {}
        sorted_time_dict[key][parameter_set[x_plot_variable]] = time_dict[get_dir_name(parameter_set)]

    return sorted_time_dict

def plot(config, plot_name, current_plot_dict, x_plot_variable):

    fig, ax = pc.setup()
    ps = pc.PlotStyles()


    # sorted_dict = sort_dict(config, x_plot_variable, dictionary)
    # print(sorted_dict)
    for graph_name, graph_config in current_plot_dict.items():
        plot_dict_for_num_steps(config, plot_name, graph_config, ax, ps, graph_name)

    # for key, time_dict in current_plot_dict.items():
    #     plot_dict_for_num_steps(config, x_plot_variable, time_dict, ax, ps, key)

    plt.xlabel(x_plot_variable)
    plt.ylabel("Tuples micro seconds")
    plt.legend()
    plt.tight_layout()
    # plt.savefig('plot_num_steps_' + str(num_steps), bbox_inches='tight')
    plt.show()


def for_each_config(config, x_plot_variable):
    dictionary = {}
    data_file = open("./pickle_dir/time.pickle", 'rb')
    tmp_dict = pickle.load(data_file)
    dictionary.update(tmp_dict)
    for plot_name, plot_config in config["plots"].items():
        current_plot_dict = dictionary[plot_name]
        plot(config, plot_name, current_plot_dict, x_plot_variable)
    return




def benchmark_plot(config, x_plot_variable):
    for_each_config(config, x_plot_variable)
    # dictionary = {}
    # data_file = open("./pickle_dir/time.pickle", 'rb')
    # tmp_dict = pickle.load(data_file)
    # dictionary.update(tmp_dict)
    # print(sort_dict(config, x_plot_variable, dictionary))
    return