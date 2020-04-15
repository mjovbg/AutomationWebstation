class LocatorsDax:
    # TABS & ACTION MENU ELEMENTS:
    dax_symbol_id                   = '514562|symbolName'
    action_menu_id                  = 'add-to-icon-symbolDetail'
    open_newwindow_css              = '#add-to-menu-symbolDetail > ul > li:nth-child(15) > a'
    constituents_css                = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td.constituents-tab > table > tbody > tr > td:nth-child(1) > a'
    overview_css                    = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(1) > a'
    chart_css                       = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(2) > a'
    topflop_css                     = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(4)'
    timessales_css                  = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(5)'
    news_css                        = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(6)'
    options_css                     = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(7)'
    derivatives_css                 = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(8)'


    # ELEMENTS FOR WAITING ON PAGES:

class LocatorsDaxWaits:
    overview_chart_1d_id            = '1D'
    chart_setdefault_id             = 'set-as-default-button'
    constituents_columnpicker_id    = 'pricePagePerformancePickerLink'
    topflop_reload_css              = '#rightDiv > div.tabs > div.tab-main.tab-mainForSecurity > div.pricepage-icon-container > div.pricepage-Reload > div > a'
    timesales_startdate_id          = 'startDate'
    news_size_id                    = 'newsFontSizeButtonHeadline'
    options_reset_id                = 'securitiesFuturesAndOptionsReset'
    derivatives_columnpicker_id     = 'futures_ttr-413719_Link'

    # ELEMENTS FOR ASSERTING PAGES:

class LocatorsDaxAsserts:
    overview_minichart_id           =   'minichart-img'
    chart_savetemplate_id           =   'save-default-chart-template-menu'
    constituents_quoteboard_css     =   '#rightDiv > div.tabs > div.tab-main.tab-mainForSecurity > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-QuoteBoard > a'
    topflop_clos_css                =   '#rightDiv > div.tabs > div.tab-main.tab-mainForSecurity > div.light-box.constituents.topflop-container > div:nth-child(2) > a.active.not-draggable'
    timesales_starthour_id          =   'startHourMinute'
    news_ecdata_css                 =   '#bonds-search-area-link > a'
    options_search_id               =   'securitiesFuturesAndOptionsSearch'
    derivatives_actionmenu_id       =   'add-to-icon-futures-ttr-413719'

class LocatorsAdidas:
    adidas_id                       = '458757|symbolName'
    # TABS:
    profile_css                     = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width > table > tbody > tr > td:nth-child(3) > a'
    financials_css                  = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width > table > tbody > tr > td:nth-child(5) > a'
    analyzer_css                    = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width > table > tbody > tr > td:nth-child(10) > a'
    traderscreen_css                = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width > table > tbody > tr > td:nth-child(13) > a'

    # WAITS:
    adidasid_wait_1D_id             = '1D'
    profile_wait_website_css        = '#rightDiv > div.tabs > div.tab-main.tab-mainForSecurity.profilePage > div:nth-child(2) > div.left > div.company-data.light-box > table > tbody > tr:nth-child(6) > td.right > a'
    financials_wait_picker_id       = 'PickerLink'
    analyzer_wait_sortarrows_css    = '#RecGV > tbody > tr:nth-child(1) > th.date.time > a'
    tradescreen_wait_picker_id      = 'traderScreenArbitrageListPickerLink'


    # ASSERTS:
    adidasid_assert_chart_id            = 'minichart-img'
    profile_assert_ir_css               = '#rightDiv > div.tabs > div.tab-main.tab-mainForSecurity.profilePage > div:nth-child(2) > div.right > div.investitor-relations.light-box > table > tbody > tr:nth-child(4) > td.right > a'
    financials_assert_estimates_css     = '#rightDiv > div.tabs > div.tab-main.tab-mainForSecurity > div.tab-area.financials-tabs > table > tbody > tr > td:nth-child(2) > a'
    analyzer_assert_chart_css           = '#ChartHolder > img'
    tradescreen_assert_count_css        = '#marketDepth > tbody > tr:nth-child(1) > th:nth-child(1)'

