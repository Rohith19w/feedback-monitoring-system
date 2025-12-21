import logging
from pathlib import Path
from collections import Counter


class AlertSystem:
    def __init__(self):
        self.path = Path("logs") / "negative_alerts.log"
        logging.basicConfig(
            filename=self.path,
            level=logging.WARNING,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.logger = logging.getLogger("alerts")
        self.count = Counter()

    def process_alerts(self, feedback_list):
        negatives = [f for f in feedback_list if f["sentiment_type"] == "Negative"]
        for item in negatives:
            cid = item["customer_id"]
            self.count[cid] += 1
            msg = f"customer={cid} message={item['message'][:120]}"
            if self.count[cid] >= 2:
                self.logger.critical("URGENT " + msg)
            else:
                self.logger.warning(msg)
        return negatives
