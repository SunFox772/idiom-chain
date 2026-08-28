# src/core/running.py
import random

from lib.idiom_manager import load_idiom_list


def run():
    """程序运行主函数"""
    idiom_list = load_idiom_list()

    last_idiom = random.choice(idiom_list)
    used_idiom = [last_idiom]
    print('欢迎来到成语接龙！')
    print(last_idiom)


    while True:
        next_idiom = input(f'请接龙（{last_idiom[-1]}）：').strip()

        if next_idiom == "/quit":
            print("已退出")
            break

        elif next_idiom == "":
            print("输入为空，请重新输入")
            continue

        elif next_idiom not in idiom_list:
            print('成语不存在，请重新输入')
            continue

        elif next_idiom[0] == last_idiom[-1] and next_idiom not in used_idiom:
            print('接龙成功')
            last_idiom = next_idiom
            used_idiom.append(next_idiom)

        else:
            print('接龙失败')
