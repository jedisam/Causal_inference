"""Test the preprocess module."""
import os
import sys
import unittest

import pandas as pd
import numpy as np


sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts"))
)

from preprocessing import PreProcess


class TESTPHARMASALES(unittest.TestCase):
    """A class for unit-testing function in the preprocess.py file.

    Args:
        unittest.TestCase this allows the new class to inherit
        from the unittest module
    """

    def setUp(self) -> pd.DataFrame:
        """Dataframe that contains the data.

        Returns:
            pd.DataFrame: DF from train_joined.csv file.
        """
        self.df = self.df = pd.DataFrame(
            {
                "radius_mean": 17.99,
                "texture_mean": 122.9,
                "perimeter_mean": 445.1,
                "area_mean": 1798.0,
                "smoothness_mean": 0.118,
                "compactness_mean": 0.099,
                "concavity_mean": 0.067,
                "concave points_mean": 0.0,
                "symmetry_mean": 0.099,
                "fractal_dimension_mean": 0.0,
                "radius_se": 0.0,
                "texture_se": 0.0,
                "perimeter_se": 32.0,
                "area_se": 0.0,
                "smoothness_se": 21.0,
                "compactness_se": 43.0,
                "concavity_se": 12.0,
                "concave points_se": 11.3,
                "symmetry_se": 32.1,
                "diagnosis": "M",
            },
            {
                "radius_mean": 17.99,
                "texture_mean": 122.9,
                "perimeter_mean": 445.1,
                "area_mean": 1798.0,
                "smoothness_mean": 0.118,
                "compactness_mean": 0.099,
                "concavity_mean": 0.067,
                "concave points_mean": 0.0,
                "symmetry_mean": 0.099,
                "fractal_dimension_mean": 0.0,
                "radius_se": 0.0,
                "texture_se": 0.0,
                "perimeter_se": 32.0,
                "area_se": 0.0,
                "smoothness_se": 21.0,
                "compactness_se": 43.0,
                "concavity_se": 12.0,
                "concave points_se": 11.3,
                "symmetry_se": 32.1,
                "diagnosis": "M",
            },
        )

        # tweet_df = self.df.get_tweet_df()

    def test_drop_column(self):
        """Test convert to datetime module."""
        inital_cols = len(self.df.columns)
        df = PreProcess(self.df).drop_column(self.df, 'radius_mean')
        assert len(df.columns) == inital_cols - 1


if __name__ == "__main__":
    unittest.main()
