# -*- coding: utf-8 -*-

from .BasePage import BasePage


class AppRecommendPage(BasePage):
    app_recommend_list_nav = 'new UiSelector().text("车家号")'
    app_down_nav_me_id = 'new UiSelector().resourceId("com.cubic.autohome:id/owner_main_RadioButton")'
    app_down_nav_index_id = 'new UiSelector().resourceId("com.cubic.autohome:id/article_main_RadioButton")'

    # 主app推荐流点击头部导航栏车家号
    def click_appTopNav_Chejiahao(self):
        # 点击导航栏头部【车家号】
        self.get_element(self.app_recommend_list_nav).click()

    # 点击主app底部导航【我】
    def click_appDownNav_me(self):
        # 点击app底部导航栏【我】
        self.get_element(self.app_down_nav_me_id).click()

    # 点击主app底部导航【首页】
    def click_appDownNav_index(self):
        # 点击app底部导航栏【首页】
        self.get_element(self.app_down_nav_index_id).click()
