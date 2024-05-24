from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import FloatField, DecimalField, IntegerField
from wtforms.fields.simple import StringField, BooleanField, FileField, SubmitField
from wtforms.validators import InputRequired, NumberRange


class ProdutoForm(FlaskForm):
    nome = StringField(label='Nome do produto',
                       validators=[InputRequired(message="É obrigatório definir o nome do produto"),
                                   Length(max=100,message="O produto pode ter até 100 caracteres")])
    preco = DecimalField(label='Preço',
                         validators=[InputRequired(message="É obrigatorio definir o preço"),
                                     NumberRange(min=0,00, message="Os preços devem ser positivos")])
    estoque = IntegerField(label='Estoque',
                           validators=[InputRequired(message="É preciso definir o estoque"),
                                       NumberRange(min=0, message="O estoque precisa ser positivo")])
    ativo = BooleanField(label='Ativo?',
                         validators=[InputRequired(message="É preciso dizer se o produto"
                                                   "está ou não ativo")])
    foto = FileField(label='Foto do produto',
                     validators=[FileAllowed(['jpg', 'png'], message="Apenas arquivos JPG o PNG")]
    categoria = SelectField(label='Categoria do produto',
                            validators=[InputRequired(message="Selecione uma categoria")])
    submit = SubmitField()