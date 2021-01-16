import datetime
from time import sleep

import pytest

from data.login_data import login_error, login_success, login_invalid
from middleware.handler import Handler
from middleware.pages.boss_login import BossLoginPage
from middleware.pages.center import CenterPage
from middleware.pages.boss_index import BossIndex

# # 读取 Excel 当中的数据
# data_error = Handler.excel.read_data("login_error")
# data_success = Handler.excel.read_data("login_success")
from middleware.pages.jenkins.jks_login import JksLogin

@pytest.mark.update_daily
def test_update_daily(driver):
    # 先初始化页面，测试用到的页面
    # 长春 2670  呼和浩特2657（58-）  沈阳2654 背景2652
    sp_id=2714
    day_start=38
    day_end=11

    daily_static = JksLogin(driver).login("duyixun", 123456).get().move_to_update()
    li =[x for x in range(day_start,day_end,-1)]
    for x in li:
        Handler.logger.info("店铺id{},days:{},剩余{}".format(sp_id, x, x-day_end))
        daily_static.get().update(x,sp_id)
        Handler.logger.info("店铺id:{},天数{}，更新成功".format(str(sp_id), str(x)))


# 注意 datetime 不需要加括号

if __name__ == "__main__":
    ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # pytest.main(["--html={}.html".format(ts), "-m error_test"])
    pytest.main(["-m update_daily","-s"])



