FROM python:3.9-alpine

# Install dependencies
RUN pip install flask numpy flask-restful flask-cors

# Copy source code
COPY . /app

# Set working directory
WORKDIR /app

# Expose port 8080
EXPOSE 8080

# Start Flask app
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]