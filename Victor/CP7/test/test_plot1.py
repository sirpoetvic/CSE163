import os
import unittest
from unittest.mock import patch

import matplotlib.pyplot as plt
import numpy as np

DATA_FILE = "geo_data/ne_110m_admin_0_countries.shp"


class Test1(unittest.TestCase):
    def setUp(self):
        if os.path.exists("south_america.png"):
            os.remove("south_america.png")

    @patch("matplotlib.pyplot.savefig")
    @patch("geopandas.read_file")
    def test_uses_main_method_pattern(self, mock_plt, mock_gpd):
        """
        #name(Uses main method pattern)
        """
        try:
            import main
        except AssertionError:
            pass
        finally:
            self.assertFalse(mock_plt.called, "Does not use main method pattern")
            self.assertFalse(mock_gpd.called, "Does not use main method pattern")

    def test_plot(self):
        """
        #name(Test that the output image looks correct)
        """
        plt.clf()

        # Run theirs
        import main

        main.main()

        # Read attempt and solution
        attempt = plt.imread("south_america.png")
        soln = plt.imread("test/expected.png")

        assert attempt.shape == soln.shape, (
            f"Expected a {soln.shape[0]} by {soln.shape[1]} plot, "
            + f"but received {attempt.shape[0]} by {attempt.shape[1]}\n"
            + "You might want to run your solution and compare your plot "
            + "visually with the one shown in the description"
        )

        close = np.isclose(attempt[:, :, :3], soln[:, :, :3])

        score = close.sum() / close.size
        assert score > 0.95, (
            f"Expected graphs to match, current match: "
            + f"{score * 100:.2f}%\nCheck that your plot looks the same "
            + "as the one in the description!"
        )
