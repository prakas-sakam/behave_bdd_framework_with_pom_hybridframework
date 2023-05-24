from datetime import datetime


def get_new_email_from_timestamp():
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "bhanu" + timestamp + "@gmail.com"