from argparse import ArgumentParser
from tokenize import String
from client import Client
from datetime import datetime, timedelta
import threading, time

def keyRotation():
    last_key_update = datetime.now()
    while True:
        update_time = datetime.now() - last_key_update
        if update_time > timedelta(seconds=args.key_timeout):
            last_key_update =  datetime.now()
            print("********************************* Regenerating keys *********************************")
        else:
            time.sleep(2)    

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-em", "--encrypt_master_key", dest="encrypt_master_key", help="Encrypt all files using just master key (MK).", required=False)
    parser.add_argument("-ed", "--encrypt_data_key", dest="encrypt_data_key", help="Encrypt all files using a data encryption key (DEK) protected with master key (MK) and a password.", required=False)
    parser.add_argument("-d", "--decrypt", dest="decrypt", help="Decrypt a file", required=False)
    parser.add_argument("-kt", "--key_timeout", dest="key_timeout", type=int, default=0, help="The time after which we need to regenerate the encryption keys in seconds")
    args = vars(parser.parse_args())
    print(args)
    client = Client(args)
    # thread = threading.Thread(target=keyRotation)
    # thread.daemon = True
    # thread.start()