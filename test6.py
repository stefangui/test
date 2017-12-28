import datetime
import time

if __name__ == '__main__':
    print(time.localtime())
    print(datetime.date.today().strftime('%d/%m/%Y'))

    siDate = datetime.datetime(1941, 1, 5, 11, 22, 33)
    print(siDate.strftime('%Y-%m-%d  %H-%M-%S'))

    siDate += datetime.timedelta(hours=11)
    print(siDate.strftime('%Y-%m-%d  %H-%M-%S'))

exit()
