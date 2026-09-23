# Interface web do CourseFeedback — imagem de produção
FROM python:3.12-slim

WORKDIR /app

# Dependências primeiro: o cache da imagem só invalida
# se o requirements.txt mudar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_DEBUG=0
EXPOSE 8000

# gunicorn: servidor WSGI de produção (não é o Werkzeug de desenvolvimento)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
