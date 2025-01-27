# Usa una imagen liviana de Python
FROM python:3.11-slim

# Definir el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY ./app /app
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto correcto
EXPOSE 8080

# Ejecutar la aplicación con Uvicorn en el puerto 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
