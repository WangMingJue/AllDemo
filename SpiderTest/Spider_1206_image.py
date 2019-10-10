import requests
from PIL import Image
from json import loads

from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
session = requests.session()


def getCheckImgIndex():
    i = 0
    for i in range(10000):
        url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
        response = session.get(url=url, headers=headers, verify=False)
        # 把验证码图片保存到本地
        f = open(f'./12306/{i}.jpg', 'wb')  # 也可以是其他任何文件名，图片保存在当前目录下
        f.write(response.content)
        f.close
        i += 1


if __name__ == '__main__':
    getCheckImgIndex()
