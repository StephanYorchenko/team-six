# from typing import List

import json
from base64 import b64encode

import requests
from fastapi import APIRouter

# from core.payments.domain.models import PaymentInputDTO, PaymentOutputDTO
from settings import *

openapi_routes = APIRouter(prefix='/openapi', tags=['OpenAPI'])


def get_access_token() -> str:
    url = f'{AS_URL}/connect/token'
    payload = f'client_id={CLIENT_ID}&grant_type=client_credentials&scope=accounts'
    auth_token = b64encode(bytes(f'{CLIENT_ID}:{CLIENT_SECRET}', 'utf-8')).decode('ascii')
    headers = {
        'Authorization': f'Basic {auth_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = requests.post(url, headers=headers, data=payload, verify=False).json()
    return resp['access_token']


def make_consent(access_token: str, amount: float) -> dict:
    url = f'{RS_PS_URL}/payment-consents'

    payload = json.dumps({
        "Data": {
            "Initiation": {
                "instructionIdentification": "PISP412",
                "endToEndIdentification": "MERCHANT.256702.IDN.12",
                "InstructedAmount": {
                    "amount": "1000.00",  # TODO: add real amount
                    "currency": "RUB"
                },
                "CreditorAccount": {
                    "schemeName": "RU.CBR.PAN",
                    "identification": "40817",
                    "name": "mvideo"
                },
                "RemittanceInformation": {
                    "unstructured": "Dishwasher machine",
                    "reference": "Internal operation code 5678"
                }
            }
        },
        "Risk": {}
    }, separators=(',', ':'))

    jws = '.'.join([
        'eyJhbGciOiJSUzI1NiIsImtpZCI6IjY2NjVCRDA0QUQ0M0JENzY1RDczNDhCNkM3QTdEODI0MTFBMEQ0RTkiLCJ4NXQiOiJabVc5QksxRHZYWmRjMGkyeDZmWUpCR2cxT2siLCJ0eXAiOiJKV1QifQ',
        b64encode(payload.encode()).decode('utf-8-sig'),
        'JzPOCXZQthjUzburLxbJVSDPIMB_3SSKhk1jbp0koBsRHXA2S0W0EuYFKKZdqPpVFrwmwZQQ2_tXCjZubSvsGbmEAQjWAKLH1Kd7dLTKzJFKHezWcRI4ljxA-Zvzm5qryX_95KMLoIfvlMMEqhLimXV_zHkvbzFaQwpjRqvfp53ePAbDGa5Hl7PQPOXkGvS-EUal6AEGcjtajyb5ItnA9FcYkk61-QoP-E-Hw6dq6j3YJrqFk0Pygi9D3G1Cxmkii9Vpr1JXCH2B6ah5d5M2kd9lE_-V4a8lgZgpyszwC17ZF_Dr-puLyNrHQzmBuGF4_d4Hnk2TdUkhboFLi6T_SQ'
    ])

    headers = {
        'x-idempotency-key': 'ad6d0401-62af-423d-be81-803a0bf940eb',
        'Accept': 'application/json',
        'x-jws-signature': jws,
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    resp = requests.post(url, headers=headers, data=payload, verify=False)
    decoded_data = resp.text.encode().decode('utf-8-sig')
    return json.loads(decoded_data)


def exchange_code(code: str) -> Dict:
    url = f'{AS_URL}/connect/token'

    payload_start = 'client_id=08220583b8e7486e9870f4d74a1edc01&client_secret=FFJmGNsntYQ546crpQ9hWiCEIztSbojs&grant_type=authorization_code&code='
    payload_end = '&redirect_uri=https%3A%2F%2Flocalhost.ru%2Fcb'
    payload = payload_start + code + payload_end

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return response.json()


def make_payment(access_token: str) -> Dict:
    url = url = f'{RS_PS_URL}/payments'

    payload = json.dumps({
        "Data": {
            "consentId": "85aa9fa5-f468-4767-92e7-c636e8b37ddd",
            "Initiation": {
                "instructionIdentification": "PISP412",
                "endToEndIdentification": "MERCHANT.256702.IDN.12",
                "InstructedAmount": {
                    "amount": "1000.00",
                    "currency": "RUB"
                },
                "CreditorAccount": {
                    "schemeName": "RU.CBR.PAN",
                    "identification": "40817",
                    "name": "mvideo"
                },
                "RemittanceInformation": {
                    "unstructured": "Dishwasher machine",
                    "reference": "Internal operation code 5678"
                }
            }
        },
        "Risk": {}
    })

    jws = '.'.join([
        'eyJhbGciOiJSUzI1NiIsImtpZCI6IjY2NjVCRDA0QUQ0M0JENzY1RDczNDhCNkM3QTdEODI0MTFBMEQ0RTkiLCJ4NXQiOiJabVc5QksxRHZYWmRjMGkyeDZmWUpCR2cxT2siLCJ0eXAiOiJKV1QifQ',
        b64encode(payload.encode()).decode('utf-8-sig'),
        'JzPOCXZQthjUzburLxbJVSDPIMB_3SSKhk1jbp0koBsRHXA2S0W0EuYFKKZdqPpVFrwmwZQQ2_tXCjZubSvsGbmEAQjWAKLH1Kd7dLTKzJFKHezWcRI4ljxA-Zvzm5qryX_95KMLoIfvlMMEqhLimXV_zHkvbzFaQwpjRqvfp53ePAbDGa5Hl7PQPOXkGvS-EUal6AEGcjtajyb5ItnA9FcYkk61-QoP-E-Hw6dq6j3YJrqFk0Pygi9D3G1Cxmkii9Vpr1JXCH2B6ah5d5M2kd9lE_-V4a8lgZgpyszwC17ZF_Dr-puLyNrHQzmBuGF4_d4Hnk2TdUkhboFLi6T_SQ'
    ])

    headers = {
        'x-idempotency-key': 'd9e45326-ed69-49ea-8015-e9694afc675b',
        'Accept': 'application/json',
        'x-jws-signature': jws,
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    resp = requests.post(url, headers=headers, data=payload, verify=False)
    decoded_data = resp.text.encode().decode('utf-8-sig')
    return json.loads(decoded_data)


@openapi_routes.get('/get_consent')
async def get_consent(amount: float):
    access_token = get_access_token()
    consent = make_consent(access_token, amount)
    return consent
