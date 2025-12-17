import datetime as dt


def currDateTime():
    """
    A function that returns the current date time.
    :return: Current date time in the form of YYYY/MM/DDThh:mm:ss
    (i.e., 2025/11/12T19:55:31)
    """
    return dt.datetime.now().strftime("%Y/%m/%dT%H:%M:%S")


# JSON Exercises
def json_reader(path):
    pass


def json_writer(dir_path, filename, data):
    pass


# YAML Exercises
def yaml_reader(path):
    pass


def yaml_writer(dir_path, filename, data):
    pass


# CSV Exercises
def csv_reader(path):
    pass


def csv_writer(dir_path, filename, data):
    pass


if __name__ == "__main__":
    print(f"Current DateTime: {currDateTime()}")
