
class LocatorsLP:
    username_id = "userName"
    password_id = "password"
    eula_css_check = '#login > table:nth-child(4) > tbody > tr:nth-child(4) > td > label.checkBoxLabel > span'
    eula_confirm = '//*[@id="login"]/table[1]/tbody/tr[4]/td/label[1]/span'
    login_btn_id = "loginUser"
    eula_warning_id = 'diseabledCookiesMessage'
    user_button_id = 'user-button'
    logout_css     = '#user-menu > ul > li:nth-child(11) > a'
    account_settings_css = '#user-menu > ul > li:nth-child(1) > a'
    clear_chart_css     =   '#rightDiv > div.tabs > div.tab-main > div:nth-child(25) > table > tbody > tr:nth-child(1) > td > label > input[type=checkbox]'
    clear_custom_css    =   '#rightDiv > div.tabs > div.tab-main > div:nth-child(25) > table > tbody > tr:nth-child(2) > td > label > input[type=checkbox]'
    clear_button_id     =   'resetAllSettingsButton'
    clear_custom_yes_css =  '#resetAllSettingsDialog > form > p > input.button.save'
