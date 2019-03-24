# -*- coding: utf-8 -*-

import pytest
import allure
from PageObjects.app_recommend_page import AppRecommendPage
from PageObjects.chejiahao_index_page import ChejiahaoIndexPage
from Common.BaseDriver_bak import base_driver


class TestChejiahaoIndex:

    @pytest.mark.usefixtures("common_driver")
    def test_index_open_success(self, common_driver):
        AppRecommendPage(common_driver).click_appNav_Chejiahao()
        ball_content = ChejiahaoIndexPage(common_driver).get_indexBall_content_ranklist()
        assert ball_content == "排行榜"
        ChejiahaoIndexPage(common_driver).click_indexBall_attention()
