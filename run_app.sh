#!/bin/bash
echo "🔥 Starting Team 999+ Flask Learning Dashboard! 🔥"
echo "---------------------------------------------------"
echo "Activating virtual environment..."
source team_999+/bin/activate

echo "Starting Flask application..."
echo "Access the app at: http://localhost:5000"
echo "---------------------------------------------------"
echo ""
echo "Available Routes:"
echo "• http://localhost:5000/ - Main Dashboard"
echo "• http://localhost:5000/course/mathematics-101 - Course Details"
echo "• http://localhost:5000/lesson/algebra-basics - Lesson Player"
echo "• http://localhost:5000/settings - Settings & Profile"
echo "• http://localhost:5000/ai-chat - AI Chat Assistant"
echo "• http://localhost:5000/offline - Offline Content"
echo "• http://localhost:5000/p2p - P2P File Sharing"
echo "• http://localhost:5000/api/courses - API Courses"
echo ""
echo "Press Ctrl+C to stop the server"
echo "---------------------------------------------------"

python app.py
