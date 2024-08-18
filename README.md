# HHMS - Hospital Management System

HHMS (Hospital Management System) is a Python QT desktop application designed to streamline operations in a hospital setting. The system divided into multiple sections within a hospital and serves various roles such as doctors, nurses, pharmacists, and radiologists.

## Main Sections

### Admission Section

- Manages patients' data and admissions process.

### Radiology Section

- Specialized section for radiologists to handle patient radiologies.

### Pharmacy Section

- Deals with drugs, medicines, selling, registering, and ordering for internal or external patients. Specifically designed for pharmacists.

### Staff Section

- Admin-only section to manage staff data for each role.

### Profile Section

- Displays information about the authenticated user and handles email communication.

### Home Section

- Visualizes the number of attended doctors, nurses, and available sets in the hospital using pie charts.

## Roles and Authorization Levels

The system supports different roles with varying levels of authorization for each section. Users can interact based on their assigned roles and permissions.

## Integrated Systems

### Messaging System

- Connects to the user's Outlook account using PyWin32 to check inbox messages and send messages.

### Attendance System

- Allows nurses and doctors to scan QR codes upon attendance, visualizing attendance data in pie charts for each day.

## Technologies Used

- **GUI Development:** PyQt5 and PySide6 used for building and handling the interface, including converting QT Designer UI files to Python.
- **Data Manipulation:** Pandas library utilized for data manipulation tasks.
- **Image Processing:** OpenCV integrated for handling radiology images and QR code tasks.
- **Database:** SQLite employed as the main database for storing application data.

## Future Enhancements

For future enhancements, the project could consider adding more roles and sections such as:

### Billing Section

- To handle all billing-related processes within the hospital.

### API Integration

- Integration with external systems using APIs to effectively communicate patient data, considering HL7 standards for interoperability.

This Hospital Management System aims to digitalize and optimize hospital operations, providing a comprehensive solution for various departments and roles within the healthcare environment.

## Instructions

- **Install Packages**: Run the following command to install required packages:

```python
pip install -r requirements.txt
```

- **Run Main File**: Execute the following command to run the main file:

```python
python -m main.py
```

---
