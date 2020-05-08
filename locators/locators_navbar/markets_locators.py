
class MarketsLocators():
    ''''
    Locators for markets button on the navbar (or sidebar) and all markets sub-pages (Quick performance, Performance, Overview, Charts, Quoteboard).
    Locators are split into groups (separated by comments).
    First locator serves for going to the specific page, second for the wait until page is loaded, third to double-check if we are on the right page.
    '''

    # MARKETS PAGE (SAME AS PERFORMANCE):
    # First page:
    markets_css                         =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(1) > td > div > table > tbody > tr > td.icon-container.icon-container-with-tree > a'
    markets_arrows_id                           =   'sort_arrows'       # used for wait
    # markets_visualisation_tab_css           =   '#rightDiv > div.tabs > div.tab-area > table > tbody > tr > td:nth-child(2) > a'


    # Quick performance view:
    market_quick_performance_css        =   '#rightDiv > div.tab-main.main-noTab > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-QuickPerformance > a'
    market_quick_performance_group_id   =   'GroupButtonId'
    market_quick_performance_next_id   =   "nextBtn"

    # Performance view:
    market_performance_css              =   '#rightDiv > div.tab-main.main-noTab > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-Performance > a'
    market_performance_columnpicker_id =   'indicesOverviewPerformancePickerLink'
    market_performance_arrows_xpath      =   '// *[ @ id = "sort_arrows"]'
    # // *[ @ id = "sort_arrows"]

    # Overivew view:
    market_overview_css                 =   '#rightDiv > div.tab-main.main-noTab > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-PricePage > a'
    market_overivew_arrows_xpath        =   "(//span[@id='sort_arrows'])[48]"
    market_overview_picker_id           =   'indicesOverviewPickerLink'


    # Chart view:
    market_chart_css                    =   '#rightDiv > div.tab-main.main-noTab > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-Chart > a'
    market_chart_reload_css             =   '#rightDiv > div.tab-main.main-noTab > div.pricepage-icon-container > div.pricepage-Reload > div > a'
    market_chart_picker_id              =   'ChartPickerLink'

    # Quoteboard view:
    market_quoteboard_css               =   '#rightDiv > div.tab-main.main-noTab > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-QuoteBoard > a'
    market_quoteboard_group_id          =   'GroupButtonId'
    market_quoteboard_picker_id         =   'QuoteBoardPickerLink'


