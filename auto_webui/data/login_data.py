

# 登录失败
login_error = [
    {"username": "", "password": "", "expected": "请输入手机号"},
    {"username": "12", "password": "", "expected": "请输入正确的手机号"},
]

# 登录成功
login_success = [
    {"username":"18684720553", "password": "python", "expected": "我的帐户[python]"}
]

# 登录没哟授权
login_invalid = [
    {"username":"18684720553", "password": "py", "expected": "帐号或密码错误!"}
]

