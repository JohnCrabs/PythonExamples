import json
import yaml
import csv
import warnings
import datetime as dt
from enum import Enum


class MESSAGE(Enum):
    ERROR = "error"
    WARN = "warn"
    INFO = "info"
    MSG = "msg"


def currDate():
    """
    Return the current date in the form of (2025/10/29T15:30:18)
    :return: 
    """
    return dt.datetime.now().strftime('%Y/%m/%dT%H:%M:%S')


def myWarn(msg: str, status: MESSAGE = MESSAGE.MSG,
           onErrorExit: bool = False,
           errorCode: int = 900,
           isPrintable: bool = True):
    """
    Returns the msg based on critical status.
    :param isPrintable:
    :param errorCode:
    :param onErrorExit:
    :param msg:
    :param status:
    :return:
    """
    if status == MESSAGE.ERROR:
        msg = f"{currDate()}::ERROR::{msg}"
        if onErrorExit:
            warnings.warn(msg)
            exit(errorCode)
        else:
            if isPrintable:
                print(msg)
            return msg
    elif status == MESSAGE.WARN:
        msg = f"{currDate()}::WARNING::{msg}"
        if isPrintable:
            print(msg)
        return msg
    elif status == MESSAGE.INFO:
        msg = f"{currDate()}::INFO::{msg}"
        if isPrintable:
            print(msg)
        return msg
    else:
        msg = f"{currDate()}::{msg}"
        if isPrintable:
            print(msg)
        return msg


def readYAML(path: str):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data


def writeYAML(o_path, data):
    with open(o_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False)
        myWarn(f"File Saved Successfully on: {o_path}")


def readJSON(path: str):
    with open(path, "r") as f:
        data = json.load(f)
    return data


def writeJSON(o_path, data):
    with open(o_path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        myWarn(f"File Saved Successfully on: {o_path}")


def readCSV(path: str):
    """
    A function that reads a CSV file
    :param path: The CSV path of the file.
    :return: A dict with the header and values of CSV.
    """
    with open(path, mode='r') as f:
        data = csv.reader(f)
        rows = []
        for lines in data:
            rows.append(lines)
        retData = {
            "header": rows[0],
            "values": rows[1:]
        }
    return retData


def writeCSV(o_path, header, values):
    with open(o_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # Write HEADER
        writer.writerow(header)
        # Write VALUES
        writer.writerows(values)


if __name__ == "__main__":
    print(f"Current Date Time: {currDate()}")
    myWarn("This is a simple Message")
    myWarn("This is an Info", MESSAGE.WARN)
    myWarn("This is a Warning", MESSAGE.WARN)
    # myWarn("This is an Error", MESSAGE.ERROR)

    # yamlPath = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/yaml/test.yaml"
    # ds = readYAML(yamlPath)
    # ds["UserName"] = "IoannisKavouras"
    # ds["Password"] = "pws2025"
    # ds["Website"] = "ikavouras.xyz"
    # o_yamlPath = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/yaml/myTest.yaml"
    # writeYAML(o_path=o_yamlPath, data=ds)
    #
    # jsonPath = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/json/starwars.json"
    # ds = readJSON(jsonPath)
    # o_jsonPath = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/json/myStarwars.json"
    # writeJSON(o_path=o_jsonPath, data=ds)
    # csvPath = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/csv/leaves_training_final.csv"
    # testCSV = readCSV(csvPath)
    # o_csvPath = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/csv/leaves_training_final_TEST.csv"
    # firstN = int(testCSV["values"].__len__() / 3)
    # writeCSV(o_csvPath, testCSV["header"], testCSV["values"][:firstN])
