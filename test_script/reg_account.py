import pymysql as pymysql
from pymysql.cursors import DictCursor


# 替换
# last_passport_id    last_pf_id
# #id# :int  #phone#  #wx_unionid#  #uuid#   #passport_id# : int    #id_name#

reg_phone = None


class MysqlHandlerTM(object):
    def __init__(self,
                 host="pftest.senguo.me",
                 port=3306,
                 user="test",
                 password="senguo_mysql",
                 charset='utf8',
                 cursorclass=DictCursor,
                 read_timeout=15,
                 write_timeout=15
                 ):

        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            cursorclass=cursorclass,
            read_timeout=read_timeout,
            write_timeout=write_timeout
        )

        self.cursor = self.conn.cursor()

    def add_one(self):
        basic_sql_for_senguopf = "INSERT INTO senguopf.account_info(`id`, `create_date_timestamp`, `phone`, `email`, `password`, `sex`, " \
                                 "`nickname`, `realname`, `headimgurl`, `wx_link`, `phone_check`, `wx_unionid`, `wx_openid`, `wx_country`, " \
                                 "`wx_province`, `wx_city`, `uuid`, `passport_id`, `birthday`, `senguo_staff`, `multi_login_count`, `is_realman_verified`, " \
                                 "`id_name`, `id_card_num`, `id_card_front`, `id_card_back`, `verify_img`, `identity`, `last_used_identity`) VALUES (#n_pf_id#, 1604479666, '#n_phone#'," \
                                 " NULL, '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 1, '微信昵称', NULL, 'https://thirdwx.qlogo.cn/mmo" \
                                 "pen/vi_32/kibtoU9pJ7d0ICQzDj8iafX7vWicmOK8141EWYwJoNcyqPWgsGXCeCdEpAubUyTLmkiacx8cXhiczd4Lo0Q5U5wvXicA/132', '', 1, '#n_wx_unionid#', NULL," \
                                 " '中国', '湖北', '武汉', '#n_uuid#', #n_passport_id#, NULL, 0, 1, 1, '#n_id_name#', '500400199809253400', '2029b1063e124" \
                                 "923b68e522cdd3afc71.jpg', 'ec547ede2c384be2957d1e43d169878c.jpg', 'pfeasy/MTYwNDQ3OTQ0NTAwMS1lN2YzM2I4MQ==.jpg', 1, 0);"

        basic_sql_for_senguo_auth = "INSERT INTO `senguo-auth`.`passport`(`id`, `uuid`, `phone`, `wx_unionid`, `qq_account`, `password`, `email`, `can_login`, " \
                                    "`can_login_ls`, `can_login_pf`, `can_login_cg`, `can_login_ph`, `create_time`, `last_login_time`, `wx_openid`, `nickname`, `realname`, " \
                                    "`headimgurl`, `sex`, `birthday`, `senguo_staff`) VALUES (" \
                                    "#n_passport_id#, NULL, '#n_phone#', '#n_wx_unionid#', NULL, '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', " \
                                    "NULL, 1, 1, 1, 1, 1, '2020-11-04 16:42:24', '2020-11-05 12:13:57', NULL, '微信昵称', NULL, 'https://thirdwx.qlogo.cn/mmopen/vi_32/kibtoU9pJ7d0ICQ" \
                                    "zDj8iafX7vWicmOK8141EWYwJoNcyqPWgsGXCeCdEpAubUyTLmkiacx8cXhiczd4Lo0Q5U5wvXicA/132',1, '0000-00-00', 0);"

        # 替换
        # last_passport_id    last_pf_id     last_phone
        # #n_pf_id# :int  #n_phone#  #wx_unionid#  #uuid#   #passport_id# : int    #id_name#

        if reg_phone:
            n_phone = str(reg_phone)
        else:
            n_phone = str(int(self.get_last_phone()) + 132)
        n_passport_id = str(self.get_last_passport_id() + 1)
        n_pf_id = str(self.get_last_pf_id() + 1)
        n_wx_unionid = "oxkR_jgyp5TgQn5uQR63" + n_phone
        n_uuid = n_phone[3:11]
        n_id_name = "身份证名"

        sql_for_senguopf = basic_sql_for_senguopf.replace("#n_phone#", n_phone).replace("#n_passport_id#",
                                                                                        n_passport_id).replace(
            "#n_pf_id#", n_pf_id).replace("#n_wx_unionid#", n_wx_unionid).replace("#n_uuid#", n_uuid).replace(
            "#n_id_name#", n_id_name).replace("'微信昵称'",f"'微信昵称+{n_phone[5:11]}'")
        sql_for_senguo_auth = basic_sql_for_senguo_auth.replace("#n_phone#", n_phone).replace("#n_passport_id#",
                                                                                              n_passport_id).replace(
            "n_pf_id", n_pf_id).replace("#n_wx_unionid#", n_wx_unionid).replace("#n_uuid#", n_uuid).replace(
            "#n_id_name#", n_id_name).replace("'微信昵称'",f"'微信昵称+{n_phone[5:11]}'")

        sql_for_senguopf_chain = sql_for_senguopf.replace("senguopf.account_info", "`senguopf_chain`.`account_info`")

        try:
            self.cursor.execute(sql_for_senguopf)
            self.cursor.execute(sql_for_senguo_auth)
            self.conn.commit()
            print("注册账号：{}，密码：123456".format(n_phone))
            # print(sql_for_senguopf_chain)
            return sql_for_senguopf_chain
        except Exception as e:
            self.conn.rollback()
            raise e

    def get_last_passport_id(self):
        sql_get_last_passport_id = "SELECT id from `senguo-auth`.`passport` ORDER BY id DESC LIMIT 1;"
        self.cursor.execute(sql_get_last_passport_id)
        return self.cursor.fetchone()["id"]

    def get_last_pf_id(self):
        sql_get_last_pf_id = "SELECT id from `senguopf`.`account_info` ORDER BY id DESC LIMIT 1;"
        self.cursor.execute(sql_get_last_pf_id)
        return self.cursor.fetchone()["id"]

    def get_last_phone(self):
        sql_get_last_phone = "SELECT phone from `senguopf`.`account_info` WHERE phone LIKE '137%' ORDER BY id DESC LIMIT 1;"
        self.cursor.execute(sql_get_last_phone)
        return self.cursor.fetchone()["phone"]


class MysqlHandlerChain():
    def __init__(self,
                 host="121.196.199.202",
                 port=30306,
                 user="senguo",
                 password="senguo123",
                 charset='utf8',
                 cursorclass=DictCursor,
                 read_timeout=15,
                 write_timeout=15,
                 sql=""
                 ):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            cursorclass=cursorclass,
            read_timeout=read_timeout,
            write_timeout=write_timeout
        )
        self.sql = sql
        self.cursor = self.conn.cursor()

    def add_one(self):
        try:
            self.cursor.execute(self.sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


def add_one_account():
    mh1 = MysqlHandlerTM()
    sql = mh1.add_one()
    mh2 = MysqlHandlerChain(sql=sql)
    mh2.add_one()


if __name__ == '__main__':
    for i in range(1):
        add_one_account()
        i += 1

    # add_one_account()