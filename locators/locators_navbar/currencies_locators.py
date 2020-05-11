
class CurrenciesLocators:

    ''''
    Locators for currencies button on the navbar (or sidebar) and all currencies sub-pages (Quick performance, Performance, Overview, Charts, Quoteboard).
    Locators are split into groups (separated by comments).
    First locator serves for going to the specific page, second for the wait until page is loaded, third to double-check if we are on the right page.
    '''
    # PERFORMANCE VIEW
    currencies_icon_link                =   'Currencies'
    currencies_peformance_picker_id     =   'currenciesPerformancePickerLink'   # Use it for wait
    currencies_performance_arrows_xpath = '// *[ @ id = "sort_arrows"]'

    # QUICK PERFORMANCE VIEW
    currencies_quick_performance_css    =   '#rightDiv > div.tab-main > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-QuickPerformance > a'
    currencies_quick_performance_next_id =   'nextBtn'
    currencies_quick_performance_arrows_xpath   =   '//*[@id="rightDiv"]/div[4]/div[2]/table/tbody/tr[1]/th[1]/a/span[2]'

    # OVERVIEW PAGE
    currencies_overview_css             =   '#rightDiv > div.tab-main > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-PricePage > a'
    currencies_overview_arrows_id       =   'sort_arrows'
    currencies_overview_picker_id       =   'currenciesPickerLink'

    # CHARTS PAGE
    currencies_chart_css                =   '#rightDiv > div.tab-main > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-Chart > a'
    currencies_chart_picker_id          =   'ChartPickerLink'
    currencies_chart_reload_css         =   '#rightDiv > div.tab-main > div.pricepage-icon-container > div.pricepage-Reload > div > a'

    # QUOTEBOARD PAGE
    currencies_quoteboard_css           =   '#rightDiv > div.tab-main > div.pricepage-icon-container > div.pricepage-icon.pricepage-icon-QuoteBoard > a'
    currencies_quoteboard_picker_id     =   'QuoteBoardPickerLink'
    currencies_quote_board_aud_cad_css  =   '#rightDiv > div.tab-main > div.light-box.currencies > div.board-view.board-view-QuoteBoard > div > div:nth-child(1) > div > a'

    # CROSS RATES PAGE
    cross_rates_link                    =   'Cross Rates'
    cross_eur_usd_last_id               =   'crossRates_13425773|last'
    cross_usd_jpy_last_id               =   'crossRates_13425921|last'

    # CRYPTOS PAGE
    cryptos_link                        =   'Cryptos'
    cryptos_btc_flag_css                =   '#rightDiv > div.light-box > table > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(1) > span'
    cryptos_btc_link                    =   'Bitcoin'

    # CRYPTO PAIRS PAGE
    crypto_pairs_link                   =   'Crypto Pairs'
    crypto_pairs_group_id               =   'GroupButtonId'
    crypto_pairs_picker_id              =   'cryptoCurrenciesPerformancePickerLink'

    # CRYPTO NEWS PAGE
    crypto_news_link                    =   'Crypto currency news'
    crypto_news_chart_reload_css        =   '#canvasChartDiv > div.tt_chartContainer > div.tt_canvasContainer.tt_cursorDefault > div.tt_panelDiv.tt_firstPanel > div:nth-child(2) > div.tt_symbol_reload'
    crypto_news_chart_resizer_id        =   'resizer'
