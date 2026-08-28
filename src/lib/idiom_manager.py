# src/lib/idiom_manager.py
def load_idiom_list()  -> list:
    """从sdata/idiom_list.txt中加载成语列表"""
    with open('data/idiom_list.txt', 'r', encoding='utf-8') as f:
        idiom_list = f.read().splitlines()

    return idiom_list
