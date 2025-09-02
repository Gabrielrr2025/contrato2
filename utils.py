from num2words import num2words
import datetime

def valor_extenso(valor: float) -> str:
    return num2words(valor, lang="pt_BR")

def data_formatada(data: datetime.date) -> str:
    meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    return f"{data.day} de {meses[data.month-1]} de {data.year}"
