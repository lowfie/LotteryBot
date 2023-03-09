import httpx
from datetime import datetime
from typing import Optional

from libs.yoomoney.schemas.operations import Operation, Payload


class History:
    def __init__(self,
                 base_url: str = None,
                 token: str = None,
                 method: str = None,
                 operation_type: str = None,
                 label: str = None,
                 from_date: Optional[datetime] = None,
                 till_date: Optional[datetime] = None,
                 start_record: str = None,
                 records: int = None,
                 details: bool = None
                 ):
        self.__private_method = method
        self.__private_base_url = base_url
        self.__private_token = token
        self.type = operation_type
        self.label = label
        if from_date is not None:
            from_date = "{Y}-{m}-{d}T{H}:{M}:{S}".format(
                Y=str(from_date.year),
                m=str(from_date.month),
                d=str(from_date.day),
                H=str(from_date.hour),
                M=str(from_date.minute),
                S=str(from_date.second)
            )
        if till_date is not None:
            till_date = "{Y}-{m}-{d}T{H}:{M}:{S}".format(
                Y=str(till_date.year),
                m=str(till_date.month),
                d=str(till_date.day),
                H=str(till_date.hour),
                M=str(till_date.minute),
                S=str(till_date.second)
            )
        self.from_date = from_date
        self.till_date = till_date
        self.start_record = start_record
        self.records = records
        self.details = details

        data = self._request()
        if "error" in data:
            raise ValueError(data)
        elif "" in data:
            raise ValueError("Invalid token")
        self.next_record = data["next_record"] if "next_record" in data else None

        self.operations = list()
        for operation_data in data["operations"]:
            operation = Operation(**operation_data)
            self.operations.append(operation)

    def _request(self):
        access_token = str(self.__private_token)
        url = self.__private_base_url + self.__private_method

        headers = {
            "Authorization": "Bearer " + str(access_token),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = Payload(
            type=self.type,
            label=self.label,
            from_date=self.from_date,
            till=self.till_date,
            start_record=self.start_record,
            records=self.records,
            details=self.details
        )

        response = httpx.post(url, headers=headers, data=payload.dict(exclude_none=True))
        return response.json()
