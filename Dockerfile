# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /card-api
# Set work directory
WORKDIR /card-api

# Install dependencies
COPY requirements.txt /card-api/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /card-api/

# Expose port 8000
EXPOSE 8000

# Run the application:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
