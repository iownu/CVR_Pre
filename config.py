# coding: utf-8

real_cvt_feats = [
    'cvt_userID',
    'pre_cvt_userID',
    'cvt_creativeID',
    'pre_cvt_creativeID',
    'cvt_positionID',
    'pre_cvt_positionID',
    'cvt_adID',
    'pre_cvt_adID',
    'cvt_camgaignID',
    'pre_cvt_camgaignID',
    'cvt_advertiserID',
    'pre_cvt_advertiserID',
    'cvt_appID',
    'pre_cvt_appID',
    'cvt_sitesetID',
    'pre_cvt_sitesetID',
    'cvt_appCategory',
    'pre_cvt_appCategory',
    'cvt_appPlatform',
    'pre_cvt_appPlatform',
    'cvt_education',
    'pre_cvt_education',
    'cvt_gender',
    'pre_cvt_gender',
    'cvt_haveBaby',
    'pre_cvt_haveBaby',
    'cvt_marriageStatus',
    'pre_cvt_marriageStatus',
    'cvt_positionType',
    'pre_cvt_positionType',
    'cvt_hometown_c',
    'pre_cvt_hometown_c',
    'cvt_hometown_p',
    'pre_cvt_hometown_p',
    'cvt_residence_c',
    'pre_cvt_residence_c',
    'cvt_residence_p',
    'pre_cvt_residence_p',
    'cvt_telecomsOperator',
    'pre_cvt_telecomsOperator',
    'cvt_connectionType',
    'pre_cvt_connectionType',
    'cvt_clickTime_week',
    # 'pre_cvt_clickTime_week',
]

real_cnt_feats = [
    'app_day_click_cnt',
    'app_uuser_click_cnt',
    'cri_day_click_cnt',
    'cri_uuser_click_cnt',
    'inst_cnt_appcate',
    'inst_cnt_installed',
    'position_day_click_cnt',
    'postion_app_day_click_cnt',
    'postion_cri_day_click_cnt',
    'rpt_click_cnt',
    'rpt_day_click_cnt',
    'tt_cnt_appcate',
    'user_app_day_click_cnt',
    'user_cri_day_click_cnt',
    'user_day_click_cnt',
    'cnt_userID',
    'pre_cnt_userID',
    'cnt_creativeID',
    'pre_cnt_creativeID',
    'cnt_positionID',
    'pre_cnt_positionID',
    'cnt_adID',
    'pre_cnt_adID',
    'cnt_camgaignID',
    'pre_cnt_camgaignID',
    'cnt_advertiserID',
    'pre_cnt_advertiserID',
    'cnt_appID',
    'pre_cnt_appID',
    'cnt_sitesetID',
    'pre_cnt_sitesetID',
    'cnt_appCategory',
    'pre_cnt_appCategory',
    'cnt_appPlatform',
    'pre_cnt_appPlatform',
    'cnt_education',
    'pre_cnt_education',
    'cnt_gender',
    'pre_cnt_gender',
    'cnt_haveBaby',
    'pre_cnt_haveBaby',
    'cnt_marriageStatus',
    'pre_cnt_marriageStatus',
    'cnt_positionType',
    'pre_cnt_positionType',
    'cnt_hometown_c',
    'pre_cnt_hometown_c',
    'cnt_hometown_p',
    'pre_cnt_hometown_p',
    'cnt_residence_c',
    'pre_cnt_residence_c',
    'cnt_residence_p',
    'pre_cnt_residence_p',
    'cnt_telecomsOperator',
    'pre_cnt_telecomsOperator',
    'cnt_connectionType',
    'pre_cnt_connectionType',
    'cnt_clickTime_week',
    'pre_cnt_clickTime_week',
    # 'cnt_creativeID_positionID',
]

real_other = [
    'inst_app_installed',
    'inst_cate_percent',
    'action_cate',
    'action_cate_recent',
    'action_installed',
]

cate_low_dim = [
    'age',
    'appCategory',
    'appPlatform',
    'clickTime_day',
    'clickTime_hour',
    'clickTime_minute',
    'clickTime_week',
    'connectionType',
    'education',
    'gender',
    'haveBaby',
    'hometown_c',
    'hometown_p',
    'marriageStatus',
    'positionType',
    'telecomsOperator',
    'residence_c',
    'residence_p',
    'appID',
    'inst_is_installed',
    'is_day_rpt_first_click',
    'is_day_rpt_last_click',
    'is_rpt_first_click',
    'is_rpt_last_click',
    'tt_is_installed',
    'sitesetID',
]

cate_high_dim = [
    'adID',
    'advertiserID',
    'camgaignID',
    'creativeID',
    'positionID',
    # 'userID',
]

cate_feats = cate_high_dim + cate_low_dim
real_feats = real_cnt_feats + real_cvt_feats + real_other
drop_feats = [
    'cnt_creativeID_positionID',
]

feats = cate_feats + real_feats

chosen_features = [
    'cvt_positionID',
    'pre_cvt_userID',
    'cvt_creativeID',
    'cvt_userID',
    'postion_cri_day_click_cnt',
    'clickTime_day',
    'pre_cvt_camgaignID',
    'pre_cvt_creativeID',
    'is_day_rpt_last_click',
    'is_day_rpt_first_click',
    'cnt_userID',
    'cvt_camgaignID',
    'cvt_connectionType',
    'appID',
    'position_day_click_cnt',
    'rpt_day_click_cnt',
    'inst_app_installed',
    'cnt_connectionType',
    'pre_cvt_positionID',
    'action_cate',
    'cvt_advertiserID',
    'pre_cnt_positionID',
    'pre_cnt_userID',
    'appCategory',
    'tt_cnt_appcate',
    'cvt_sitesetID',
    'pre_cvt_connectionType',
    'cnt_positionID',
    'rpt_click_cnt',
    'cnt_appID',
    'cnt_advertiserID',
    'user_day_click_cnt',
    'cvt_appCategory',
    'age',
    'gender',
    'pre_cnt_advertiserID',
    'advertiserID',
    'positionID',
    'postion_app_day_click_cnt',
    'pre_cvt_advertiserID',
    'pre_cnt_creativeID',
    'cnt_appCategory',
    'cvt_adID',
    'cvt_appID',
    'connectionType',
    'is_rpt_first_click',
    'cnt_appPlatform',
    'pre_cnt_appID',
    'cnt_adID',
    'cri_day_click_cnt',
    'cnt_creativeID',
    'pre_cnt_appCategory',
]

COLUMN_LIST_FILENAME = 'columns_list.pkl'
