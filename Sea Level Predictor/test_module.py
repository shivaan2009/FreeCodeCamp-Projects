import unittest
import sea_level_predictor
import matplotlib.pyplot as plt

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot(self):
        # Test the plot creation
        fig = sea_level_predictor.draw_plot()
        self.assertIsInstance(fig, plt.Axes)
