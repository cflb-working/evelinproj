#!/bin/sh
set -e

echo "Aguardando o banco de dados..."
/wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Banco de dados está pronto!"

echo "Aplicando migrações..."
python manage.py migrate

echo "Criando superusuário..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
    print('Superusuário criado com sucesso.')
EOF

echo "Iniciando a aplicação..."
exec "$@"
