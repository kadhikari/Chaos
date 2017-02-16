import os

#URI for postgresql
# postgresql://<user>:<password>@<host>:<port>/<dbname>
#http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#psycopg2
DATABASE_HOST = str(os.getenv('DATABASE_HOST', 'localhost'))
SQLALCHEMY_DATABASE_URI = 'postgresql://navitia:navitia@' + DATABASE_HOST + '/chaos_testing'

NAVITIA_URL = 'http://navitia2-ws.ctp.customer.canaltp.fr/'


DEBUG = True

RABBITMQ_HOST = str(os.getenv('RABBITMQ_HOST', 'localhost'))
RABBITMQ_CONNECTION_STRING = 'pyamqp://guest:guest@' + RABBITMQ_HOST + ':5672//?heartbeat=60'


#amqp exhange used for sending disruptions
EXCHANGE='navitia'

CONTRIBUTOR='shortterm.tn'
#
ENABLE_RABBITMQ=False

CACHE_CONFIGURATION = {
    'CACHE_TYPE': 'null'
}

#Log Level available
# - DEBUG
# - INFO
# - WARN
# - ERROR

# logger configuration
LOGGER = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters':{
        'default': {
            'format': '[%(asctime)s] [%(levelname)5s] [%(process)5s] [%(name)25s] %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
        },
        'celery':{
            'level': 'INFO',
        },
        'sqlalchemy.engine': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'sqlalchemy.pool': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'sqlalchemy.dialects.postgresql': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
        'alembic.migration': {
            'handlers': ['default'],
            'level': 'WARN',
            'propagate': False
        },
    }
}
