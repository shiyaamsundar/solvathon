import schedule

import time

from datetime import datetime


def my_function():


    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{current_time}: Running my_function every minute")


    schedule.every(1).minutes.do(my_function)






if __name__ == "__main__":

    while True:

        print('asda')

        schedule.run_pending()

        time.sleep(1) 