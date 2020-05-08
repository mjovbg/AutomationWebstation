
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


