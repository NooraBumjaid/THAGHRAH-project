#!/usr/bin/env python3
from thaghrah import create_app
from thaghrah.db import init_db

init_db()
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
