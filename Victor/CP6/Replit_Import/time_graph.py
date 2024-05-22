# stop replit from complaining about MPLCONFIGDIR
import os
import tempfile

os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()

import time
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


class TimeGraph:
    def __init__(self):
        sns.set()

    def _time_fn(self, fn, n):
        t0 = time.time()
        fn(n)
        t1 = time.time()
        return t1 - t0

    def _do_timing(self, fn, iterations=16):
        ns = []
        times = []
        n = 100
        for attempts in range(iterations):
            ns.append(n)
            time_elapsed = self._time_fn(fn, n)
            times.append(time_elapsed)
            print(f"For n = {n}, time is: {time_elapsed:.5f}")
            n *= 2
        return (ns, times)

    def _plot_time(self, ns, times, method):
        # Plot the times (uses some advanced plotting features)
        fig, ax = plt.subplots(1)
        ax.plot(ns, times, "g^", label="primes")
        # ax.plot(ns, times, label='sum2')
        ax.set_ylabel("Time (seconds)")
        ax.set_xlabel("n")
        ax.set_title("Growth of time for Method:" + method)
        ax.legend()
        fig.savefig(method + ".png")

    def time_and_graph(self, fn, method, max_iters=16):
        print("\n*** Measuring and plotting", method, "***\n")
        ns, times = self._do_timing(fn, max_iters)
        # self._print_stats(ns, times)
        self._plot_line(ns, times, method)

    """
    def _print_stats(self, ns, times):
        p, e, *_ = np.polyfit(ns, times, 1, full=True)
        print(f'Line: y={p[0]}x + {p[1]}')
        print(f'Linear Sq Error {e[0]}')
        p, e, *_ = np.polyfit(ns, times, 2, full=True)
        if (p[0] < 0):
            print('Inverted Quadratic. Can\'t be right!')
        print(f'Quadratic: y={p[0]}x^2 + {p[1]}x + {p[2]}')
        print(f'Quadratic Sq Error {e[0]}')
    """

    def _plot_line(self, ns, times, method):
        """
        Plot two regession plots: linear and quadratic
        """
        data = [[n, t] for n, t in zip(ns, times)]
        df = pd.DataFrame(data, columns=["n", "time"])
        # Plot the times (uses some advanced plotting features)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        sns.regplot(x="n", y="time", ci=None, ax=ax1, data=df)
        sns.regplot(
            x="n", y="time", ci=None, ax=ax2, order=2, color="g", data=df
        )
        ax1.set_title("Linear")
        ax2.set_title("Quadratic")
        ax1.set_ylabel("Time (seconds)")
        ax2.set_ylabel("")
        fig.suptitle("Growth of time: " + method)
        plt.savefig(method + ".png", bbox_inches="tight")
