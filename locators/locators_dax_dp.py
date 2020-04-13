class LocatorsDax:
    # TABS ELEMENTS:
    dax_symbol_id = '514562|symbolName'
    action_menu_id = 'add-to-icon-symbolDetail'
    constituents_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td.constituents-tab > table > tbody > tr > td:nth-child(1) > a'
    overview_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(1) > a'
    chart_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(2) > a'
    topflop_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(4)'
    timessales_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(5)'
    news_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(6)'
    options_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(7)'
    derivatives_css = '#rightDiv > div.tabs > div.tab-area.funds-tab-area.security.tabs-full-width.tabs-less-number > table > tbody > tr > td:nth-child(8)'

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








