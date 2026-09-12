# src/lib/idiom_manager.py
from pathlib import Path


def load_idiom_list() -> list:
    """从 data/idiom_list.txt 中加载成语列表"""
    file_path = Path(__file__).parent.parent.parent / "data" / "idiom_list.txt"
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
