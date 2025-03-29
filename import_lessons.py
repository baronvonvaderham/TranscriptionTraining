import os

from TranscriptionTraining.settings import BASE_DIR


if __name__ == '__main__':
    # Get list of lesson directory names to loop through, and same for already-imported lessons to save time
    lesson_dirs = os.listdir(os.path.join(BASE_DIR, 'lessons'))
    existing_lesson_index = open(os.path.join(BASE_DIR, 'TranscriptionTraining/lesson_index.txt')).read()
    if not existing_lesson_index:
        existing_lesson_index = []
    lesson_index = []
    print(existing_lesson_index)
    for lesson in lesson_dirs:

        # First check if it has been imported already, skip if so and just include in index
        if lesson in existing_lesson_index:
            lesson_index.append(lesson)
            continue

        """
        If it's a new lesson, execute the following steps:
        
        1) Create the new template file with the raw JS contents and lesson name references inserted.
        2) Loop over all assets and update SRC references in the file.
        
        """
        js = open(os.path.join(BASE_DIR, f'lessons/{lesson}/assets/js/project.js')).read()

        for asset in os.listdir(os.path.join(BASE_DIR, f'lessons/{lesson}/ar')):
            js = js.replace(f'ar/{asset}', f'{{% static "{lesson}/ar/{asset}" %}}')

        for asset in os.listdir(os.path.join(BASE_DIR, f'lessons/{lesson}/dr')):
            js = js.replace(f'dr/{asset}', f'{{% static "{lesson}/dr/{asset}" %}}')

        for asset in os.listdir(os.path.join(BASE_DIR, f'lessons/{lesson}/assets/htmlimages')):
            js = js.replace(f'dr/{asset}', f'{{% static "{lesson}/assets/htmlimages/{asset}" %}}')

        lesson_template = \
        f"""
        {{% load static %}}
        <script>
            {js}
        </script>
        """

        with open(os.path.join(BASE_DIR, f'templates/{lesson}.html'), 'w') as template:
            template.write(lesson_template)

        lesson_index.append(lesson)

    # Write the lesson index to the file to save
    with open(os.path.join(BASE_DIR, 'TranscriptionTraining/lesson_index.txt'), 'w') as index:
        index.write(str(lesson_index))
