from flask import Flask, render_template, redirect, url_for, request, jsonify
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Routes for the main pages
@app.route('/')
@app.route('/dashboard')
def dashboard():
    """Main learning dashboard - shows courses, upcoming lessons, offline content"""
    return render_template('main_learning_dashboard_1.html')

@app.route('/dashboard2')
def dashboard2():
    """Alternative dashboard view"""
    return render_template('main_learning_dashboard_2.html')

@app.route('/course/<int:course_id>')
@app.route('/course/<course_name>')
def course_details(course_id=None, course_name=None):
    """Course details page showing lessons, progress, etc."""
    # You can pass course data here in the future
    return render_template('course_details_screen.html')

@app.route('/lesson/<int:lesson_id>')
@app.route('/lesson/<lesson_name>')
def lesson_player(lesson_id=None, lesson_name=None):
    """Video lesson player page"""
    # You can pass lesson data here in the future
    return render_template('lesson_player.html')

@app.route('/settings')
def settings():
    """Settings and profile management page"""
    return render_template('settings_and_profile.html')

@app.route('/profile')
def profile():
    """User profile page (redirects to settings for now)"""
    return redirect(url_for('settings'))

@app.route('/offline')
def offline_content():
    """Offline content management page"""
    return render_template('offline_content_management.html')

@app.route('/p2p')
@app.route('/sharing')
def p2p_sharing():
    """P2P file sharing page"""
    return render_template('p2p_file_sharing.html')

@app.route('/ai-tutor')
@app.route('/ai-chat')
def ai_chat():
    """AI chat assistant page"""
    return render_template('ai_chat-assistant.html')

# API endpoints for dynamic functionality
@app.route('/api/courses')
def api_courses():
    """API endpoint to get courses data"""
    # Mock data - replace with real database queries
    courses = [
        {
            "id": 1,
            "name": "Mathematics 101",
            "instructor": "Dr. Smith",
            "lessons": 12,
            "progress": 30,
            "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuALt_PcL1UElaef_9_y4l7iRpW2RHVgi1WuXTbzNSGLhV0EErDQPtCxoZ6O9pK5AcJ46-RG7iv5CQJ7oEC1y6dcPk0lllma8wZkoeiJZ_qqeLZ1CI-594SCR9IFHSKFo5EGIMUHNzSTMwefHKMOFrAb-vu10cSZfpIhpjwHUH3nSX6Jbja8dCc4dViTrjzs_pWt2M37m1dFJdwm4-PShT9-BiodSJG4N28tY1BBu5IwQ5xg4cgVi50HZwmTb12uD5AsLZrHaqTy884"
        },
        {
            "id": 2,
            "name": "Science Fundamentals",
            "instructor": "Dr. Johnson",
            "lessons": 10,
            "progress": 60,
            "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAmdLdv9Swi_kE2gvRBBMJGoht48mnV73s0VR4QDYGBhUqWLOyqqV80WDqQOaROu9gIRMHvY-olK5h51H8TtonMP3hwhTwzb2wpcJhueQlKKVjiI8u7UOme7jP5Lk7xE-ov4kJRZSdtxVKj_ERM5xel_9WrP76VLhBRqIiaEusYifo6OPegh8mr0xQ4VOISwLvQoNUG07Hivm2m9bS9fj1FuMofPLczWCGqfKgi5Un6rVlY2_IW9s9l32Jnjq6k0Q4XJJagfKO1VDM"
        },
        {
            "id": 3,
            "name": "World History",
            "instructor": "Dr. Davis",
            "lessons": 15,
            "progress": 20,
            "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCoB_YQKKvLnfwldyT2xKkoZlVQHmUnqin6d0WapX5NJtyi7XKCtIfVZZdvpmLjkV8OJ5_swA-vaIRyUggikqBseePtJ0TOZt72PgQ9Xje1-BQE65SiROgHE10GrBE4xQcfSVKuURAVd1zADBFnW26_HUh_O3JvusahQuR_ZpLVGmGEfV85k44LKCKBBHc6LYV8rQ_a3tGpgOWvkSr3OXzMfUm33ecNEwQMo-rxGgZj2tH2aS6gm6vwN7Tw9EbczVjTUKK35vtMX3E"
        }
    ]
    return jsonify(courses)

@app.route('/api/lessons/<int:course_id>')
def api_lessons(course_id):
    """API endpoint to get lessons for a specific course"""
    # Mock data - replace with real database queries
    lessons = [
        {
            "id": 1,
            "title": "Introduction to Physics",
            "duration": "12:34",
            "status": "completed"
        },
        {
            "id": 2,
            "title": "Kinematics",
            "duration": "15:02",
            "status": "completed"
        },
        {
            "id": 3,
            "title": "Newton's Laws",
            "duration": "21:15",
            "status": "available"
        }
    ]
    return jsonify(lessons)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
