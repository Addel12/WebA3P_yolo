import os
from detector import app  # ⬅️ Ini penting!

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
