from os import environ

SESSION_CONFIGS = [
    dict(
        name='market_pilot',
        display_name='Market Pilot – Treatment 1 (Abstract Framing & Control)',
        app_sequence=['market_pilot'],
        num_demo_participants=10,
        control_pct=15,  # percent allocated to control (rest → treatment1)
        prolific=True,
        link_completed='https://app.prolific.com/submissions/complete?cc=CF11XHAO',
        link_no_consent='https://app.prolific.com/submissions/complete?cc=CVGDWZOQ',
        link_no_attention='https://app.prolific.com/submissions/complete?cc=C4B65D7J',
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc="",
)

PARTICIPANT_FIELDS = ['treatment']
SESSION_FIELDS = []

LANGUAGE_CODE = 'de'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    dict(
        name='market_pilot',
        display_name='Market Pilot Study',
    ),
    dict(
        name='market_pilot2',
        display_name='Market Pilot Study 2',
    ),
]

ADMIN_USERNAME = environ.get('OTREE_ADMIN_USERNAME', 'qQOVXHJ5cy1GBns')
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """Market Pilot Experiment – Primary vs Secondary Markets"""

SECRET_KEY = '{{ secret_key }}'
