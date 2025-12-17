import examples.ex01.myUtils as myUtils
import examples.ex01.myPath as myPath


class MyLog:
    def __init__(self, logPath: str):
        self.__path = logPath
        self.__genFile()

    @property
    def path(self):
        return self.__path

    def __genFile(self):
        with open(self.path, "w") as f:
            msg = myUtils.myWarn(msg="<==== MyLogging ====>", isPrintable=False)
            f.write(msg)
            f.close()

    def append(self, msg, status: myUtils.MESSAGE = myUtils.MESSAGE.MSG):
        msg = myUtils.myWarn(
            msg=msg,
            status=status,
            isPrintable=False
        )
        with open(self.path, "a") as f:
            f.write(f"\n{msg}")


if __name__ == "__main__":
    lPath = "D:/Programming/PythonCoding/99_Other/PythonExamples/data/logs/log.txt"
    mLog = MyLog(lPath)
    mLog.append(
        msg="Hello World!",
        status=myUtils.MESSAGE.INFO
    )
    mLog.append(
        msg="THIS IS A WARNING",
        status=myUtils.MESSAGE.WARN
    )

