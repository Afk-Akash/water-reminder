# Use the official Python image from the Docker Hub
FROM artifactory.idfcfirstbank.com/etoll-docker/python:3.9-bullseye

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any necessary dependencies specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Install cron
RUN apt-get update && apt-get install -y cron

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/my-cron-job

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/my-cron-job

# Apply cron job
RUN crontab /etc/cron.d/my-cron-job

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

EXPOSE 8080

# Run the command on container startup
CMD ["python", "server.py"]
