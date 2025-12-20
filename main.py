import importlib
import argparse
import time
from typing import Callable
from multiprocessing import freeze_support


def profile(function: Callable, *args):
    start_clock_time = time.perf_counter_ns()
    start_cpu_time = time.process_time_ns()

    ret = function(*args)

    end_clock_time = time.perf_counter_ns()
    end_cpu_time = time.process_time_ns()

    print(f"\nProfiling of {function.__name__}:")
    print(f"    Clock time: {(end_clock_time - start_clock_time) / 1e9} s")
    print(f"      CPU time: {(end_cpu_time - start_cpu_time) / 1e9} s\n")

    return ret


def execute_day(day: int):
    try:
        mod = importlib.import_module(f"day_{day}.solver")
    except ModuleNotFoundError:
        exit()

    print("-----------------------------------------------------")
    print(f"Day {day}:")
    print(f"Part one result: {profile(mod.part_one, f"day_{day}/input.txt")}")
    print(f"Part two result: {profile(mod.part_two, f"day_{day}/input.txt")}")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    freeze_support()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--day", type=int, help="Executes only this day if given"
    )
    args = parser.parse_args()

    if args.day:
        execute_day(args.day)
    else:
        for day in range(1, 13):
            execute_day(day)
