# Stitch Learning Dashboard - Flask Backend

🔥 **Team 999+ Learning Dashboard with Flask Backend** 🔥

## Overview

This is a complete Flask backend for the Stitch learning dashboard with all HTML templates converted to work with Flask routing. The application includes:

- **Main Dashboard**: Course overview, upcoming lessons, offline content
- **Course Details**: Individual course pages with lesson listings
- **Lesson Player**: Video lesson interface
- **Settings & Profile**: User settings and profile management
- **AI Chat Assistant**: AI tutoring interface
- **Offline Content Management**: Download and manage offline content
- **P2P File Sharing**: Peer-to-peer file sharing capabilities

## Features

✅ **Complete Flask Backend**: All routes and endpoints configured
✅ **Template Integration**: HTML templates converted to Jinja2 
✅ **Navigation System**: Full navigation between all pages
✅ **API Endpoints**: RESTful API for courses and lessons data
✅ **Responsive Design**: TailwindCSS styling maintained
✅ **Dark Mode Support**: Built-in dark/light theme switching

## Project Structure

```
stitch_main_learning_dashboard/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── templates/               # Jinja2 HTML templates
│   ├── main_learning_dashboard_1.html
│   ├── main_learning_dashboard_2.html
│   ├── course_details_screen.html
│   ├── lesson_player.html
│   ├── settings_and_profile.html
│   ├── ai_chat-assistant.html
│   ├── offline_content_management.html
│   └── p2p_file_sharing.html
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── team_999+/              # Virtual environment
```

## Flask Routes

- `/` or `/dashboard` - Main learning dashboard
- `/dashboard2` - Alternative dashboard view  
- `/course/<course_name>` - Course details page
- `/lesson/<lesson_name>` - Lesson player
- `/settings` - Settings and profile
- `/profile` - Redirects to settings
- `/offline` - Offline content management
- `/p2p` or `/sharing` - P2P file sharing
- `/ai-tutor` or `/ai-chat` - AI chat assistant
- `/api/courses` - API endpoint for courses data
- `/api/lessons/<course_id>` - API endpoint for lessons data

## Installation & Setup

1. **Activate Virtual Environment**:
   ```bash
   source team_999+/bin/activate
   ```

2. **Install Dependencies** (if needed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and go to `http://localhost:5000`

## API Usage

### Get Courses
```bash
curl http://localhost:5000/api/courses
```

### Get Lessons for Course
```bash
curl http://localhost:5000/api/lessons/1
```

## Navigation Features

- **Dashboard**: View all courses, upcoming lessons, offline content
- **Course Pages**: Click any course to see detailed lesson listings
- **Lesson Player**: Click lessons to open video player
- **Settings**: Access user profile and settings
- **AI Tutor**: Chat with AI assistant for help
- **P2P Sharing**: Share files with peers
- **Offline Content**: Download content for offline use

## Development Notes

- All HTML templates updated with Flask `url_for()` functions
- Navigation links properly configured between pages
- Responsive design maintained with TailwindCSS
- Dark mode support preserved
- API endpoints ready for frontend integration
- Extensible structure for adding new features

## Next Steps

- Add database integration (SQLite/PostgreSQL)
- Implement user authentication
- Add file upload functionality
- Connect real video streaming
- Implement P2P file sharing backend
- Add AI chat integration

---

**Developed by Team 999+ for the Stitch Learning Platform** 🚀
