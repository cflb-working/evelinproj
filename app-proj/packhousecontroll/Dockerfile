# Dockerfile
FROM python:3.13.2

# Set the working directory
WORKDIR /app/app-proj/packhousecontroll

# Copy the requirements file
COPY ./requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

RUN python manage.py collectstatic --noinput
    #python manage.py makemigrations && \
    #python manage.py migrate

# Expose the port
EXPOSE 8000

# Copia o script de entrada
COPY scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh
COPY scripts/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
# Define o script como ponto de entrada
ENTRYPOINT ["sh", "/scripts/entrypoint.sh"]

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "packhousecontroll.wsgi:application"]
