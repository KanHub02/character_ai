JAZZMIN_SETTINGS = {
    "site_title": "Umut",
    "site_header": "Umut",
    "site_brand": "Umut Admin",
    "site_logo_classes": "img-circle",
    # "site_icon": '/assets/icons/admin_logo.png',
    "welcome_sign": "Добро пожаловать в панель администратора сайта Umut!",
    "copyright": "Geekstudio",
    "search_model": "auth.User",
    "user_avatar": "None",
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    "usermenu_links": [
        {
            "model": "user.User",
        },
    ],
    "show_sidebar": True,
    "navigation_expanded": False,
    "hide_apps": [],
    "hide_models": [],
    "icons": {},
    "order_with_respect_to": [
        # apps
        # models
    ],
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-thumbtack",
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "simplex",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
    "actions_sticky_top": False,
}


SUMMERNOTE_CONFIG = {
    "summernote": {
        "toolbar": [
            ["style", ["style"]],
            ["style", ["ul"]],
            ["style", ["bold"]],
            ["style", ["heading"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ],
    },
}
