def send_email(
    recipient: str,
    subject: str,
    message: str
):

    # Later integrate SMTP / SendGrid / AWS SES

    print(
        f"EMAIL sent to {recipient}"
    )

    print(message)

    return True