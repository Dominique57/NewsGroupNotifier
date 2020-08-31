FROM python:3.8

# Create a /code folder to put everything in
RUN mkdir /code
# Defines this as relative directory
WORKDIR /code
# Copy requirements file
COPY doc/requirements.txt /code/
# Create venv to separate OS-python and application-python
RUN python -m venv env
# Install requirements
RUN env/bin/pip install -r requirements.txt
# Copy code
COPY src/ /code/

CMD ["env/bin/gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
