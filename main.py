from send_email import GmailAdapter
from messages import Message_from_library
from data_base import create_connection, get_person
from os import getenv
from dotenv import load_dotenv
import logging
import datetime


load_dotenv()
logging.basicConfig(level=logging.DEBUG)

today_date = datetime.datetime.now()

if __name__ == '__main__':
    cursor = create_connection(getenv('DB_NAME'))
    info = get_person(cursor, today_date)
    adapter = GmailAdapter(getenv('SENDER_EMAIL'), getenv('PASSWORD'))
    adapter.login()
    logging.info('Poprawne logowanie')
    message = Message_from_library()

    try:
        for n in info:
            client_name, mail, book_title, return_at = n.values()
            adapter.sendmail(mail,
                             'Przypomnienie o zwrocie książki',
                             body_message=message.render(
                                 client_name=client_name, book_title=book_title, return_at=return_at)
                             )
            logging.info(f'Wysłano wiadomość do {mail}.')
    except Exception as error:
        logging.error('Błąd podczas próby wysłania wiadomości!')
        raise error
