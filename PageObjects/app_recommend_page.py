# -*- coding: utf-8 -*-

from .BasePage import BasePage


class AppRecommendPage(BasePage):
    app_recommend_list_nav = 'new UiSelector().text("车家号")'

    # 主app推荐流点击导航栏车家号
    def click_appNav_Chejiahao(self):
        # 点击导航栏【车家号】
        self.get_element(self.app_recommend_list_nav).click()
