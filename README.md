FeeTrack Academy

Android school fee management application developed by Joseph Mbui.

Features

- Student registration
- Fee payment recording
- Balance calculation
- PDF statement generation
- Secure login screen (hashed password)
- Dashboard totals
- SQLite database support
- Student details screen
- Android APK build with Buildozer

Default Login

- Username: "admin"
- Password: "1234"

Package Information

- Package: "com.josephmbui.feetrackacademy"
- Version: "1.0.1"

Project Structure

FeeTrackAcademy/
├── main.py
├── buildozer.spec
├── feetrack.db
└── screens/
    ├── login_screen.py
    ├── dashboard_screen.py
    ├── add_student_screen.py
    ├── student_list_screen.py
    ├── student_detail_screen.py
    └── payment_screen.py

Run on Desktop

python main.py

Build Android APK

buildozer android debug

Requirements

- Python 3
- Kivy 2.3.0
- ReportLab

Author

Joseph Mbui
Email: mbuijoseph51@gmail.com
