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
from algos.math import rmse
import numpy as np
import pandas as pd


def cross_validation_split(ds, folds):
    fold_size = len(ds) // folds
    result = []
    for i in range(0, len(ds), fold_size):
        result += [ds[i:i + fold_size]]
    return result


def evaluate(dataset, algorithm, response, folds, **args):
    folds = cross_validation_split(dataset, folds)
    for i, fold in enumerate(folds):
        print('fold %d' % i)
        test_set = fold
        train_folds = folds.copy()
        del train_folds[i]
        train_set = pd.concat(train_folds)
        predictions = algorithm(train_set, test_set, response, **args)
        actuals = fold[response].values
        score = rmse(actuals, predictions)
    return [1]


def split_feature_response(df, response):
    """
    split dataframe in train in test using feature column
    """
    return df[set(df.columns) - set([response])], df[[response]]
