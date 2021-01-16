@echo off
echo 清理开始....
taskkill /F /IM chromedriver.exe
taskkill /F /IM IE8DriverServer.exe
echo 清理完毕。
pause
echo 按任意键继续....