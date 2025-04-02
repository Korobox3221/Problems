# CS50X Final project: Portfolio

## Project Author: Konstantin Korobeynikov
### [Video Demo: Watch Here](https://www.youtube.com/watch?v=hjfRIVtKuKw)
## Description:


📌 This portfolio website is my final project for Harvard’s CS50x, showcasing my programming skills, academic background, and professional journey. Built with Python’s Flask framework, it integrates a backend database to store user messages and visitor analytics, while the frontend employs modern design principles like fluid typography via Utopia.fyi. The site is fully responsive and designed to reflect my identity as a developer.

🔍 Key Objectives
Demonstrate proficiency in full-stack development (Flask, SQLite, HTML/CSS/JS).

Create a dynamic, interactive platform to display my projects and credentials.

Implement backend functionality to capture user engagement (messages, IP analytics).

✨ Features
1. User-Focused Navigation
The website features an intuitive navigation bar with four sections:

HOME: A visually striking introduction with a personalized backdrop (photo of your city) and social media links.

ABOUT: A brief bio, your image, and a list of technical skills (languages, frameworks, tools).

EXPERIENCE: Academic achievements (Linguistics degree, CS50 certificates) and a link to your CS50 problem sets repository.

CONTACT: A functional form that submits messages to a database.

2. Backend Functionality
SQLite Database:

Stores user messages (name, email, message) for later retrieval.

Logs visitor IPs and interaction data (e.g., timestamps) for analytics.

Flask Integration:

Handles routing, form submissions, and dynamic content rendering.

3. Frontend Design
Fluid Typography: Uses Utopia.fyi for scalable, responsive text.

Visual Hierarchy: Clean sections with consistent spacing and contrast.

Interactive Elements: Hover effects on buttons/social icons for engagement.

4. Responsiveness
Adapts seamlessly to mobile, tablet, and desktop screens.

Media queries ensure readability and usability across devices.

🛠 Technologies Used
Frontend
HTML5/CSS3: Semantic markup and custom styling.


Utopia.fyi: Fluid type scaling for responsive typography.

Backend
Python (Flask): Backend logic and routing.

SQLite3: Lightweight database for message storage.

CS50’s SQL Library: Simplified database queries.

Development Tools
Git/GitHub: Version control.

VS Code: Primary code editor.

🚀 How to Run Locally
Prerequisites
Python 3.x

Flask (pip install flask)

CS50 SQL Library (pip install cs50)



Run app.py to initialize SQLite tables:

bash
Copy
python app.py
Launch the Application:

Navigate to http://localhost:5000 in your browser.

📂 Project Structure
plaintext
Copy
🔧 Technical Deep Dive
1. Database Design
Tables:

messages: Stores id, name, email, message, and timestamp.

visitors: Logs ip_address, user_agent, and visit_time.

Security:

Form validation prevents SQL injection (using CS50’s SQL library).

2. Flask Backend
Routes:

/: Renders the homepage.

/contact: Handles POST requests for message submissions.

Dynamic Content:

Certificates and repository links are hardcoded for simplicity but could be pulled from a database in future iterations.

3. Frontend Techniques
Utopia.fyi Integration:

Clamp-based fluid typography ensures text scales smoothly between breakpoints.

Example CSS snippet:

css
Copy
:root {
  --space-3xs: clamp(0.3125rem, 0.3125rem + 0vw, 0.3125rem);
  --space-2xs: clamp(0.5625rem, 0.5408rem + 0.1087vw, 0.625rem);
  --space-xs: clamp(0.875rem, 0.8533rem + 0.1087vw, 0.9375rem);
  --space-s: clamp(1.125rem, 1.0815rem + 0.2174vw, 1.25rem);
  --space-m: clamp(1.6875rem, 1.6223rem + 0.3261vw, 1.875rem);
  --space-l: clamp(2.25rem, 2.163rem + 0.4348vw, 2.5rem);
  --space-xl: clamp(3.375rem, 3.2446rem + 0.6522vw, 3.75rem);
  --space-2xl: clamp(4.5rem, 4.3261rem + 0.8696vw, 5rem);
  --space-3xl: clamp(6.75rem, 6.4891rem + 1.3043vw, 7.5rem);
}

📜 License
This project is open-source under the MIT License.

🙏 Acknowledgments
1. CS50 Team
David Malan and the CS50 staff for creating an unparalleled introduction to computer science. The course’s hands-on approach gave me the confidence to build this project from scratch.

2. Inspiration & Resources
Utopia.fyi: For revolutionizing my approach to responsive typography.

Flask Documentation: Guided backend implementation.

3. Personal Reflection
Completing CS50x transformed my understanding of programming. From struggling with Problem Set 0 to deploying a full-stack portfolio, the journey has been immensely rewarding. This project encapsulates my growth and serves as a foundation for future endeavors in web development.

🎯 Future Improvements
User Authentication: Allow visitors to log in and manage their messages.

Project Gallery: Dynamic loading of projects via an API (e.g., GitHub repos).

Dark Mode: Toggle for improved accessibility.

