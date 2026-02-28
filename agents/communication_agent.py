import re

def extract_details(query):
    # Extract dates like "10 March to 15 March"
    date_pattern = r"(\d{1,2}\s+\w+\s*(?:to|-)\s*\d{1,2}\s+\w+)"
    dates = re.search(date_pattern, query)

    if dates:
        leave_dates = dates.group(1)
    else:
        leave_dates = "the required dates"

    # Try to extract reason after 'due to'
    reason_pattern = r"due to (.+)"
    reason_match = re.search(reason_pattern, query.lower())

    if reason_match:
        reason = reason_match.group(1)
    else:
        reason = "personal reasons"

    return leave_dates, reason


def draft_email(name, department, query):
    dates, reason = extract_details(query)

    return f"""
Subject: Application for Leave ({dates})

Respected Sir/Madam,

I am writing to inform you that I will be unable to attend classes due to {reason}.

I kindly request you to grant me leave for {dates}. I will make sure to cover the missed academic work.

Thanking you.

Yours sincerely,
{name}
Department: {department}
"""