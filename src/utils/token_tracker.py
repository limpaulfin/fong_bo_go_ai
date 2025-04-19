"""
Module theo dõi lượng token sử dụng, hỗ trợ theo dõi theo ngày và tháng.
"""
import json
from datetime import datetime
import os
from config.settings import TOKEN_STATS_FILE

class TokenUsageTracker:
    def __init__(self):
        self.stats_file = TOKEN_STATS_FILE
        self.stats = self._load_stats()

    def _load_stats(self):
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._create_default_stats()
        return self._create_default_stats()

    def _create_default_stats(self):
        return {
            "total_tokens": 0,
            "daily_tokens": {},
            "monthly_tokens": {}
        }

    def _save_stats(self):
        # Đảm bảo thư mục tồn tại
        os.makedirs(os.path.dirname(self.stats_file), exist_ok=True)

        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2, ensure_ascii=False)

    def update_usage(self, tokens):
        today = datetime.now().strftime("%Y-%m-%d")
        month = datetime.now().strftime("%Y-%m")

        # Cập nhật tổng token
        self.stats["total_tokens"] += tokens

        # Cập nhật token theo ngày
        if today not in self.stats["daily_tokens"]:
            self.stats["daily_tokens"][today] = 0
        self.stats["daily_tokens"][today] += tokens

        # Cập nhật token theo tháng
        if month not in self.stats["monthly_tokens"]:
            self.stats["monthly_tokens"][month] = 0
        self.stats["monthly_tokens"][month] += tokens

        self._save_stats()

    def get_stats(self):
        today = datetime.now().strftime("%Y-%m-%d")
        month = datetime.now().strftime("%Y-%m")
        return {
            "total_tokens": self.stats["total_tokens"],
            "today_tokens": self.stats["daily_tokens"].get(today, 0),
            "month_tokens": self.stats["monthly_tokens"].get(month, 0)
        }
