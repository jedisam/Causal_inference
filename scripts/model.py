"""Model Scripts."""

import sys

import numpy as np
import pandas as pd
from logger import Logger


class Model:
    def __init__(self):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        try:
            self.logger = Logger("model.log").get_app_logger()
            self.logger.info("Successfully Instantiated Model Class Object")
        except Exception:
            self.logger.exception("Failed to Instantiate Model Class Object")
            sys.exit(1)

    def train_score(self, models, X_train, X_test, y_train, y_test):
        """Train and score the models.

        Args:
            models (str): model type
            X_train (_type_): _description_
            X_test (_type_): _description_
            y_train (_type_): _description_
            y_test (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Set random seed
        np.random.seed(0)
        # Make an empty dictionary for model scores
        scores = {}
        # Loop through models
        for name, model in models.items():
            # Fit the model to the data
            model.fit(X_train, y_train)
            # Evaluate the model and append its score to the scores dictionary
            scores[name] = model.score(X_test, y_test)
        return scores

    # how many missing values exist or better still what is the % of missing values in the dataset?
