from pathlib import Path
from collections import defaultdict
from datetime import datetime


class ReportGenerator:
    def __init__(self):
        self.path = Path("output") / "daily_feedback_report.txt"
        self.path.parent.mkdir(exist_ok=True)

    def build_suggestions(self, category_counts, total):
        if total == 0:
            return ["Monitor feedback volume and verify data pipeline."]
        suggestions = []
        if category_counts.get("Delivery Delay", 0) / total > 0.3:
            suggestions.append("Investigate delivery delays and review logistics partners.")
        if category_counts.get("Billing Problem", 0) / total > 0.2:
            suggestions.append("Review billing, payment, and refund workflows.")
        if category_counts.get("App/Website Issue", 0) / total > 0.15:
            suggestions.append("Prioritize resolving app/website stability and performance issues.")
        if not suggestions:
            suggestions.append("Maintain current operations and continue monitoring feedback trends.")
        return suggestions

    def generate_report(self, feedback_list, sentiment_counts, category_counts):
        total = len(feedback_list)
        lines = []
        lines.append("FLIPKART DAILY CUSTOMER FEEDBACK REPORT")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Total feedback: {total}")
        lines.append("=" * 60)
        if total > 0:
            lines.append(
                f"Positive: {sentiment_counts.get('Positive',0):3d} "
                f"({sentiment_counts.get('Positive',0)/total*100:5.1f}%)"
            )
            lines.append(
                f"Neutral:  {sentiment_counts.get('Neutral',0):3d} "
                f"({sentiment_counts.get('Neutral',0)/total*100:5.1f}%)"
            )
            lines.append(
                f"Negative: {sentiment_counts.get('Negative',0):3d} "
                f"({sentiment_counts.get('Negative',0)/total*100:5.1f}%)"
            )

        lines.append("=" * 60)
        lines.append("Top categories:")
        for cat, count in category_counts.most_common():
            pct = count / total * 100 if total else 0
            lines.append(f"{cat:25s} {count:4d} ({pct:5.1f}%)")

        samples = defaultdict(list)
        for item in feedback_list:
            if len(samples[item["category"]]) < 3:
                samples[item["category"]].append(item["message"][:120])

        lines.append("=" * 60)
        lines.append("Sample comments:")
        for cat, msgs in samples.items():
            lines.append(f"[{cat}]")
            for msg in msgs:
                lines.append(f"- {msg}")
            lines.append("")

        lines.append("=" * 60)
        lines.append("Suggestions:")
        for suggestion in self.build_suggestions(category_counts, total):
            lines.append(f"- {suggestion}")

        self.path.write_text("\n".join(lines), encoding="utf-8")
