from pydantic import BaseModel


class Payload(BaseModel):
    receiver: str
    quickpay_form: str
    targets: str
    paymentType: str
    sum: float
    formcomment: str = None
    short_dest: str = None
    label: str = None
    comment: str = None
    successURL: str = None
    need_fio: bool = None
    need_email: bool = None
    need_phone: bool = None
    need_address: bool = None
