from django.core.management.base import BaseCommand
from app.models import Quiz, Question, Choice


class Command(BaseCommand):
    help = 'Fill database with quiz data'

    def handle(self, *args, **kwargs):
        python_quiz = Quiz.objects.create(title='Основы Python')

        question1 = Question.objects.create(
            quiz=python_quiz,
            text='Что такое PEP?',
        )
        choice1 = Choice.objects.create(
            question=question1,
            text='Python Enhancement Proposal',
            is_correct=True,
        )
        choice2 = Choice.objects.create(
            question=question1,
            text='Python Enterprise Platform',
            is_correct=False,
        )
        choice3 = Choice.objects.create(
            question=question1,
            text='Python Ecosystem Package',
            is_correct=False,
        )

        question2 = Question.objects.create(
            quiz=python_quiz,
            text='Как создать переменную в Python?',
        )
        choice4 = Choice.objects.create(
            question=question2,
            text='x = 5',
            is_correct=True,
        )
        choice5 = Choice.objects.create(
            question=question2,
            text='int x = 5',
            is_correct=False,
        )
        choice6 = Choice.objects.create(
            question=question2,
            text='var x = 5',
            is_correct=False,
        )

        question3 = Question.objects.create(
            quiz=python_quiz,
            text='Какой оператор используется для сравнения значений в Python?',
        )
        choice7 = Choice.objects.create(
            question=question3,
            text='==',
            is_correct=True,
        )
        choice8 = Choice.objects.create(
            question=question3,
            text='=',
            is_correct=False,
        )
        choice9 = Choice.objects.create(
            question=question3,
            text='===',
            is_correct=False,
        )

        question4 = Question.objects.create(
            quiz=python_quiz,
            text='Что выведет следующий код: print("hello"[::-1])?',
        )
        choice10 = Choice.objects.create(
            question=question4,
            text='olleh',
            is_correct=True,
        )
        choice11 = Choice.objects.create(
            question=question4,
            text='hello',
            is_correct=False,
        )
        choice12 = Choice.objects.create(
            question=question4,
            text='ll',
            is_correct=False,
        )

        question5 = Question.objects.create(
            quiz=python_quiz,
            text='Как получить количество элементов в списке в Python?',
        )
        choice13 = Choice.objects.create(
            question=question5,
            text='len()',
            is_correct=True,
        )
        choice14 = Choice.objects.create(
            question=question5,
            text='count()',
            is_correct=False,
        )
        choice15 = Choice.objects.create(
            question=question5,
            text='size()',
            is_correct=False,
        )

        self.stdout.write(self.style.SUCCESS('Quiz data has been successfully added to the database.'))

