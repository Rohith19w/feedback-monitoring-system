import sys
from pathlib import Path
from collections import Counter

sys.path.append(str(Path(__file__).parent / "modules"))

from reader import FeedbackReader
from sentiment import SentimentAnalyzer
from categorizer import FeedbackCategorizer
from alerts import AlertSystem
from reporter import ReportGenerator


def ensure_structure():
    for name in ["data", "logs", "output", "modules"]:
        Path(name).mkdir(exist_ok=True)
    (Path("logs") / "negative_alerts.log").touch()


def build_stats(feedback):
    sentiment_counts = Counter(f["sentiment_type"] for f in feedback)
    category_counts = Counter(f["category"] for f in feedback)
    return {
        "total": len(feedback),
        "sentiment": sentiment_counts,
        "categories": category_counts,
    }


def show_dashboard(stats, alerts_path: Path):
    total = stats["total"]
    sentiment = stats["sentiment"]
    categories = stats["categories"]

    print("\n================ CUSTOMER FEEDBACK DASHBOARD ================")
    print(f"Total feedback: {total}")
    if total > 0:
        print(
            f"Positive: {sentiment.get('Positive',0):3d} "
            f"({sentiment.get('Positive',0)/total*100:5.1f}%)"
        )
        print(
            f"Neutral:  {sentiment.get('Neutral',0):3d} "
            f"({sentiment.get('Neutral',0)/total*100:5.1f}%)"
        )
        print(
            f"Negative: {sentiment.get('Negative',0):3d} "
            f"({sentiment.get('Negative',0)/total*100:5.1f}%)"
        )

    print("\nCategory distribution:")
    for category, count in categories.most_common():
        pct = count / total * 100 if total else 0
        print(f"{category:25s} {count:4d} ({pct:5.1f}%)")

    if alerts_path.exists():
        lines = [
            ln for ln in alerts_path.read_text(encoding="utf-8").splitlines()
            if ln.strip()
        ]
        print(f"\nAlerts triggered today: {len(lines)}")
    else:
        print("\nAlerts triggered today: 0")
    print("=============================================================\n")


def main():
    ensure_structure()

    reader = FeedbackReader()
    sentiment = SentimentAnalyzer()
    categorizer = FeedbackCategorizer()
    alerts = AlertSystem()
    reporter = ReportGenerator()

    feedback = reader.read_all_sources()
    if not feedback:
        print("No feedback found in data/ directory.")
        return

    for item in feedback:
        score, label = sentiment.analyze(item["message"])
        item["sentiment_score"] = score
        item["sentiment_type"] = label

    for item in feedback:
        item["category"] = categorizer.categorize(item["message"])

    alerts.process_alerts(feedback)

    stats = build_stats(feedback)
    show_dashboard(stats, Path("logs/negative_alerts.log"))
    reporter.generate_report(feedback, stats["sentiment"], stats["categories"])


if __name__ == "__main__":
    main()
