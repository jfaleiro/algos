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

from algos import Algorithm
from algos.math import rmse


logger = logging.getLogger(__name__)


class LinearSGDRegression(Algorithm):
    def __init__(self, learning_rate=.01, epochs=5):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.reset()

    def do_fit(self, features, responses):
        yhat_column, responses_column, error_column = '_yhat', '_responses', '_error'
        self.coefficients = [.0] * (len(features.columns) + 1)
        for epoch in range(self.epochs):
            predictions = features.copy()
            predictions[yhat_column] = self.do_predict(features)
            predictions[responses_column] = responses.values
            predictions[error_column] = (predictions[yhat_column] -
                                         predictions[responses_column])
            for _, feature in predictions.iterrows():
                error = feature[error_column]
                self.coefficients[0] -= self.learning_rate * error
                for i, column in enumerate(sorted(set(feature.keys()) - set([error_column, yhat_column, responses_column]))):
                    self.coefficients[i + 1] -= (self.learning_rate *
                                                 error * feature[column])
            logger.info('epoch=%d; error=%f', epoch,
                        rmse(predictions[yhat_column].values, responses.values))

    def do_predict(self, features):
        def yhat(row):
            result = self.coefficients[0]
            for i, column in enumerate(sorted(row.keys())):
                result += self.coefficients[i + 1] * row[column]
            return result
        features = features.copy()
        features['yhat'] = features.apply(yhat, axis=1)
        return features['yhat']

    def do_reset(self):
        self.coefficients = None
