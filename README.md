# feedback-monitoring-system
Real-Time Customer Feedback Analyzer & Sentiment Monitoring

Python-based rule‑based sentiment analysis and service issue monitoring system, built as Task‑3 for the Python Internship at Flipkart Pvt Ltd. The tool reads customer feedback from multiple sources, scores sentiment, categorizes issues, raises alerts for negative feedback, and generates a daily summary report.

# demo video link : https://drive.google.com/file/d/1Zfnik_dwa7BJfpbnkKcmFsB94TCc-aE4/view?usp=sharing

Main features:
- Reads feedback from feedback_today.txt, chat_logs.txt, email_feedback.csv
- Rule-based sentiment analysis: +1 / 0 / -1, Positive / Neutral / Negative
- Categorizes feedback into: Service Issue, Delivery Delay, Billing Problem, App/Website Issue, General Appreciation
- Logs negative feedback and marks repeated complaints from the same customer as URGENT
- Generates a daily report in output/daily_feedback_report.txt
- Prints a console dashboard with counts and distributions

Basic usage:
1. Create a folder, save the Python code as main.py.
2. Create a subfolder named data and place:
   - data/feedback_today.txt
   - data/chat_logs.txt
   - data/email_feedback.csv
3. Run: python main.py
4. Check:
   - logs/negative_alerts.log
   - output/daily_feedback_report.txt
   - the console output for the dashboard.

5. Check outputs:

- Console: simple dashboard with sentiment and category stats.
- `logs/negative_alerts.log`: list of negative feedback and urgent alerts.
- `output/daily_feedback_report.txt`: daily report with summary and suggestions.
---
# Make sure inputs exist:

-data/feedback_today.txt
-data/chat_logs.txt
-data/email_feedback.csv

---
# structure:
feedback_monitoring_system/
│


├── main.py


│


├── data/


│ ├── feedback_today.txt


│ ├── chat_logs.txt


│ └── email_feedback.csv


│


├── logs/


│ └── negative_alerts.log # auto‑created


│


├── output/


│ └── daily_feedback_report.txt # auto‑created


│


└── README.md


---

Customization Ideas

- Extend the positive and negative keyword dictionaries to better fit e‑commerce and Flipkart‑style language.
- Add more detailed categories (for example: Product Quality Issue, Packaging Issue).
- Add date filters to process only today’s feedback.
- Export the report as CSV or integrate it into a simple web dashboard using Flask or Streamlit.
- Schedule the script using cron (Linux) or Task Scheduler (Windows) for automatic daily runs.


