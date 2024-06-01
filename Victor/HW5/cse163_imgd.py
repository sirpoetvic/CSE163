"""
Ryan Siu
Runs imgd with student output against expected output
and produces images showing the pixel differences.
"""
import subprocess
import os

import hw5

PLOTS = [
    "map.png",
    "population_map.png",
    "county_population_map.png",
    "county_food_access.png",
    "low_access.png"
]
IMGD_ARGS = [
    "--pixel-correct-threshold", "0.985",
    "--diff-mode", "always",
    "--correct-colour", "ffffff",
]


def run_imgd(expected, actual, args=IMGD_ARGS):
    """
    Runs imgd of student output against expected.
    Produces diff image only if both student and expected output exist.
    """
    if not os.path.exists(actual):
        print(f"Could not find the file: {actual} after running hw5.py\n"
              "Make sure to call all plotting functions in your main method!")
    elif not os.path.exists(expected):
        print(f"Could not find the file: {expected}\n")
    else:
        print(f"Running image comparison tool on {actual}...")
        output = subprocess.run(["/opt/ed/bin/imgd", expected, actual]
                                + args, capture_output=True)
        output = output.stdout.decode("utf-8")
        print(output)
        os.rename("diff.png", f"{os.path.splitext(actual)[0]}_diff.png")


def main():
    print("Running hw5.main(). This may take a few seconds")
    hw5.main()
    print()
    for plot_name in PLOTS:
        run_imgd(f"expected/{plot_name}", plot_name)


if __name__ == "__main__":
    main()
