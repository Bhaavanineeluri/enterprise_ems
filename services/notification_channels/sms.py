def send_sms(
    phone: str,
    message: str
):

    # Later integrate Twilio / AWS SNS

    print(
        f"SMS sent to {phone}"
    )

    print(message)

    return True