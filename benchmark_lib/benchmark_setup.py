import os

from benchmark_lib.benchmark_helper import *

def make_dirs():
    message("creating benchmark directories")
    if(not os.path.exists("./" + benchmark_dir)):
        os.mkdir("./" + benchmark_dir)
    if(not os.path.exists("./" + benchmark_dir + "/" + base_dir)):
        os.mkdir("./" + benchmark_dir + "/" + base_dir)
    message(benchmark_dir + " and " + base_dir + " created")
    return

def cmake(config):
    command = "cd ./" + benchmark_dir + "/" + base_dir + " &&  cmake " + get_root(config)
    print(command)
    os.system(command)
    return

def benchmark_setup(config):
    make_dirs()
    message("call cmake")
    cmake(config)
