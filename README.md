# 🧠 DevTrackr – Developer Productivity CLI  
### Phase 3 CLI + ORM Project | Python + PostgreSQL + SQLAlchemy

---

## 📘 Overview
**DevTrackr** is a Command-Line Interface (CLI) application designed to help developers track productivity by recording coding sessions, logging challenges (hiccups), managing projects, and summarizing time spent.  
The system uses **SQLAlchemy ORM** with a **PostgreSQL** database for structured and efficient data storage.

This project combines a well-structured Python package, ORM-based database models, and a clean CLI interface powered by **Click** and **Rich** for colorful output.

---

## 🎯 Learning Goals
- Build a **CLI application** using Python and Click.
- Implement **SQLAlchemy ORM** with 3+ related tables.
- Manage a **PostgreSQL** database through CRUD operations.
- Use **environment variables** with `python-dotenv`.
- Apply **OOP concepts** and coding best practices.
- Manage dependencies in a **Pipenv virtual environment**.

---

## ⚙️ System Architecture
- **Python (Click + Rich)** → CLI layer for user interaction  
- **SQLAlchemy ORM** → Data modeling and persistence  
- **PostgreSQL** → Relational database for projects, developers, and sessions  
- **dotenv** → Secure configuration via `.env`  
- **Repository Pattern** → Clean separation between logic and database operations  

---

## 🧩 Features
✅ Add, edit, and delete developers and projects  
✅ Start and stop coding sessions (with timestamps)  
✅ Record hiccups (issues or blockers)  
✅ View summaries and total coding time per project  
✅ Colorful, easy-to-read CLI tables (via `Rich`)  
✅ Organized modular structure with ORM integration  

---

## 🗂 Project Structure
DevTrackr/
│
├── Pipfile
├── .env.example
├── run.py
├── README.md
│
├── devtrackr/
│ ├── init.py
│ ├── db.py
│ ├── models.py
│ ├── repository.py
│ ├── cli.py
│ ├── utils.py
│
└── tests/
└── test_smoke.py

**Install dependencies**
pipenv install
pipenv shell

**Create PostgreSQL database**
CREATE DATABASE devtrackr_db;

 **Initialize the database**
python run.py init-db

**CLI Usage Examples**
Command	Description;
python run.py add-developer "Brian Githinji"	Add a new developer
python run.py add-project "Bossie Ride App" "Uber-like web app"	Add a new project
python run.py list-projects	List all projects
python run.py start-timer 1 1	Start coding timer for a project
python run.py stop-timer 1	Stop the timer
python run.py summary	View summary of coding hours
python run.py edit-developer 1 "Brian G."	Edit developer info
python run.py delete-project 1	Delete a project

**Expected Outcomes**

Improved tracking of developer productivity.

Clear organization of projects, sessions, and hiccups.

Enhanced understanding of CLI app development and ORM integration.

Demonstration of full CRUD functionality and clean code practices.

**Future Improvements**

Add data visualization using Matplotlib or Plotly.

Export reports to PDF or CSV.

Implement authentication and user roles.

Develop a simple web dashboard version.

**Author**

Brian Githinji
GitHub: BRian-210

**License**

This project is licensed under the MIT License.

“Track your progress. Measure your impact. Code smarter with DevTrackr.”
