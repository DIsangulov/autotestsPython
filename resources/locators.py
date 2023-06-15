
class MainLocators:
    LOGO_LEFT = "//div[@class='logoleft']"
    LOGO_ON_AYTH_PAGE = "//img[@src='images/productLogo_sc.png']"
    SEARCH_BUTTON = "//*[text()='Поиск']"
    MAIN_FRAME = "//iframe[@class='gwt-Frame x-component']"
    LEFT_SIDE_FRAME = "//div[@class='navigationViewTree x-component x-unselectable']"
    RUS_BUTTON = "//a[@onclick='setLanguage(\"ru_RU\")']"


class AuthLocators:
    LOGIN_INPUT = "//input[@name='username']"
    PAS_INPUT = "//input[@name='password']"
    ENTER_BUT = "//input[@name='login']"
    LOGOUT = "//div[@id='logout']"


class LoggingLocators:
    LOGGING = "(//span[@class='x-tree3-node-text'])[12]"
    SESSION_LOG = "(//span[@class='x-tree3-node-text'])[18]"
    LOG_START_TIME = "#x-auto-101-input"
    SESSION_OPTIONS = "(//em[@class='x-btn-arrow'])[1]"
    SHOW_DETAILS = "//span[contains(@class, 'x-menu-item x-unselectable x-component') and contains(text(), 'Показать детали')]"
    DETAILID_SESSION_VIEW_BUTTON = "(//div[@class='x-grid3-cell-inner x-grid3-col-showLogDetail'])[1]"
    TEXT_AREA = "//textarea[@class=' x-form-field x-form-textarea']"

