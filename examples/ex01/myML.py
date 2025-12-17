import examples.ex01.myUtils as myUtils
import examples.ex01.myPath as myPath
import examples.ex01.myLog as myLog

import numpy as np


class MyML:
    def __init__(self, dataPath):
        self.__path = dataPath
        self.__rawDS = {}

    @property
    def path(self):
        return self.__path

    @property
    def raw(self):
        return self.__rawDS

    @raw.setter
    def raw(self, value: dict):
        self.__rawDS = value

    def read(self):
        ds = myUtils.readCSV(self.path)
        self.raw = {}
        for __index__ in range(ds["header"].__len__()):
            self.raw[ds["header"][__index__]] = [_val_[__index__] for _val_ in ds["values"]]

    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:  # Failed
            return False

    def gen_train_test(self, X_cols: [], y_cols: []):
        Xs = {}
        ys = {}

        for __x__ in X_cols:
            if __x__ in self.raw.keys():
                if type(self.raw[__x__][0]) is str and self.is_number(self.raw[__x__][0]):
                    x = np.array(self.raw[__x__])
                    Xs[__x__] = x.astype(np.float32)
                else:
                    Xs[__x__] = np.array(self.raw[__x__])

        for __y__ in y_cols:
            if __y__ in self.raw.keys():
                if type(self.raw[__y__][0]) is str and self.is_number(self.raw[__y__][0]):
                    y = np.array(self.raw[__y__])
                    ys[__y__] = y.astype(np.float32)
                else:
                    ys[__y__] = np.array(self.raw[__y__])

        print(Xs)


if __name__ == "__main__":
    path = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/csv/regression/weatherHistory.csv"
    mml = MyML(dataPath=path)
    mml.read()

    X_values = [
        "PrecipType",
        "Temperature",
        "ApparentTemperature",
        "Humidity",
        "WindSpeed",
        "WindBearing",
        "Visibility",
        "LoudCover",
        "Pressure"
    ]
    y_values = ["DailySummary"]

    mml.gen_train_test(X_cols=X_values, y_cols=y_values)

