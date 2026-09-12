# src/core/running.py
import random
from lib.idiom_manager import load_idiom_list


class IdiomGame:
    """成语接龙游戏核心类"""

    def __init__(self):
        self.idiom_list = load_idiom_list()
        self.reset()

    def reset(self):
        """重置游戏，随机选一个新成语开始"""
        self.last_idiom = random.choice(self.idiom_list)
        self.used_idioms = [self.last_idiom]

    def get_current_idiom(self) -> str:
        """获取当前成语"""
        return self.last_idiom

    def get_last_char(self) -> str:
        """获取当前尾字"""
        return self.last_idiom[-1]

    def get_used_count(self) -> int:
        """获取已接龙数量"""
        return len(self.used_idioms) - 1

    def submit(self, user_input: str) -> tuple[bool, str]:
        """
        提交用户答案
        返回: (是否成功, 消息)
        """
        if not user_input:
            return False, "请输入成语！"

        if user_input not in self.idiom_list:
            return False, "❌ 成语不存在，请重新输入"

        if user_input in self.used_idioms:
            return False, "⚠️ 这个成语已经用过了"

        if user_input[0] != self.get_last_char():
            return False, f'❌ 需要以 "{self.get_last_char()}" 开头'

        self.last_idiom = user_input
        self.used_idioms.append(user_input)
        return True, "✅ 接龙成功！"
