# -*- coding: utf-8 -*-
#
from ..const import CONFIG, DYNAMIC

# Storage settings
COMMAND_STORAGE = {
    'ENGINE': 'terminal.backends.command.db',
}
DEFAULT_TERMINAL_COMMAND_STORAGE = {
    "default": {
        "TYPE": "server",
    },
}
TERMINAL_COMMAND_STORAGE = DYNAMIC.TERMINAL_COMMAND_STORAGE or {}
DEFAULT_TERMINAL_REPLAY_STORAGE = {
    "default": {
        "TYPE": "server",
    },
}
TERMINAL_REPLAY_STORAGE = DYNAMIC.TERMINAL_REPLAY_STORAGE

# Security settings
SECURITY_MFA_AUTH = DYNAMIC.SECURITY_MFA_AUTH
SECURITY_COMMAND_EXECUTION = DYNAMIC.SECURITY_COMMAND_EXECUTION
SECURITY_LOGIN_LIMIT_COUNT = DYNAMIC.SECURITY_LOGIN_LIMIT_COUNT
SECURITY_LOGIN_LIMIT_TIME = DYNAMIC.SECURITY_LOGIN_LIMIT_TIME  # Unit: minute
SECURITY_MAX_IDLE_TIME = DYNAMIC.SECURITY_MAX_IDLE_TIME  # Unit: minute
SECURITY_PASSWORD_EXPIRATION_TIME = DYNAMIC.SECURITY_PASSWORD_EXPIRATION_TIME # Unit: day
SECURITY_PASSWORD_MIN_LENGTH = DYNAMIC.SECURITY_PASSWORD_MIN_LENGTH  # Unit: bit
SECURITY_PASSWORD_UPPER_CASE = DYNAMIC.SECURITY_PASSWORD_UPPER_CASE
SECURITY_PASSWORD_LOWER_CASE = DYNAMIC.SECURITY_PASSWORD_LOWER_CASE
SECURITY_PASSWORD_NUMBER = DYNAMIC.SECURITY_PASSWORD_NUMBER
SECURITY_PASSWORD_SPECIAL_CHAR = DYNAMIC.SECURITY_PASSWORD_SPECIAL_CHAR
SECURITY_PASSWORD_RULES = [
    'SECURITY_PASSWORD_MIN_LENGTH',
    'SECURITY_PASSWORD_UPPER_CASE',
    'SECURITY_PASSWORD_LOWER_CASE',
    'SECURITY_PASSWORD_NUMBER',
    'SECURITY_PASSWORD_SPECIAL_CHAR'
]
SECURITY_MFA_VERIFY_TTL = CONFIG.SECURITY_MFA_VERIFY_TTL
SECURITY_VIEW_AUTH_NEED_MFA = CONFIG.SECURITY_VIEW_AUTH_NEED_MFA
SECURITY_SERVICE_ACCOUNT_REGISTRATION = DYNAMIC.SECURITY_SERVICE_ACCOUNT_REGISTRATION

# Terminal other setting
TERMINAL_PASSWORD_AUTH = DYNAMIC.TERMINAL_PASSWORD_AUTH
TERMINAL_PUBLIC_KEY_AUTH = DYNAMIC.TERMINAL_PUBLIC_KEY_AUTH
TERMINAL_HEARTBEAT_INTERVAL = DYNAMIC.TERMINAL_HEARTBEAT_INTERVAL
TERMINAL_ASSET_LIST_SORT_BY = DYNAMIC.TERMINAL_ASSET_LIST_SORT_BY
TERMINAL_ASSET_LIST_PAGE_SIZE = DYNAMIC.TERMINAL_ASSET_LIST_PAGE_SIZE
TERMINAL_SESSION_KEEP_DURATION = DYNAMIC.TERMINAL_SESSION_KEEP_DURATION
TERMINAL_HOST_KEY = DYNAMIC.TERMINAL_HOST_KEY
TERMINAL_HEADER_TITLE = DYNAMIC.TERMINAL_HEADER_TITLE
TERMINAL_TELNET_REGEX = DYNAMIC.TERMINAL_TELNET_REGEX

# User or user group permission cache time, default 3600 seconds
ASSETS_PERM_CACHE_ENABLE = CONFIG.ASSETS_PERM_CACHE_ENABLE
ASSETS_PERM_CACHE_TIME = CONFIG.ASSETS_PERM_CACHE_TIME

# Asset user auth external backend, default AuthBook backend
BACKEND_ASSET_USER_AUTH_VAULT = False

DEFAULT_ORG_SHOW_ALL_USERS = CONFIG.DEFAULT_ORG_SHOW_ALL_USERS
PERM_SINGLE_ASSET_TO_UNGROUP_NODE = CONFIG.PERM_SINGLE_ASSET_TO_UNGROUP_NODE
WINDOWS_SSH_DEFAULT_SHELL = CONFIG.WINDOWS_SSH_DEFAULT_SHELL
FLOWER_URL = CONFIG.FLOWER_URL

# Enable internal period task
PERIOD_TASK_ENABLED = CONFIG.PERIOD_TASK_ENABLED

# Email custom content
EMAIL_SUBJECT_PREFIX = DYNAMIC.EMAIL_SUBJECT_PREFIX
EMAIL_SUFFIX = DYNAMIC.EMAIL_SUFFIX
EMAIL_CUSTOM_USER_CREATED_SUBJECT = DYNAMIC.EMAIL_CUSTOM_USER_CREATED_SUBJECT
EMAIL_CUSTOM_USER_CREATED_HONORIFIC = DYNAMIC.EMAIL_CUSTOM_USER_CREATED_HONORIFIC
EMAIL_CUSTOM_USER_CREATED_BODY = DYNAMIC.EMAIL_CUSTOM_USER_CREATED_BODY
EMAIL_CUSTOM_USER_CREATED_SIGNATURE = DYNAMIC.EMAIL_CUSTOM_USER_CREATED_SIGNATURE

DISPLAY_PER_PAGE = CONFIG.DISPLAY_PER_PAGE
DEFAULT_EXPIRED_YEARS = 70
USER_GUIDE_URL = DYNAMIC.USER_GUIDE_URL
HTTP_LISTEN_PORT = CONFIG.HTTP_LISTEN_PORT
WS_LISTEN_PORT = CONFIG.WS_LISTEN_PORT
LOGIN_LOG_KEEP_DAYS = DYNAMIC.LOGIN_LOG_KEEP_DAYS
TASK_LOG_KEEP_DAYS = CONFIG.TASK_LOG_KEEP_DAYS
ORG_CHANGE_TO_URL = CONFIG.ORG_CHANGE_TO_URL
