You can run this Dockerized password manager application on any machine that supports Docker, including Linux, Windows, and macOS. Below are the steps to set up and run the project on each of these operating systems.
Prerequisites

    Install Docker:
        Linux: Follow the instructions on the Docker website.
        Windows: Install Docker Desktop from Docker's website.
        macOS: Install Docker Desktop from Docker's website.

    Install Docker Compose:
        Linux: Docker Compose is usually included with the Docker package. If not, you can follow the installation instructions.
        Windows: Docker Compose is included with Docker Desktop.
        macOS: Docker Compose is included with Docker Desktop.

Steps to Run the Project

Clone the Repository:

Open a terminal (or Command Prompt/PowerShell on Windows) and clone your GitHub repository:


    git clone https://github.com/yourusername/password_manager.git
    
    cd password_manager

Run Docker Compose:

Ensure you are in the root directory of the project where the docker-compose.yml file is located, and then run:

    docker-compose up --build

This command will build the Docker image and start the container.

Accessing the Application

Once the container is running, you can interact with the password manager through the Docker container's shell.

To open a shell into the running container, run:

    docker exec -it password_manager_password_manager_1 /bin/bash

This command opens a bash shell in the running container (adjust the container name if necessary).

From there, you can run the password manager:

    python app/main.py

Example Usage

You will see a menu in the terminal where you can add, retrieve, and list passwords.

    1. Add a new password
    2. Retrieve a password
    3. List all stored passwords
    4. Exit

Exiting

To stop the application, press Ctrl+C in the terminal where Docker Compose is running. Then, you can shut down the Docker container with:

    docker-compose down

Troubleshooting

 Linux: If you encounter permission issues with Docker, you might need to run the commands with sudo.

 Windows: Ensure Docker Desktop is running before you run any Docker commands.
 
 macOS: Ensure Docker Desktop is running before you run any Docker commands.

Additional Notes

Ensure that the Docker daemon is running before you execute any Docker commands.
For Windows and macOS, Docker Desktop provides a user-friendly interface for managing Docker containers.
On all platforms, you can use tools like Portainer for managing Docker containers through a web interface.
