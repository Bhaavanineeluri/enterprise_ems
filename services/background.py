from fastapi import BackgroundTasks


# ==========================================
# EMAIL TASK
# ==========================================

def send_email(email: str):

    print(f"Email sent to {email}")


# ==========================================
# SMS TASK
# ==========================================

def send_sms(phone: str):

    print(f"SMS sent to {phone}")


# ==========================================
# START EMAIL TASK
# ==========================================

def email_task(

    background_tasks: BackgroundTasks,

    email: str

):

    background_tasks.add_task(
        send_email,
        email
    )

    return {

        "message": "Email queued successfully"

    }


# ==========================================
# START SMS TASK
# ==========================================

def sms_task(

    background_tasks: BackgroundTasks,

    phone: str

):

    background_tasks.add_task(
        send_sms,
        phone
    )

    return {

        "message": "SMS queued successfully"

    }
# ==========================================
# RETRY TASK
# ==========================================

def retry_task(

    func,

    retries=3

):

    for _ in range(retries):

        try:

            func()

            return True

        except Exception:

            pass

    return False
# ==========================================
# BATCH PROCESSING
# ==========================================

def process_batch(items):

    for item in items:

        print(item)

    return {

        "processed": len(items)

    }
def daily_cleanup():
    
    print("Running daily cleanup...")