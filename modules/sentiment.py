import re


class SentimentAnalyzer:
    def __init__(self):
        self.positive = {
            "excellent": 2,
            "amazing": 2,
            "fantastic": 2,
            "perfect": 2,
            "great": 1.5,
            "good": 1,
            "nice": 1,
            "wonderful": 1.5,
            "happy": 1.5,
            "love": 1.5,
            "awesome": 2,
            "superb": 2,
            "thank": 1,
            "thanks": 1,
        }
        self.negative = {
            "terrible": -2,
            "horrible": -2,
            "awful": -2,
            "worst": -2,
            "bad": -1.5,
            "poor": -1.5,
            "disappointed": -1.8,
            "angry": -2,
            "hate": -2,
            "delay": -1.8,
            "late": -1.5,
            "problem": -1.2,
            "issue": -1,
            "error": -1.5,
            "bug": -1.5,
            "crash": -1.8,
            "fraud": -2,
            "scam": -2,
            "cheat": -2,
        }

    def normalize(self, text):
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def analyze(self, message):
        text = self.normalize(message)
        tokens = text.split()

        pos_score = sum(self.positive.get(w, 0) for w in tokens)
        neg_score = sum(self.negative.get(w, 0) for w in tokens)

        if re.search(r"\b(not|no|never)\s+(good|great|happy|excellent)", text):
            pos_score *= 0.3
        if re.search(r"\b(not|no|never)\s+(bad|terrible|horrible|worst)", text):
            neg_score *= 0.3

        total = pos_score + neg_score
        if total > 0.5:
            return 1, "Positive"
        if total < -0.5:
            return -1, "Negative"
        return 0, "Neutral"
