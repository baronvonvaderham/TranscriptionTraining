import ast
import os

from django.views.generic.base import TemplateView

from TranscriptionTraining.settings import BASE_DIR


class LessonListView(TemplateView):
    template_name = 'lesson_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson_list = ast.literal_eval(open(os.path.join(BASE_DIR, 'TranscriptionTraining/lesson_index.txt')).read())
        url_list = [f'/lesson/{lesson}' for lesson in lesson_list]
        context['lesson_url_list'] = url_list
        return context

class LessonView(TemplateView):
    template_name = 'lesson.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = kwargs.get('lesson')
        context['lesson_template'] = f'{lesson}.html'
        context['main_chunk'] = f'{lesson}/dist/main.chunk.js'
        context['bundle'] = f'{lesson}/dist/runtime-main.bundle.js'
        context['vendors_chunk'] = f'{lesson}/dist/vendors-main.chunk.js'
        return context
