import os
import re

def update_template_file(file_path):
    """Update HTML template file with Flask endpoints"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Update common navigation links
    content = re.sub(r'href="#"', '{{ url_for("dashboard") }}', content)
    
    # Update footer navigation based on context
    if 'home' in content and 'material-symbols-outlined' in content:
        # Update home link
        content = re.sub(
            r'<a class="[^"]*" href="{{ url_for\(\'dashboard\'\) }}"[^>]*>\s*<span class="material-symbols-outlined">home</span>',
            '<a class="flex flex-col items-center gap-1 text-primary" href="{{ url_for(\'dashboard\') }}"><span class="material-symbols-outlined">home</span>',
            content
        )
        
        # Update courses link
        content = re.sub(
            r'<span class="material-symbols-outlined">school</span>',
            '<span class="material-symbols-outlined">school</span>',
            content
        )
        
        # Update AI tutor link
        content = re.sub(
            r'<span class="material-symbols-outlined">smart_toy</span>',
            '<span class="material-symbols-outlined">smart_toy</span>',
            content
        )
        
        # Update profile link
        content = re.sub(
            r'<span class="material-symbols-outlined">person</span>',
            '<span class="material-symbols-outlined">person</span>',
            content
        )
    
    # Fix specific navigation patterns
    if 'course_details_screen' in file_path:
        # Update back button to go to dashboard
        content = re.sub(
            r'<button class="[^"]*"[^>]*>\s*<span class="material-symbols-outlined[^"]*">arrow_back</span>',
            '<a href="{{ url_for(\'dashboard\') }}" class="flex items-center justify-center rounded-full p-2 hover:bg-gray-200/50 dark:hover:bg-gray-700/50"><span class="material-symbols-outlined text-gray-700 dark:text-gray-300">arrow_back</span></a>',
            content
        )
        
        # Update footer navigation
        content = re.sub(
            r'<a class="[^"]*" href="{{ url_for\(\'dashboard\'\) }}"[^>]*>\s*<span class="material-symbols-outlined">home</span>\s*<span class="[^"]*">Home</span>\s*</a>',
            '<a class="flex flex-col items-center gap-1 p-2 text-gray-500 dark:text-gray-400" href="{{ url_for(\'dashboard\') }}"><span class="material-symbols-outlined">home</span><span class="text-xs font-medium">Home</span></a>',
            content
        )
        
        content = re.sub(
            r'<a class="[^"]*" href="{{ url_for\(\'dashboard\'\) }}"[^>]*>\s*<span class="material-symbols-outlined">school</span>\s*<span class="[^"]*">Courses</span>\s*</a>',
            '<a class="flex flex-col items-center gap-1 rounded-lg p-2 text-primary" href="{{ url_for(\'course_details\', course_name=\'physics\') }}"><span class="material-symbols-outlined">school</span><span class="text-xs font-medium">Courses</span></a>',
            content
        )
        
        content = re.sub(
            r'<a class="[^"]*" href="{{ url_for\(\'dashboard\'\) }}"[^>]*>\s*<span class="material-symbols-outlined">smart_toy</span>\s*<span class="[^"]*">AI Tutor</span>\s*</a>',
            '<a class="flex flex-col items-center gap-1 p-2 text-gray-500 dark:text-gray-400" href="{{ url_for(\'ai_chat\') }}"><span class="material-symbols-outlined">smart_toy</span><span class="text-xs font-medium">AI Tutor</span></a>',
            content
        )
        
        content = re.sub(
            r'<a class="[^"]*" href="{{ url_for\(\'dashboard\'\) }}"[^>]*>\s*<span class="material-symbols-outlined">person</span>\s*<span class="[^"]*">Profile</span>\s*</a>',
            '<a class="flex flex-col items-center gap-1 p-2 text-gray-500 dark:text-gray-400" href="{{ url_for(\'settings\') }}"><span class="material-symbols-outlined">person</span><span class="text-xs font-medium">Profile</span></a>',
            content
        )
        
        # Update lesson click handlers to go to lesson player
        content = re.sub(
            r'<div class="flex cursor-pointer items-center gap-4 rounded-lg[^"]*"[^>]*>',
            '<a href="{{ url_for(\'lesson_player\', lesson_name=\'introduction-physics\') }}" class="flex cursor-pointer items-center gap-4 rounded-lg bg-white/50 dark:bg-gray-800/20 p-3 hover:bg-primary/10 dark:hover:bg-primary/20 block no-underline">',
            content
        )
    
    with open(file_path, 'w') as f:
        f.write(content)

# Update all template files
template_files = [
    'templates/course_details_screen.html',
    'templates/lesson_player.html', 
    'templates/settings_and_profile.html',
    'templates/ai_chat-assistant.html',
    'templates/offline_content_management.html',
    'templates/p2p_file_sharing.html',
    'templates/main_learning_dashboard_2.html'
]

for file_path in template_files:
    if os.path.exists(file_path):
        update_template_file(file_path)
        print(f"Updated {file_path}")
    else:
        print(f"File not found: {file_path}")
