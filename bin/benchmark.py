#! /usr/bin/env python
import argparse
import importlib
import sys
import os

from benchmark_lib.benchmark_create import benchmark_create
from benchmark_lib.benchmark_execute import benchmark_execute
from benchmark_lib.benchmark_setup import benchmark_setup
from benchmark_lib.benchmark_collect import benchmark_collect
from benchmark_lib.benchmark_plot import benchmark_plot
from benchmark_lib.benchmark_clear import benchmark_clear

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--step",
                    help="benchmark step",
                    required=False)

parser.add_argument("-c", "--config_file",
                    help="path to the benchmark config file",
                    required=True)

sys.path.append(str(os.getcwd()))

args = parser.parse_args()

config = importlib.import_module(args.config_file).config

if args.step == "setup":
    benchmark_setup(config)
elif args.step == "create":
    benchmark_create(config)
elif args.step == "execute":
    benchmark_execute(config)
elif args.step == "collect":
    benchmark_collect(config)
elif args.step == "plot":
    benchmark_plot(config, "Number of Threads")
elif args.step == "clear":
    benchmark_clear(config)