# from typing import List

import requests
from fastapi import APIRouter

# from core.payments.application.use_cases.get_payments_by_crm_id import GetAllPayments
# from core.payments.domain.models import PaymentInputDTO, PaymentOutputDTO
from settings import *

# from infrastructure.dependencies.repositories import get_payments_repository
#
authorization_routes = APIRouter(prefix='/auth', tags=['Authorization'])


# @authorization_routes.get('/crm/{crm_id}/get_all', response_model=List[PaymentOutputDTO])
# async def get_all_payments(
#         crm_id: int,
#         payments_repository=Depends(get_payments_repository),
#         user=Depends(get_user_from_token),
# ):
#     use_case = GetAllPayments(payments_repository=payments_repository)
#     return await use_case.execute(input_dto=PaymentInputDTO(crm_id=crm_id))


@authorization_routes.get('/get_consent')
async def auth():
    # payload = f'client_id={CLIENT_ID}&grant_type=client_credentials&scope=accounts&state=e0d8e246-a46f-4352-b581-4f1d0d0df6c4'
    # headers = {
    #     'Authorization': f'Basic {user}',
    #     'Content-Type': 'application/x-www-form-urlencoded'
    # }
    # resp = requests.post(f'{AS_URL}/connect/token', headers=headers, data=payload, verify=False)
    # return resp.json()

    url = f'{AS_URL}/connect/token'
    payload = 'client_id=08220583b8e7486e9870f4d74a1edc01&grant_type=client_credentials&scope=accounts&state=e0d8e246-a46f-4352-b581-4f1d0d0df6c4'
    headers = {
        'Authorization': 'Basic MDgyMjA1ODNiOGU3NDg2ZTk4NzBmNGQ3NGExZWRjMDE6RkZKbUdOc250WVE1NDZjcnBROWhXaUNFSXp0U2JvanM=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)

    print(response.text)
    return response.json()
