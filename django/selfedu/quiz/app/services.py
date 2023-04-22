from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List

from .models import Quiz, Question, Choice

class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        quiz = Quiz.objects.get(uuid=self.quiz_dto.uuid)
        answers = []
        for answer_dto in self.answers_dto.answers:
            question = quiz.get_question_by_uuid(answer_dto.question_uuid)
            choices = Choice.objects.filter(uuid__in=answer_dto.choices)
            answers.append((question, choices))
        score = self._calculate_score(answers)
        return score

    def _calculate_score(self, answers) -> float:
        num_correct = 0
        total = 0
        for question, choices in answers:
            for choice in choices:
                if choice.is_correct:
                    num_correct += 1
                    break
            total += 1
        return num_correct / total if total > 0 else 0.0

