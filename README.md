# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram

```mermaid
graph TD
    %% Define Actors
    Student((Student))
    Admin((Administrator))

    %% Student Use Cases
    subgraph Enrollment System
        Student --> UC1(Login as Student)
        Student --> UC2(View Course Catalog)
        Student --> UC3(Register for a Course)
        Student --> UC4(Drop a Course)
        Student --> UC5(View My Schedule)
        Student --> UC6(Billing Summary)
        Student --> UC7(Edit My Profile)
        Student --> UC8(Logout and Save)

        %% Admin Use Cases
        Admin --> UC9(Login as Admin)
        Admin --> UCA(View Class Roster)
        Admin --> UCB(View All Students)
        Admin --> UCC(Add New Student)
        Admin --> UCD(Edit Student Profile)
        Admin --> UCE(Add New Course)
        Admin --> UCF(Edit Course)
        Admin --> UCG(View Student Schedule)
        Admin --> UCH(Admin Billing Summary)
        Admin --> UCI(Logout and Save)
    end
```

### Flowchart of the main workflow

```mermaid
flowchart TD
    Start([Execute Main]) --> Init[Load Data / Seed Defaults]
    Init --> LoginMenu{Login Menu}
    
    LoginMenu -->|1| StudentLogin[Student Login]
    LoginMenu -->|2| AdminLogin[Admin Login]
    LoginMenu -->|3| Exit[Save and Exit]
    
    StudentLogin --> CheckStudent{Valid ID or 'new'?}
    CheckStudent -->|Yes| StudentMenu
    CheckStudent -->|No| LoginMenu

    AdminLogin --> CheckPwd{Admin Password?}
    CheckPwd -->|Correct| AdminMenu
    CheckPwd -->|Incorrect| LoginMenu
    
    StudentMenu -->|Pick Action| StudentAction[Perform Action]
    StudentAction --> StudentMenu
    StudentMenu -->|Logout| LoginMenu
    
    AdminMenu -->|Pick Action| AdminAction[Perform Action]
    AdminAction --> AdminMenu
    AdminMenu -->|Logout| LoginMenu
    
    Exit --> End([Terminate Application])
```

### Prompts

Below are the prompts used to assist with generating the Python counterpart logic for Task 5:

1. *"Based on the Java `EnrollmentSystem` logic, Can you implement the 'Register for a use case and a simplifed Python code that represent the original one. Without having Gson file structure and let the user enter their Student ID, display the course catalog, and test the constraints (Capacity, Prerequisites, Time Conflict). Make it run via command-line until the user quits."*
