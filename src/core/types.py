# Type Definitions for Windows EDR System

class WindowsEDR:
    def __init__(self, id: str, name: str, version: str):
        self.id = id  # Unique identifier for the EDR
        self.name = name  # Name of the EDR solution
        self.version = version  # Version of the EDR solution

    def __repr__(self):
        return f"<WindowsEDR(id={self.id}, name={self.name}, version={self.version})>"

class EDRAlert:
    def __init__(self, alert_id: str, severity: str, description: str, timestamp: str):
        self.alert_id = alert_id  # Unique identifier for the alert
        self.severity = severity  # Severity of the alert (e.g., low, medium, high)
        self.description = description  # Description of the alert
        self.timestamp = timestamp  # Time the alert was generated

    def __repr__(self):
        return f"<EDRAlert(alert_id={self.alert_id}, severity={self.severity}, description={self.description}, timestamp={self.timestamp})>"

class EDRProcess:
    def __init__(self, process_id: str, name: str, command_line: str, start_time: str):
        self.process_id = process_id  # Unique identifier for the process
        self.name = name  # Name of the process
        self.command_line = command_line  # Command line used to start the process
        self.start_time = start_time  # Time when the process started

    def __repr__(self):
        return f"<EDRProcess(process_id={self.process_id}, name={self.name}, command_line={self.command_line}, start_time={self.start_time})>"

# Additional type definitions can be added as needed.
