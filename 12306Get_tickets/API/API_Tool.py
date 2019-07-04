from PyQt5.Qt import *
import requests
import re
import base64


class API(object):

    #----------------------------------------------------------------------
    Xq_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64'
    # 构造请求表单
    Xq_parmas = {
        "login_site": "E",
        "module": "login",
        "rand": "sjrand",
        "1555036551227": "",
        "callback": "jQuery19108754385247664451_1555036549517",
        "_": "1555036549518",
    }
    # 构造请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/73.0.3683.86 Safari/537.36"
    }
    #----------------------------------------------------------------------

    #----------------------------------------------------------------------
    # # 校验验证码

    CHECK_YZM_URL = "https://kyfw.12306.cn/passport/captcha/captcha-check"
    #----------------------------------------------------------------------

class APITool(QObject):
    session = requests.session()

    @classmethod
    def download_verification_code(cls):
        # 对图片页发送请求
        response = cls.session.get(url=API.Xq_url, params=API.Xq_parmas, headers=API.headers).text
        # 获取图片数据
        image_bs64 = re.findall('"image":"(.*?)",', response)[0]
        # 解码数据
        image = base64.b64decode(image_bs64)
        # 保存图片
        with open('API/yzm.jpg', 'wb') as f:
            f.write(image)

        return "API/yzm.jpg"

    @classmethod
    def check_verification_code(cls,verification_code):
        YZM_params = \
            {
                "answer": verification_code,
                "rand": "sjrand",
                "login_site": "E",
            }
        response = cls.session.post(url=API.CHECK_YZM_URL, data=YZM_params)
        dic = response.json()
        print(response.json())
        return dic['result_code'] == '4'




if __name__ == '__main__':
    APITool.download_verification_code()
