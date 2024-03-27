from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import django
from django.conf import settings
import os


def before_all(context):
    # 确保 Django 设置正确加载
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    django.setup()

    # 初始化 WebDriver 的选项
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器界面
    chrome_options.add_argument("--no-sandbox")  # 在 Docker 或 CI 系统中运行时需要
    chrome_options.add_argument("--disable-dev-shm-usage")  # 避免资源限制问题
    chrome_options.add_argument("--window-size=1920,1080")  # 设置窗口大小

    # 初始化 WebDriver
    # 请根据您的 ChromeDriver 路径进行调整
    # 如果 ChromeDriver 在您的 PATH 中，您可以直接使用 webdriver.Chrome(options=chrome_options)
    context.browser = webdriver.Chrome(options=chrome_options)

    # 设置隐式等待时间
    context.browser.implicitly_wait(5)

def after_all(context):
    # 测试结束后关闭浏览器
    if hasattr(context, 'browser'):  # 检查 context 对象是否有 'browser' 属性
        context.browser.quit()

def before_scenario(context, scenario):
    # 每个场景开始前可以进行的操作（如果有需要）
    pass

def after_scenario(context, scenario):
    # 每个场景结束后可以进行的操作（如果有需要），例如清理测试数据
    pass
