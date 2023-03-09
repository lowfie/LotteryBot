import httpx
from libs.yoomoney.schemas.quickpay import Payload


class Quickpay:
    def __init__(self,
                 receiver: str,
                 quickpay_form : str,
                 targets: str,
                 paymentType: str,
                 sum: float,
                 formcomment: str = None,
                 short_dest: str = None,
                 label: str = None,
                 comment: str = None,
                 successURL: str = None,
                 need_fio: bool = None,
                 need_email: bool = None,
                 need_phone: bool = None,
                 need_address: bool = None,
                 ):
        self.receiver = receiver
        self.quickpay_form = quickpay_form
        self.targets = targets
        self.paymentType = paymentType
        self.sum = sum
        self.formcomment = formcomment
        self.short_dest = short_dest
        self.label = label
        self.comment = comment
        self.successURL = successURL
        self.need_fio = need_fio
        self.need_email = need_email
        self.need_phone = need_phone
        self.need_address = need_address

        self.response = self._request()

    def _request(self):
        self.base_url = "https://yoomoney.ru/quickpay/confirm.xml?"
        payload = Payload(
            receiver=self.receiver,
            quickpay_form=self.quickpay_form,
            targets=self.targets,
            paymentType=self.paymentType,
            sum=self.sum,
            formcomment=self.formcomment,
            short_dest=self.short_dest,
            label=self.label,
            comment=self.comment,
            successURL=self.successURL,
            need_fio=self.need_fio,
            need_email=self.need_email,
            need_phone=self.need_phone,
            need_address=self.need_address
        )
        for key, value in payload.dict(exclude_none=True).copy().items():
            self.base_url += key.replace("_", "-") + "=" + str(value)
            self.base_url += "&"
        self.base_url = self.base_url[:-1].replace(" ", "%20")

        response = httpx.post(self.base_url)
        self.redirected_url = response.url
        return response
