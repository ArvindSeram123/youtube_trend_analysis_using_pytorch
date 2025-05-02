# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the 'dashboard' folder into the container
COPY app.py /app/app.py

# Copy the 'data/output/top_tags' directory into the container
COPY data/output /app/data/output

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the Streamlit app when the container starts
CMD ["sh", "-c", "streamlit run /app/app.py"]
