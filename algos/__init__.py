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
from abc import ABC, abstractmethod


class Algorithm(ABC):

    def __init__(self):
        self.trained = False

    def fit(self, features, responses):
        result = self.do_fit(features, responses)
        self.trained = True
        return result

    @abstractmethod
    def do_fit(self, features, responses):
        pass

    def predict(self, responses):
        if not self.trained:
            raise Exception('not trained')
        return self.do_predict(responses)

    @abstractmethod
    def do_predict(self, responses):
        pass

    def reset(self):
        self.do_reset()
        self.trained = False

    @abstractmethod
    def do_reset(self):
        pass
