# 敏感关键词扫描工具（正则表达式匹配）
import re

def scan_sensitive_data(text):
    patterns = {
        '身份证号': r'\b\d{17}[\dXx]\b',
        '手机号': r'\b1[3-9]\d{9}\b',
        '邮箱': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    }
    for key, pattern in patterns.items():
        if re.search(pattern, text):
            print(f"发现敏感信息 - {key}")

# 示例：扫描一段文本
text_sample = "用户手机号：13812345678，邮箱：user@example.com"
scan_sensitive_data(text_sample)
