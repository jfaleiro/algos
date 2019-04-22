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

from algos.cv import split_feature_response, evaluate, cross_validation_split
import pandas as pd
import unittest.mock as mock


class Test(unittest.TestCase):

    def test_split_feature_response(self):
        wines = pd.read_csv('data/wines/winequality-red.csv', sep=';')
        feature_column = 'quality'
        f, r = split_feature_response(wines, feature_column)
        self.assertEqual(len(wines), len(f))
        self.assertEqual(len(wines), len(r))
        self.assertEqual(set(f.columns) - set(r.columns),
                         set(f.columns) - set([feature_column]))
        self.assertFalse(feature_column in f.columns)
        self.assertTrue(feature_column in r.columns)

    def test_mocks(self):
        ds = mock.MagicMock()
        ds.len.return_value = 50
        ds.__len__.return_value = 50
        self.assertEqual(50, ds.len())
        self.assertEqual(50, ds.len())
        self.assertEqual(50, len(ds))

    def test_cross_validation_splits(self):
        df = mock.MagicMock()
        df.__len__.return_value = 50
        folds = cross_validation_split(df, 5)
        self.assertEqual(5, len(folds))

    def test_evaluate(self):
        wines = pd.read_csv('data/wines/winequality-red.csv', sep=';')
        feature_column = 'quality'

        algo = mock.MagicMock()
        algo.predict.return_value(wines[feature_column].values)
        algo.fit.return_value(pd.Series())
        errors = evaluate(wines, algo, feature_column, 5)
        self.assertEqual(6, len(errors))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
