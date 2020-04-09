# Locators for side bar (navigation menu) and its pages.

class LocatorsHp:
    markets_css         =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(1) > td > div > table > tbody > tr > td.icon-container.icon-container-with-tree > a'
    arrows_id   =   'sort_arrows'

    currencies_css      =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td.icon-container.icon-container-with-tree > a'
    # use arrows_id
    commodities_css     =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(3) > td > div > table > tbody > tr > td.icon-container.icon-container-with-tree > a'
    # use arrows_id

    fix_income_css      =   '#fixedIncomeButton > table > tbody > tr > td.icon-container.icon-container-with-tree > a'
    # use arrows_id

    futures_css         =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(5) > td > div > table > tbody > tr > td.icon-container.icon-container-with-tree > a'
    # use arrows_id

    news_css            =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(6) > td > div > table > tbody > tr > td > a'
    news_home_css       =   '#reactnews > div > div.news-overview-header > ul > li:nth-child(1) > span'

    workspace_css       =   '#personalPageButton > table > tbody > tr > td.icon-container.icon-container-with-tree > a'
    workspace_new_css   =   '#watchlistTabs > li.unsortable'

    watchlist_css       =   '#watchlistButton > table > tbody > tr > td > a'
    watchlist_new_css   =   '#rightDiv > div.main-pages-header.watchlist > a:nth-child(4)'

    covid_css           =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(9) > td > div > table > tbody > tr > td > a'
    covid_map_css       =   '#rightDiv > table > tbody > tr > td.coronaButtons > a.selected'

    trump_css           =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(10) > td > div > table > tbody > tr > td > a'
    trump_icon_css      =   '#rightDiv > div.main-pages-header.trumpEfect > div'

    screener_css        =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(11) > td > div > table > tbody > tr > td > a'
    screener_tab_css    =   '#ScreenerNavigation > table > tbody > tr > td:nth-child(2) > a'

    funds_css           =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(12) > td > div > table > tbody > tr > td > a'
    funds_overview_css  =   '#rightDiv > div.main-pages-header.funds > a.selected'

    portfolio_css       =   '#portfolioButton > table > tbody > tr > td > a'
    portfolio_new_css   =   '#rightDiv > div.main-pages-header.portfolio > a:nth-child(3)'

    calendar_css        =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(14) > td > div > table > tbody > tr > td > a'
    calendar_filter_css =   '#rightDiv > div.no-top-padding.tab-area > table > tbody > tr > td.current > a'

    analyzer_css        =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(15) > td > div > table > tbody > tr > td > a'
    analyzer_filter_css =   '#rightDiv > div.no-top-padding.tab-area > table > tbody > tr > td:nth-child(3) > a'

    backtester_css      =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(16) > td > div > table > tbody > tr > td > a'
    backtester_help_css =   '#text-help'

    alerts_css          =   '#alertsButton > table > tbody > tr > td > a'
    alerts_calendar_css =   '#rightDiv > div.main-pages-header.alerts > a:nth-child(4)'

    economic_data_css   =   '#economicDataButton > table > tbody > tr > td > a'
    economic_filter_css =   '#rightDiv > div.main-pages-header.economicCalendar > a.selected'

    etfs_css            =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(19) > td > div > table > tbody > tr > td > a'
    etf_overview_css    =   '#rightDiv > div.main-pages-header.etf > a'

    derivatives_css     =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(20) > td > div > table > tbody > tr > td > a'
    derivatives_issuers_css = '#rightDiv > div.main-pages-header.derivatives > a.selected'

    realtime_css        =   '#lowerDiv > div.navigation-vertical-container > table > tbody > tr:nth-child(21) > td > div > table > tbody > tr > td > a'
    # use arrows_id

    feedback_css        =   '#feedbackButtonVericalNav > td > div > table > tbody > tr > td > div'

    user_button_id = 'user-button'
    logout_css     = '#user-menu > ul > li:nth-child(11) > a'

    # LOCATORS THAT SERVE FOR ASSERTIONS:
    # Used for markets, currencies, commodities, fixed income, futures
    column_picker_class     =   'columnPicker-icon'

    # used for news:
    news_search_class       =   'newsSearchField'

    # used for workspace (workspace title):
    workspace_assert_css     =   '#rightDiv > div.main-pages-header.personal-pages > div'

    # used for watchlist (watchlist title):
    watchlist_assert_css     =   '#rightDiv > div.main-pages-header.watchlist > div'

    # used for covid(covid title):
    covid_assert_css        =   '#rightDiv > table > tbody > tr > td.title'

    # used for trump effect (trump title):
    trump_assert_css        =   '#rightDiv > div.main-pages-header.trumpEfect > div'

    # used for screener (screener title):
    screener_assert_css     =   '#rightDiv > div.main-pages-header.screenerHeader > div'

    # used for funds
    funds_assert_css       =   '#rightDiv > div.main-pages-header.funds > div'

    # used for portfolio:
    portfolio_assert_css    =   '#rightDiv > div.main-pages-header.portfolio > div'

    # used for calendar
    calendar_assert_css     =   '#rightDiv > div.main-pages-header.companyCalendar > div'

    # used for analyzer:
    analyzer_assert_css     =   '#rightDiv > div.main-pages-header.analyzerHeader > div'

    # used for backtester:
    backtester_assert_css   =   '#rightDiv > div.main-pages-header.back-tester > div.title'

    # used for alerts:
    alerts_assert_css       =   '#rightDiv > div.main-pages-header.alerts > div'

    # used for economic data:
    economic_assert_css     =   '#rightDiv > div.main-pages-header.economicCalendar > div'

    # used for etfs:
    etf_assert_css          =   '#rightDiv > div.main-pages-header.etf > div'

    # used for derivatives:
    derivatives_assert_css  =   '#rightDiv > div.main-pages-header.derivatives > div'

    # used for real time:
    realtime_assert_css     =   '#rightDiv > div.main-pages-header.realtimeIn > div'

