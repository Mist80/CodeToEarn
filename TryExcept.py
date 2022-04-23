#导入存储异常信息的库
import traceback

#将代码放入try语句块中。通常是打开文件，访问网络文件等，容易发生意外错误的操作。
#这里的意外错误，可能是程序本身，也可能是硬件等其他原因。例如断网。
try:
    myValue=8/0
    print(myValue)
#当异常发生时，首先打印异常内容。然后处理异常情况。
except:
    info=traceback.format_exc()
    print(info)
#当没有异常发生时，执行else。except和else，类似if和else的关系
else:
    print("no error")
#无论发生什么都会执行finally。写finally只是为了程序更易读
finally:
    print("finally")