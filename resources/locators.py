
class MainLocators:
    LOGO_LEFT = "//div[@class='logoleft']"
    LOGO_ON_AYTH_PAGE = "//img[@src='images/productLogo_sc.png']"
    MAIN_FRAME = "//iframe[@class='gwt-Frame x-component']"
    RUS_BUTTON = "//a[@onclick='setLanguage(\"ru_RU\")']"
    CLEAR_BUTTON = "//*[text()='Очистить']"
    SEARCH_BUTTON = "//*[text()='Поиск']"
    LEFT_SIDE_FRAME = "//div[@class='navigationViewTree x-component x-unselectable']"
    SAVE_BUTTON = "//*[text()='Сохранить']"
    YES_BUTTON = "//button[@class='x-btn-text ' and @type='button' and text()='Да']"
    REFRESH_PAGE = "(//td[@class='x-btn-mc'])[13]"
    SHIFT_RIGHT_BUTTON = "(//td[@class='x-table-layout-cell'])[5]"
    OK_BUTTON = "//button[@class='x-btn-text ' and text()='Ok']"


class AuthLocators:
    LOGIN_INPUT = "//input[@name='username']"
    PAS_INPUT = "//input[@name='password']"
    ENTER_BUT = "//input[@name='login']"
    LOGOUT = "//div[@id='logout']"


class UserDefinitionLocators:
    USERNAME_INPUT = "//input[@name='username']"
    PERSON_NO_INPUT = "//input[@name='personelId']"
    PASS_INPUT = "//input[@name='password']"
    CONFIRM_PASS_INPUT = "//input[@name='confirmPassword']"
    FIRST_NAME_INPUT = "//input[@name='firstName']"
    SURNAME_INPUT = "//input[@name='surname']"
    EMAIL_INPUT = "//input[@name='email']"
    PHONE_INPUT = "//input[@id='x-auto-187-input']"
    SAVE_BUT = "(//button[@class='x-btn-text '])[6]"
    SEARCH_BUT = "(//button[@class='x-btn-text '])[5]"
    OPTION_BUT = "//em[@class='x-btn-arrow']"
    CONFIRM_BUT = "(//button[@class='x-btn-text '])[7]"


class UserGroupsLocators:
    NAME_GROUP_INPUT = "//input[@id='x-auto-172-input']"
    USER_INPUT = "//input[@id='x-auto-174-input']"
    DESCRIPTION_INPUT = "//input[@id='x-auto-198-input']"
    MANAGER_INPUT = "//input[@id='x-auto-200-input']"
    SAVE_BUT = "(//button[@class='x-btn-text '])[6]"
    SEARCH_BUT = "(//button[@class='x-btn-text '])[5]"
    CONFIRM_BUT = "(//button[@class='x-btn-text '])[7]"
    OPTION_BUT = "(//button[@class='x-btn-text'])[4]"


class DeviceManagement:
    GROUP_NAME = "#x-auto-72-input"
    NAME_AREA_DEVICES = "//label[contains(text(), 'Имя области устройства:')]/following::input[1]"
    DESCRIPTION_AREA_DEVICES = "//label[contains(text(), 'Описание:')]/following::input[1]"
    CHOICE_GROUP_DEVICES = "//label[contains(text(), 'Выбор Группы устройств:')]/following::input[1]"
    CHOICE_GROUP_USERS = "//label[contains(text(), 'Выбор Группы пользователей:')]/following::input[1]"
    ADD_GROUP_DEVICES_BUTTON = "(//td[@class='x-btn-mc'])[4]"
    ADD_GROUP_USERS_BUTTON = "(//td[@class='x-btn-mc'])[6]"


class LoggingLocators:
    LOGGING = "(//span[@class='x-tree3-node-text'])[12]"
    SESSION_LOG = "(//span[@class='x-tree3-node-text'])[18]"
    LOG_START_TIME = "#x-auto-101-input"
    SESSION_OPTIONS = "(//em[@class='x-btn-arrow'])[1]"
    SHOW_DETAILS = "//span[contains(@class, 'x-menu-item x-unselectable x-component') and contains(text(), 'Показать детали')]"
    DETAILID_SESSION_VIEW_BUTTON = "(//div[@class='x-grid3-cell-inner x-grid3-col-showLogDetail'])[1]"
    TEXT_AREA = "//textarea[@class=' x-form-field x-form-textarea']"



