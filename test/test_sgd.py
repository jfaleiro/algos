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

import unittest

from algos.cv import split_feature_response
from algos.math import rmse
from algos.sgd import LinearSGDRegression
import pandas as pd


class Test(unittest.TestCase):

    def test_fit(self):
        sgd = LinearSGDRegression()
        wines = pd.read_csv('../data/wines/winequality-red.csv', sep=';')
        train_features, train_responses = split_feature_response(
            wines, 'quality')
        sgd.fit(train_features, train_responses)
        print(sgd.coefficients)

    def test_predict(self):
        sgd = LinearSGDRegression()
        wines = pd.read_csv('../data/wines/winequality-red.csv', sep=';')
        train_features, train_responses = split_feature_response(
            wines, 'quality')
        sgd.fit(train_features, train_responses)
        predictions = sgd.predict(train_features)
        print(rmse(predictions.values, train_responses.values))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
