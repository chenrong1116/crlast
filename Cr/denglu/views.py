from django.shortcuts import render
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.


class Code:

    def __init__(self, browser):
        self.browser = browser

    def move(self,num):
        try:
            element = self.browser.find_element_by_class_name('touclick-img-par')
            for i in num:
                a = int(i)
                if a <= 4:
                    ActionChains(self.browser).move_to_element_with_offset(element,40+72*(a-1),73).click().perform()
                else :
                    a -= 4
                    ActionChains(self.browser).move_to_element_with_offset(element,40+72*(a-1),145).click().perform()
        except:
            print('元素不可选！')

    def main(self,num):
        self.move(num)




class Index(View):
    sava_info ={}

    def get(self,request):
        browser = webdriver.Chrome()
        browser.set_window_size(800, 600)
        browser.get('https://kyfw.12306.cn/otn/login/init')
        code = Code(browser)
        button = browser.find_element_by_id('loginSub')

        self.sava_info['brower'] = browser
        self.sava_info['button'] = button
        self.sava_info['code'] = code

        input_name = browser.find_element_by_id('username')
        input_pd = browser.find_element_by_id('password')
        time.sleep(1)
        input_name.send_keys('15157757088')
        input_pd.send_keys('zcl1314')
        return render(request, '12306.html')

    def post(self,request):
        num = request.POST.get('num')
        brower = self.sava_info['brower']
        code = self.sava_info['code']
        button = self.sava_info['button']

        code.move(num.split())
        button.click()
        time.sleep(2)
        return HttpResponseRedirect("/")