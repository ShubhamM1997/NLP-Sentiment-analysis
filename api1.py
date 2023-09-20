from fastapi import FastAPI
from pydantic import BaseModel
from email.utils import parsedate_to_datetime
import os
import email
import pandas as pd
from email import policy
from email.parser import BytesParser
import re

app = FastAPI()

class EmailInfo(BaseModel):
    eml_path: str

def extract_email_info(eml_path):
    with open(eml_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    subject = msg['subject']
    from_address = msg['from']
    to_address = msg['to']
    timestamp = parsedate_to_datetime(msg['Date']).date()

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)
                break
    else:
        body = msg.get_payload(decode=True)

    if type(body) is bytes:
        body = body.decode()

    split_warning = "CAUTION: This email comes from outside of Utthunga."
    if split_warning in body:
        body = body.split(split_warning, 1)[1]

    signature_indicators = ["Regards", "Thank you"]
    for indicator in signature_indicators:
        if indicator in body:
            body = body.split(indicator, 1)[0]
            break

    person_from_match = re.search(r'(.*) <.*@.*\..*>', from_address)
    if person_from_match:
        person_from = person_from_match.group(1)
        organization_match = re.search(r'@(.*)\.', from_address)
        if organization_match:
            organization = organization_match.group(1)
        else:
            organization = ""
    else:
        person_from = from_address
        organization = ""

    return subject, person_from, organization, to_address, timestamp, body.strip()


@app.post("/extract_email")
def extract_email(email_info: EmailInfo):
    subject, person_from, organization, to_address, timestamp, body = extract_email_info(email_info.eml_path)
    return {
        "subject": subject,
        "person_from": person_from,
        "organization": organization,
        "to_address": to_address,
        "timestamp": timestamp,
        "body": body.strip()
    }
