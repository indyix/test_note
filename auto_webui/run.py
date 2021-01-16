"""运行测试用例"""
import pytest
import datetime

# 注意 datetime 不需要加括号
ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

if __name__ == "__main__":
    # pytest.main(["--html={}.html".format(ts), "-m error_test"])
    pytest.main(["--alluredir=allureout".format(ts), "-m update_daily","-s"])
    