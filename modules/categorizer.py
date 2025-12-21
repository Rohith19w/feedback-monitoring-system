import re


class FeedbackCategorizer:
    def __init__(self):
        self.rules = {
            "Service Issue": [
                r"(customer care|support|help).*(no|not.*help|bad)",
                r"call.*not.*connect",
                r"chat.*not.*reply",
                r"return.*(not.*accept|problem)",
            ],
            "Delivery Delay": [
                r"deliver(ed|y).*(late|delay|not received)",
                r"ship.*late",
                r"not delivered",
                r"courier.*problem",
                r"logistics.*issue",
            ],
            "Billing Problem": [
                r"bill.*(wrong|extra|double)",
                r"charge.*(wrong|extra|double)",
                r"payment.*(failed|issue)",
                r"refund.*(not|delay|pending)",
                r"money.*deduct",
            ],
            "App/Website Issue": [
                r"(app|website|site|portal).*(bug|crash|slow|not.*working)",
                r"login.*(fail|error)",
                r"order.*not.*show",
                r"cart.*empty",
                r"page.*not.*load",
            ],
            "General Appreciation": [
                r"(fast|quick).*(delivery|service)",
                r"on time",
                r"easy.*order",
                r"smooth.*experience",
                r"thank.*flipkart",
            ],
        }

    def categorize(self, message):
        text = message.lower()
        for label, patterns in self.rules.items():
            for pattern in patterns:
                if re.search(pattern, text):
                    return label
        return "Uncategorized"
