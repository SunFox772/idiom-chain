# 成语接龙

一个简单的成语接龙游戏，使用 Python 编写。

## 功能

- 随机选择起始成语
- 用户输入成语进行接龙
- 验证成语是否存在于词库中
- 检查成语是否重复使用
- 检查首尾字是否匹配
- 输入 `/quit` 退出游戏

## 运行环境

- Python 3.6 及以上
- 无需安装第三方库

## 文件结构

```
src/
├── main.py              # 程序入口
└── lib/
    └── idiom_manager.py # 成语加载模块
data/
└── idiom_list.txt       # 成语词库（每行一个成语）
```

## 使用方法

1. 确保 `data/idiom_list.txt` 文件存在且包含成语列表（每行一个）

2. 运行程序：
   ```bash
   python src/main.py
   ```

3. 输入成语进行接龙，程序会提示当前需要接龙的尾字

4. 输入 `/quit` 退出游戏

## 示例

```
欢迎来到成语接龙！
一帆风顺
请接龙（顺）：顺手牵羊
接龙成功
请接龙（羊）：洋洋得意
接龙成功
请接龙（意）：意气风发
接龙成功
请接龙（发）：/quit
已退出
```

## 词库

成语列表存储在 `data/idiom_list.txt` 中，每行一个成语，共收录约 30000+ 个成语。

## 未来计划

详见 [TODO.md](./TODO.md)

## 作者

SunFox772

## 许可证

MIT License

## 鸣谢

详见 [CONTRIBUTORS.md](./CONTRIBUTORS.md)


## 数据来源
成语数据来自 [crazywhalecc/idiom-database](https://github.com/crazywhalecc/idiom-database)

- 数据文件：`data/idiom_list.txt`
- 来源协议：MIT License
- 原始仓库：[crazywhalecc/idiom-database](https://github.com/crazywhalecc/idiom-database)