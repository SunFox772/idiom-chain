# run.py
import sys
from pathlib import Path

# 把 src/ 加入 Python 路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

from web.app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
