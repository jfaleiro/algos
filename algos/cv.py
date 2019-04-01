#
#      Algos - A collection of toy algos for machine learning.
#
#      Copyright (C) 2019 Jorge M. Faleiro Jr.
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as published
#      by the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import logging

from algos.math import rmse
import pandas as pd


logger = logging.Logger(__name__)


def cross_validation_split(ds, folds):
    """
    split dataframe in folds
    """
    fold_size = len(ds) // folds
    result = []
    for i in range(0, len(ds), fold_size):
        result += [ds[i:i + fold_size]]
    return result


def evaluate(dataset, algorithm, response, folds):
    """
    cross validate algorithm in n folds
    """
    folds = cross_validation_split(dataset, folds)
    scores = []
    for i, fold in enumerate(folds):
        test_set = fold
        train_folds = folds.copy()
        del train_folds[i]
        train_set = pd.concat(train_folds)
        features, responses = split_feature_response(train_set, response)
        algorithm.fit(features, responses)
        features_tests, responses_tests = split_feature_response(
            test_set, response)
        predictions = algorithm.predict(features_tests)
        scores += [rmse(responses_tests.values, predictions.values)]
    return scores


def split_feature_response(df, response):
    """
    split dataframe in train in test using feature column
    """
    return df[set(df.columns) - set([response])], df[[response]]
