AUTH_TYPE = 1
AUTH_USER_REGISTRATION = True


HTML_SANITIZATION = False
TALISMAN_ENABLED = False
TALISMAN_CONFIG = {
    "content_security_policy": None,
    "content_security_policy_nonce_in": ["script-src"],
    "force_https": False,
    "session_cookie_secure": False
}
D3_FORMAT = {
    "decimal": ",",
    "thousands": " ",
    "grouping": [3],
    "currency": ["", " руб."]
}
ENABLE_CORS = True
CORS_OPTIONS = {
 'supports_credentials': True,
 'allow_headers': ['*'],
 'resources':['*'],
 'origins': ['*']
}

ENABLE_JAVASCRIPT_CONTROLS = True
WTF_CSRF_ENABLED = False
PUBLIC_ROLE_LIKE = "Public"
SUPERSET_DASHBOARD_POSITION_DATA_LIMIT = 655350
SUPERSET_WEBSERVER_TIMEOUT = 300

BABEL_DEFAULT_LOCALE = "ru"

LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "ru": {"flag": "ru", "name": "Russian"}
}

CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 3600,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": "redis",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_URL": "redis://redis:6379/0"
}

DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 3600,
    "CACHE_KEY_PREFIX": "superset_results",
    "CACHE_REDIS_URL": "redis://redis:6379/1"
}

FILTER_STATE_CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 8*60*60, 
    "CACHE_KEY_PREFIX": "filter_",
    "CACHE_REDIS_URL": "redis://redis:6379/2"
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 8*60*60, 
    "CACHE_KEY_PREFIX": "chart_",
    "CACHE_REDIS_URL": "redis://redis:6379/3"
}

THUMBNAIL_SELENIUM_USER = "admin"
THUMBNAIL_CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 24 * 60 * 60 * 30,
    'CACHE_KEY_PREFIX': 'thumbnail_',
    'CACHE_NO_NULL_WARNING': True,
    "CACHE_REDIS_URL": "redis://redis:6379/4"
}

MAPBOX_API_KEY = "pk.eyJ1Ijoicm9tYW5rZXZpY2hzdiIsImEiOiJjbDJ4ZHQ0NDUwbHozM2JxbDc5ZDRqeTN4In0.9ER9xonCVTw-v1UOfIezow"

FEATURE_FLAGS = {
        "THUMBNAILS": True,
        "DASHBOARD_RBAC": True,
        "ENABLE_TEMPLATE_PROCESSING": True,
        "DASHBOARD_NATIVE_FILTERS_SET": True,
        "DASHBOARD_FILTERS_EXPERIMENTAL": True,
        "EMBEDDED_SUPERSET": True,
        "DASHBOARD_CACHE": True
}
SECRET_KEY = 'asdfasdfasdfadsfadsfadsfasd'

EXCEL_EXPORT = {
    'float_format': "{:,}"
}

