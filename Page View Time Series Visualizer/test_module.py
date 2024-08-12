import unittest
import time_series_visualizer as tsv
import matplotlib

class TestTimeSeriesVisualizer(unittest.TestCase):
    def setUp(self):
        self.line_fig = tsv.draw_line_plot()
        self.bar_fig = tsv.draw_bar_plot()
        self.box_fig = tsv.draw_box_plot()

    def test_line_plot(self):
        self.assertEqual(self.line_fig.axes[0].get_title(), 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
        self.assertEqual(self.line_fig.axes[0].get_xlabel(), 'Date')
        self.assertEqual(self.line_fig.axes[0].get_ylabel(), 'Page Views')

    def test_bar_plot(self):
        self.assertEqual(self.bar_fig.axes[0].get_xlabel(), 'Years')
        self.assertEqual(self.bar_fig.axes[0].get_ylabel(), 'Average Page Views')
        self.assertTrue('Jan' in [t.get_text() for t in self.bar_fig.axes[0].get_legend().get_texts()])

    def test_box_plot(self):
        self.assertEqual(self.box_fig.axes[0].get_title(), 'Year-wise Box Plot (Trend)')
        self.assertEqual(self.box_fig.axes[0].get_xlabel(), 'Year')
        self.assertEqual(self.box_fig.axes[0].get_ylabel(), 'Page Views')
        self.assertEqual(self.box_fig.axes[1].get_title(), 'Month-wise Box Plot (Seasonality)')
        self.assertEqual(self.box_fig.axes[1].get_xlabel(), 'Month')
        self.assertEqual(self.box_fig.axes[1].get_ylabel(), 'Page Views')

if __name__ == "__main__":
    unittest.main()
