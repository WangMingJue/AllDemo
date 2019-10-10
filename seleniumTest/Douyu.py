import time
import re
from selenium import webdriver


def regular_with_attr(pattern, elements, attribute):
    """
    使用正则来寻找元素
    :param pattern: 正则
    :param elements: 所有元素（List）
    :param attribute: 以什么元素属性来查找
    :return:
    """
    pat = re.compile(pattern)
    for element in elements:
        html_content = element.get_attribute(attribute)
        data = re.match(pat, html_content)
        if data:
            return data.group(0)
    return None


# 初始化Web
driver = webdriver.Chrome()
# 设置Web窗口大小
driver.set_window_size(1366, 768)
# 打开瓜皮蛙蛙的鱼吧
driver.get("https://yuba.douyu.com/group/2982")
# 查找[非登录]状态的元素
span_element = driver.find_elements_by_xpath('//span')
user_rect = regular_with_attr('(.*)?navRightItemAvatarNotLogin(.*)?', span_element, 'class')
# 如果存在，就进行登录操作
if user_rect:
    # 点击元素，弹出登录窗口
    driver.find_element_by_class_name(user_rect).click()
    # 切换到登录窗口（查找class名字为passport-iframe-con的div，再查这个div下的iframe）
    driver.switch_to.frame(driver.find_element_by_xpath("//div[contains(@class,'passport-iframe-con')]/iframe"))
    # 点击[密码登录]（查找属性data-type名字为login的任意元素）
    driver.find_element_by_xpath("//*[contains(@data-type,'login')]").click()
    # 点击[昵称登录]（查找属性data-subtype名字为login-by-nickname的任意元素）
    driver.find_element_by_xpath("//*[contains(@data-subtype,'login-by-nickname')]").click()
    # 输入账号密码，并点击登录
    driver.find_element_by_name("username").send_keys("NoDreamBig")
    driver.find_element_by_name("password").send_keys("3121321whyljl")
    driver.find_element_by_xpath("//input[contains(@type, 'submit')]").click()

time.sleep(5)
# driver.quit()

