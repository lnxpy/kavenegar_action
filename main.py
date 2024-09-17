from kavenegar import KavenegarAPI
from pyaction import PyAction

workflow = PyAction()


@workflow.action()
def action(api_key: str, receptor: str, message: str) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    api = KavenegarAPI(api_key)
    params = {
        "receptor": receptor,
        "message": message,
    }

    api.sms_send(params)
