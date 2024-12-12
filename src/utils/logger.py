import json
from datetime import datetime
from config.settings import API_LOG_FILE

class APILogger:
    def __init__(self):
        self.log_file = API_LOG_FILE

    def log_response(self, response_data, text_input, corrected_output):
        """Ghi log API response với format JSONL"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "input": text_input,
            "output": corrected_output,
            "response_id": response_data.id,
            "model": response_data.model,
            "system_fingerprint": response_data.system_fingerprint,
            "usage": {
                "prompt_tokens": response_data.usage.prompt_tokens,
                "completion_tokens": response_data.usage.completion_tokens,
                "total_tokens": response_data.usage.total_tokens
            },
            "finish_reason": response_data.choices[0].finish_reason
        }

        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
        except Exception as e:
            print(f"Lỗi khi ghi API log: {str(e)}")
