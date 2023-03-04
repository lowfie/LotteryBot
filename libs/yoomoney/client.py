from datetime import datetime
from libs.yoomoney.operation.history import History


class Client:
    def __init__(self, token: str = None, base_url: str = None):
        if base_url is None:
            self.base_url = "https://yoomoney.ru/api/"

        if token is not None:
            self.token = token

    def operation_history(
            self,
            operation_type: str = None,
            label: str = None,
            from_date: datetime = None,
            till_date: datetime = None,
            start_record: str = None,
            records: int = None,
            details: bool = None,
    ):
        method = "operation-history"
        return History(
            base_url=self.base_url,
            token=self.token,
            method=method,
            operation_type=operation_type,
            label=label,
            from_date=from_date,
            till_date=till_date,
            start_record=start_record,
            records=records,
            details=details,
        )
