# -*- coding: utf-8 -*-

from .BasePage import BasePage


class ChejiahaoIndexPage(BasePage):
    index_ball_RankingList = 'new UiSelector().text("排行榜")'
    index_ball_attentions = 'new UiSelector().text("关注作者")'

    # 获取车家号首页球文案-排行榜
    def get_indexBall_content_ranklist(self):
        ball_content = self.get_element(self.index_ball_RankingList).text
        return ball_content

    # 点击车家号首页求-关注作者
    def click_indexBall_attention(self):
        self.get_element(self.index_ball_attentions).click()
