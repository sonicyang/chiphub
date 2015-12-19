# coding= utf-8
from keys import keys
import requests
from login.auth import get_user_profile

def get_subject_and_text(filename, subject_format, text_format):
    #XXX: need to read raw_subject and raw_text from file
    raw_subject = u"訂單已收到"
    raw_text = u"%(real_name)s 您好：\n訂單已收到，請匯款至XXX，並於匯款後至XXX填寫匯款資料及匯款日期。"

    subject = raw_subject % subject_format
    text = raw_text % text_format

    return subject, text

def send_order_received(request):
    user = get_user_profile(request)
    subject, text = get_subject_and_text("test", {}, {"real_name": user.real_name})
    return requests.post(
        keys.MAILGUN_API_URL,
        auth=("api", keys.MAILGUN_API_KEY),
        data={"from": "noreply@chiphub.c4labs.xyz",
              "to": [user.email],
              "subject": subject,
              "text": text}
    )
