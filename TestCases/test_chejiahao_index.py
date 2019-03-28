# -*- coding: utf-8 -*-

import pytest
import allure
from PageObjects.app_recommend_page import AppRecommendPage
from PageObjects.chejiahao_index_page import ChejiahaoIndexPage
from Common.BaseDriver_bak import base_driver


class TestChejiahaoIndex:

    @pytest.mark.usefixtures("common_driver")
    def test_index_open_success(self, common_driver):
        AppRecommendPage(common_driver).click_appTopNav_Chejiahao()
        AppRecommendPage(common_driver).click_appDownNav_me()
        AppRecommendPage(common_driver).click_appDownNav_index()
