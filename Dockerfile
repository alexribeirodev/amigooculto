FROM python:3.12-slim

ENV CRYPTO_KEY=$CRYPTO_KEY
ENV NAMES=$NAMES

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN python generate_person_codes.py

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]