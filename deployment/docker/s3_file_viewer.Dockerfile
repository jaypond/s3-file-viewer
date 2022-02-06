FROM base_python_image

COPY ./app /usr/app
WORKDIR /usr/app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]