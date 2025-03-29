Transcription Training
======================

Setup
------------

1. Install Python 3 on your machine (for MacOS, use [these instructions](https://docs.python-guide.org/starting/install3/osx/)).
2. Open a terminal.
3. Navigate to the directory containing the project code within the terminal.
4. Run the following command: `pip install -r requirements.txt`

Adding New Lessons
------------------

1. Drop the extracted folder of lesson assets into the `lessons` directory within this project.
IMPORTANT NOTE: The name of the lesson folder cannot contain spaces! Rename the folder as necessary (can just replace spaces with underscores).
2. Open a terminal
3. Navigate to the directory containing the project code within the terminal.
4. Run the command `python import_lessons.py`

Running the Server Locally
--------------------------

1. Open a terminal.
2. Navigate to the directory containing the project code within the terminal.
3. Run the following command: `python manage.py runserver`
4. Open a new browser tab and type into the navigation bar: `http://127.0.0.1:8000/`
5. To stop the server, in the terminal window hit Ctrl+C (or Command+C).

Anticipated Troubleshooting
---------------------------

* If you need to re-import one or more lessons, you will need to open `lesson_index.txt` and delete its contents (or at a minimum remove the entry for the lesson you need to redo).