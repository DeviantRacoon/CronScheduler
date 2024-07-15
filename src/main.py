# -*- coding: utf-8 -*-

from datetime import date
from modules.logger import LoggerManager, logger_decorator
from modules.read_json import read_json_file
from modules.fetch_url import Fetcher
from modules.rules import execute_callbacks
from utils.dotenv import load_dotenv


def _get_fetcher():
    return Fetcher()


def _get_logger():
    return LoggerManager(logger_name='cron_presico').get_logger()


def execute_endpoints(endpoints):
    logger = _get_logger()
    fetcher = _get_fetcher()
    failures = []

    for endpoint in endpoints['endpoints']:
        domains = endpoint['domain']
        url = endpoint['url']
        
        results = fetcher.fetch_all(domains, url)
        failures.extend([result for result in results if not result['success']])

    for failure in failures:
        logger.error(failure)
        
    if len(failures) == 0:
        logger.info('Todas las consultas en {} han sido exitosas'.format(endpoints['name']))
        
    return {'failures': len(failures), 'successes': len(results) - len(failures), 'total': len(results)}


def send_sms(data):
    dotenv = load_dotenv()
    phones = dotenv['PHONES_NUMBERS'].split(',')
    message_information = """
    --- INFORMACION DE CIERRES ---

    Exitosos: {}
    Fallidos: {}
    Total: {}

    Fecha: {}""".format(data['successes'], data['failures'], data['total'], date.today())

    fetcher = _get_fetcher()
    for phone_number in phones:
        # print({'message': message_information, 'number': phone_number})
        fetcher.post_data(dotenv['SERVICE_SMS'], {'message': message_information, 'number': phone_number})


@logger_decorator
def main():
    services = read_json_file('endpoints.json')

    for item in services:
        days = item.get('days')
        callbacks = [execute_endpoints]
        if item.get('name') == 'CIERRE CAJAS':
            callbacks.append(send_sms)

        execute_callbacks(callbacks, days, item)


if __name__ == "__main__":
    main()

