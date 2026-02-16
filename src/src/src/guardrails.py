def check_guardrails(user_query):
    blocked_keywords = [
        "account balance",
        "customer data",
        "override policy",
        "investment advice",
        "hack",
        "bypass"
    ]

    for word in blocked_keywords:
        if word in user_query.lower():
            return False

    return True
