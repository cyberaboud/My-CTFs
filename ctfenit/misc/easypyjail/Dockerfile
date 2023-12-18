FROM ubuntu

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install Python 3
RUN apt-get install -y python3

# Create a non-root user 'ctf'
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

# Set the working directory
WORKDIR /home/ctf

# Copy necessary files
COPY jail.py .
#COPY flag.txt .
COPY ynetd .
RUN chmod 777 ./ynetd

# Change ownership to the 'ctf' user
RUN chown -R ctf:ctf /home/ctf

# Switch to the 'ctf' user
USER ctf

# Run the ynetd command to start the challenge
CMD ./ynetd -p 1234 "python3 jail.py" 2>/dev/null
