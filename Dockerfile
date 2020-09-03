FROM python:3.8

# Defines this as relative directory
WORKDIR /code
# Copy requirements file
COPY doc/requirements.txt .
# Install requirements
RUN pip install -r requirements.txt
# Copy code
COPY src/ .

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
