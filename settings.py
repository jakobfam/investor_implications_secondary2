from os import environ

SESSION_CONFIGS = [
    dict(
        name='market_pilot',
        display_name='Market Implications – Treatment 1 (Equ. Pricing, Risk and ESG Outcome)',
        app_sequence=['market_pilot'],
        num_demo_participants=10,
        control_pct=15,  # percent allocated to control (rest → treatment1)
        prolific=True,
        link_completed='https://app.prolific.com/submissions/complete?cc=C13CNJTF',
        link_no_consent='https://app.prolific.com/submissions/complete?cc=C1O46EDD',
        link_no_attention='https://app.prolific.com/submissions/complete?cc=CAFF9WJT',
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
        welcome_page='_welcome_pages/consent.html',
    ),
    dict(
        name='market_pilot2',
        display_name='Market Pilot Study 2',
        welcome_page='_welcome_pages/consent.html',
    ),
]

ADMIN_USERNAME = environ.get('OTREE_ADMIN_USERNAME', 'qQOVXHJ5cy1GBns')
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """Market Pilot Experiment – Primary vs Secondary Markets"""

SECRET_KEY = '{{ secret_key }}'
