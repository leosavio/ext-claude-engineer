import subprocess
import os

# Change to the project directory
os.chdir('springboot-rest-actuator')

# Run Maven command to compile and start the Spring Boot application
try:
    process = subprocess.Popen(['mvn', 'spring-boot:run'], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    
    # Print the first few lines of output to confirm the application is starting
    for i, line in enumerate(process.stdout):
        print(line.strip())
        if "Started DemoApplication" in line or i > 20:  # Stop after app starts or after 20 lines
            break
    
    print("\nApplication is now running. You can access it at http://localhost:8080")
    print("To test the new endpoint, try accessing http://localhost:8080/timenow")
    print("The process ID is:", process.pid)
    print("To stop the application, you'll need to use the stop_process function with this PID.")

except Exception as e:
    print(f"An error occurred: {str(e)}")