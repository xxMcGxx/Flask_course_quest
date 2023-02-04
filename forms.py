from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, StringField
from wtforms.validators import InputRequired, Length


# Стартовая форма
class StartForm(FlaskForm):
    gamer_name = StringField("Имя игрока", validators=[
        InputRequired(), Length(
            min=3,
            max=20,
            message="Имя игрока не может быть менее 3х символов и более 20 символов.")]
                             )
    start_button = SubmitField("Начать приключение")


# Финишная форма
class FinishForm(FlaskForm):
    finish_button = SubmitField("Вернуться на главную")


# Основная игровая форма
class GameForm(FlaskForm):
    direction = SelectField(
        'Выберете направление для движения',
        coerce=int,
        choices=[
            (0, 'Север'),
            (1, 'Восток'),
            (2, 'ЮГ'),
            (3, 'Запад')
        ],
        render_kw={"class": "form-control"}
    )
    moves = IntegerField("Количество передвижений", render_kw={"class": "form-control"}, validators=[InputRequired()])
    move_button = SubmitField("Идти")
