import requests


def visit(
        url,
        method='get',
        params=None,
        data=None,
        json=None,
        **kwargs
):
    """访问接口。
    返回字典 。 res.json()
    """
    res = requests.request(
        method,
        url,
        params=params,
        data=data,
        json=json,
        **kwargs
    )

    try:
        return res.json()
    except Exception as e:
        return None


if __name__ == '__main__':
    pass