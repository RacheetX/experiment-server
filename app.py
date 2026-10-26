import os
from flask import Flask, Response

app = Flask(__name__)

@app.route('/<exp_code>', methods=['GET'])
def get_experiment_code(exp_code):
    match exp_code:
        case "exp1":
            # Code from Experiment 1: Classes and Objects[cite: 8]
            code = r"""
// ==========================================
// CODE 1: StudentDemo
// ==========================================
class Student {
    String name;
    int age;
    String email;
    String contact;

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Email: " + email);
        System.out.println("Contact: " + contact);
        System.out.println();
    }
}

class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "Racheet";
        s1.age = 18;
        s1.email = "racheet@gmail.com";
        s1.contact = "9876543210";

        Student s2 = new Student();
        s2.name = "Ketan";
        s2.age = 19;
        s2.email = "ketan@gmail.com";
        s2.contact = "9876501234";

        Student s3 = new Student();
        s3.name = "Aditya";
        s3.age = 20;
        s3.email = "aditya@gmail.com";
        s3.contact = "9876512345";

        s1.display();
        s2.display();
        s3.display();
    }
}

// ==========================================
// CODE 2: BankDemo
// ==========================================
class BankAccount {
    private String name;
    private double balance;

    public void setName(String name) {
        this.name = name;
    }
    public void setBalance(double balance) {
        this.balance = balance;
    }
    public String getName() {
        return name;
    }
    public double getBalance() {
        return balance;
    }
}

class BankDemo {
    public static void main(String[] args) {
        BankAccount b = new BankAccount();
        b.setName("Racheet");
        b.setBalance(500000);
        System.out.println("Account Holder: " + b.getName());
        System.out.println("Balance: " + b.getBalance());
    }
}
"""
        case "exp2":
            # Code from Experiment 2: Method and constructor overloading[cite: 7]
            code = r"""
// ==========================================
// CODE 1: Constructor Overloading
// ==========================================
class Student {
    String name;
    int age;
    String course;

    Student(String name) {
        this.name = name;
        System.out.println("Student Name: " + name);
    }

    Student(String name, int age) {
        this.name = name;
        this.age = age;
        System.out.println("Student Name: " + name);
        System.out.println("Age: " + age);
    }

    Student(String name, int age, String course) {
        this.name = name;
        this.age = age;
        this.course = course;
        System.out.println("Student Name : " + name);
        System.out.println("Age : " + age);
        System.out.println("Course : " + course);
    }
}

public class StudentDemo {
    public static void main(String[] args) {
        System.out.println("Constructor 1");
        Student s1 = new Student("Racheet");
        System.out.println("\nConstructor 2");
        Student s2 = new Student("Racheet", 19);
        System.out.println("\nConstructor 3");
        Student s3 = new Student("Racheet", 19, "Computer Engineering");
    }
}

// ==========================================
// CODE 2: Method Overloading
// ==========================================
class Shape {
    void calculateArea(double radius) {
        double area = 3.14 * radius * radius;
        System.out.println("Area of Circle = " + area);
    }
    void calculateArea(double length, double breadth) {
        double area = length * breadth;
        System.out.println("Area of Rectangle = " + area);
    }
    void calculateArea(int base, double height) {
        double area = 0.5 * base * height;
        System.out.println("Area of Triangle = " + area);
    }
    void calculateArea(int side) {
        int area = side * side;
        System.out.println("Area of Square = " + area);
    }
}

public class ShapeDemo {
    public static void main(String[] args) {
        Shape obj = new Shape();
        obj.calculateArea(7.0);          
        obj.calculateArea(10.0, 5.0);    
        obj.calculateArea(8, 6.0);  
        obj.calculateArea(4);
    }
}
"""
        case "exp3":
            # Code from Experiment 3: Inheritance and Exception Handling[cite: 6]
            code = r"""
// ==========================================
// CODE 1: School Management System
// ==========================================
class Person {
    String name;
    int age;
    Person(String name, int age) {
        this.name=name;
        this.age=age;
    }
    void PersonDet() {
        System.out.println("Name: "+name);
        System.out.println("Age: "+age);
    }
}

class Student extends Person {
    int rollno;
    String course;
    Student(String name, int age, int rollno, String course) {
        super(name,age);
        this.rollno=rollno;
        this.course=course;
    }
    void StudDet() {
        PersonDet();
        System.out.println("Roll No: "+rollno);
        System.out.println("Course: "+course);
    }
}

class GraduateStudent extends Student {
    String special;
    GraduateStudent(String name, int age, int rollno, String course, String special) {
        super(name,age,rollno,course);
        this.special=special;
    }
    void GrStudDet() {
        StudDet();
        System.out.println("Specialization: "+special);
    }
}

class Teacher extends Person {
    String sub;
    String salary;
    Teacher(String name,int age,String sub , String salary) {
        super(name,age);
        this.sub=sub;
        this.salary=salary;
    }
    void TeacherDet() {
        PersonDet();
        System.out.println("Subject: "+sub);
        System.out.println("Salary: "+salary);
    }
}

public class SchoolManagement {
    public static void main(String[] args) {
        Student s1 = new Student("Harsh", 18, 201, "Java");
        GraduateStudent g1 = new GraduateStudent("Aryan", 19, 202, "Springboot", "Masters");
        Teacher t1 = new Teacher("Sweety Ma'am", 24, "Full Stack Java","₹65,000" );
        
        System.out.println("Student Details");
        s1.StudDet();
        System.out.println("-------------");
        
        System.out.println("Graduate Student Details");
        g1.GrStudDet();
        System.out.println("-------------");
        
        System.out.println("Teacher Details");
        t1.TeacherDet();
    }
}

// ==========================================
// CODE 2: Hospital Management System
// ==========================================
interface AdministrativeDuties {
    void manageSchedule();
    void fillReports();
}
interface MedicalDuties {
    void diagnosePatient();
    void prescribeMedicine();
}

class DoctorAdministrator implements AdministrativeDuties, MedicalDuties {
    String name;
    int doctorId;
    DoctorAdministrator(String name, int doctorId) {
        this.name = name;
        this.doctorId = doctorId;
    }
    public void manageSchedule() {
        System.out.println("Managing doctor's schedule.");
    }
    public void fillReports() {
        System.out.println("Filling hospital reports.");
    }
    public void diagnosePatient() {
        System.out.println("Diagnosing the patient.");
    }
    public void prescribeMedicine() {
        System.out.println("Prescribing appropriate medicine.");
    }
    void showDetails() {
        System.out.println("Doctor Name: " + name);
        System.out.println("Doctor ID: " + doctorId);
    }
}

public class Main {
    public static void main(String[] args) {
        DoctorAdministrator doctor = new DoctorAdministrator("Dr. Raj", 1001);
        System.out.println("----- DOCTOR DETAILS -----");
        doctor.showDetails();
        System.out.println("\n----- ADMINISTRATIVE DUTIES -----");
        doctor.manageSchedule();
        doctor.fillReports();
        System.out.println("\n----- MEDICAL DUTIES -----");
        doctor.diagnosePatient();
        doctor.prescribeMedicine();
    }
}

// ==========================================
// CODE 3: Exception Handling
// ==========================================
import java.util.Scanner;

public class StudentMarks {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = 0;
        double average;
        
        for (int i = 1; i <= 5; i++) {
            while (true) {
                try {
                    System.out.print("Enter marks for Subject " + i + ": ");
                    int marks = sc.nextInt();
                    if (marks < 0 || marks > 100) {
                        throw new Exception("Marks must be between 0 and 100.");
                    }
                    total += marks;
                    break;
                } catch (Exception e) {
                    System.out.println("Invalid input: " + e.getMessage());
                    sc.nextLine();
                }
            }
        }
        
        average = total / 5.0;
        System.out.println("\n===== RESULT =====");
        System.out.println("Total Marks : " + total);
        System.out.println("Average     : " + average);
        
        if (average >= 90) {
            System.out.println("Grade       : A");
        } else if (average >= 75) {
            System.out.println("Grade       : B");
        } else if (average >= 50) {
            System.out.println("Grade       : C");
        } else if (average >= 35) {
            System.out.println("Grade       : D");
        } else {
            System.out.println("Grade       : Fail");
        }
        sc.close();
    }
}
"""
        case "exp5":
            # Code from Experiment 5: Static website HTML CSS JS[cite: 5]
            code = r"""
<!-- ========================================== -->
<!-- 1. index.html -->
<!-- ========================================== -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VCET College Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="logo">
            <h1>VCET</h1>
            <p>Vidyavardhini's College of Engineering & Technology</p>
        </div>
        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    <main>
        <section id="home" class="home">
            <div class="home-text">
                <h2>Welcome to VCET</h2>
                <p>Welcome to Vidyavardhini's College of Engineering & Technology. This website provides basic information about our college.</p>
                <button onclick="showMessage()">Click Here</button>
                <p id="message"></p>
            </div>
            <div class="home-image">
                <img src="https://tse1.mm.bing.net/th/id/OIP.a5sCpjqba4596WcOxZzaHAHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3" alt="VCET College">
            </div>
        </section>
        <section id="about" class="box">
            <div>
                <h2>About VCET</h2>
                <p>VCET provides students with technical knowledge, practical learning and opportunities to improve their skills.</p>
            </div>
            <div class="icon">🎓</div>
        </section>
        <section id="contact" class="box">
            <div>
                <h2>Contact</h2>
                <p>For more information, please contact the college office.</p>
                <button onclick="contactMessage()">Contact Us</button>
                <p id="contactMessage"></p>
            </div>
            <div class="icon">✉</div>
        </section>
    </main>
    <footer>
        <p>© 2026 VCET College Website</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>

/* ========================================== */
/* 2. style.css */
/* ========================================== */
html {
    scroll-behavior: smooth;
}
body {
    font-family: Arial, sans-serif;
    margin: 0;
    background-color: #f2f6fa;
    color: #333;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}
header {
    background-color: #174a7e;
    color: white;
    padding: 25px 8%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
}
.logo h1 { margin: 0; font-size: 42px; }
.logo p { margin: 5px 0 0; font-size: 17px; }
nav a {
    color: white;
    text-decoration: none;
    margin-left: 30px;
    padding: 10px 15px;
    border-radius: 7px;
    transition: 0.3s;
}
nav a:hover { background-color: #3b82d0; }
main {
    width: 86%;
    max-width: 1050px;
    margin: auto;
    flex: 1;
}
.home {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 45px;
    padding: 50px 10px;
}
.home-text { flex: 1; }
.home-text h2 { color: #123f75; font-size: 42px; margin-bottom: 20px; }
.home-text p { font-size: 18px; line-height: 1.7; }
.home-image { flex: 1; }
.home-image img { width: 100%; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.15); }
button {
    background-color: #174a7e;
    color: white;
    border: none;
    padding: 13px 25px;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
}
button:hover { background-color: #0d355c; transform: translateY(-2px); }
button:active { transform: scale(0.97); }
#message, #contactMessage { color: #174a7e; font-weight: bold; }
.box {
    background-color: white;
    margin: 25px 0;
    padding: 35px 40px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: 0.3s;
}
.box:hover { transform: translateY(-3px); box-shadow: 0 7px 18px rgba(0,0,0,0.13); }
.box h2 { color: #123f75; font-size: 32px; margin-top: 0; }
.box p { font-size: 18px; line-height: 1.6; }
.icon {
    width: 120px; height: 120px;
    background-color: #e8f1fb;
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    font-size: 55px; margin-left: 30px;
}
footer { background-color: #174a7e; color: white; text-align: center; padding: 20px; margin-top: 30px; }
footer p { margin: 0; }
@media (max-width: 700px) {
    header { flex-direction: column; text-align: center; }
    nav { margin-top: 20px; }
    nav a { margin: 5px; display: inline-block; }
    .home { flex-direction: column; padding: 35px 0; }
    .home-text h2 { font-size: 34px; }
    .box { padding: 25px; }
    .icon { width: 80px; height: 80px; font-size: 40px; }
}

// ========================================== 
// 3. script.js 
// ========================================== 
function showMessage() {
    const message = document.getElementById("message");
    message.textContent = "Welcome to VCET! Have a great learning experience.";
}
function contactMessage() {
    const message = document.getElementById("contactMessage");
    message.textContent = "Thank you for your interest in VCET.";
}
"""
        case "exp6":
            # Code from Experiment 6: JS email validation[cite: 4]
            code = r"""
<!-- ========================================== -->
<!-- 1. index.html -->
<!-- ========================================== -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VCET College Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="logo">
            <h1>VCET</h1>
            <p>Vidyavardhini's College of Engineering & Technology</p>
        </div>
        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    <main>
        <section id="home" class="home">
            <div class="home-text">
                <h2>Welcome to VCET</h2>
                <p>Welcome to Vidyavardhini's College of Engineering & Technology. This website provides basic information about our college.</p>
                <button onclick="showMessage()">Click Here</button>
                <p id="message"></p>
            </div>
            <div class="home-image">
                <img src="https://tse1.mm.bing.net/th/id/OIP.a5sCpjqba4596WcOxZzaHAHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3" alt="VCET College">
            </div>
        </section>
        <section id="about" class="box">
            <div>
                <h2>About VCET</h2>
                <p>VCET provides students with technical knowledge, practical learning and opportunities to improve their skills.</p>
            </div>
            <div class="icon">🎓</div>
        </section>
        <section id="contact" class="box">
            <div>
                <h2>Contact</h2>
                <p>For more information, please contact the college office.</p>
                <button onclick="contactMessage()">Contact Us</button>
                <p id="contactMessage"></p>
                <h3>Validate Your Email</h3>
                <input type="text" id="email" placeholder="Enter your email">
                <br><br>
                <button onclick="validateEmail()">Validate Email</button>
                <p id="emailMessage"></p>
            </div>
            <div class="icon">✉</div>
        </section>
    </main>
    <footer>
        <p>© 2026 VCET College Website</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>

/* ========================================== */
/* 2. style.css */
/* ========================================== */
html { scroll-behavior: smooth; }
body {
    font-family: Arial, sans-serif;
    margin: 0;
    background-color: #f2f6fa;
    color: #333;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}
header {
    background-color: #174a7e;
    color: white;
    padding: 25px 8%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
}
.logo h1 { margin: 0; font-size: 42px; }
.logo p { margin: 5px 0 0; font-size: 17px; }
nav a {
    color: white;
    text-decoration: none;
    margin-left: 30px;
    padding: 10px 15px;
    border-radius: 7px;
    transition: 0.3s;
}
nav a:hover { background-color: #3b82d0; }
main { width: 86%; max-width: 1050px; margin: auto; flex: 1; }
.home { display: flex; justify-content: space-between; align-items: center; gap: 45px; padding: 50px 10px; }
.home-text { flex: 1; }
.home-text h2 { color: #123f75; font-size: 42px; margin-bottom: 20px; }
.home-text p { font-size: 18px; line-height: 1.7; }
.home-image { flex: 1; }
.home-image img { width: 100%; border-radius: 10px; display: block; box-shadow: 0 5px 15px rgba(0,0,0,0.15); }
button { background-color: #174a7e; color: white; border: none; padding: 13px 25px; border-radius: 6px; font-size: 16px; cursor: pointer; transition: 0.3s; }
button:hover { background-color: #0d355c; transform: translateY(-2px); }
button:active { transform: scale(0.97); }
#message, #contactMessage, #emailMessage { color: #174a7e; font-weight: bold; }
.box { background-color: white; margin: 25px 0; padding: 35px 40px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: flex; justify-content: space-between; align-items: center; transition: 0.3s; }
.box:hover { transform: translateY(-3px); box-shadow: 0 7px 18px rgba(0,0,0,0.13); }
.box h2 { color: #123f75; font-size: 32px; margin-top: 0; }
.box h3 { color: #123f75; margin-top: 25px; }
.box p { font-size: 18px; line-height: 1.6; }
.box input { width: 280px; padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 16px; box-sizing: border-box; }
.icon { width: 120px; height: 120px; background-color: #e8f1fb; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 55px; margin-left: 30px; }
footer { background-color: #174a7e; color: white; text-align: center; padding: 20px; margin-top: 30px; }
footer p { margin: 0; }
@media (max-width: 700px) {
    header { flex-direction: column; text-align: center; }
    nav { margin-top: 20px; }
    nav a { margin: 5px; display: inline-block; }
    .home { flex-direction: column; padding: 35px 0; }
    .home-text h2 { font-size: 34px; }
    .box { padding: 25px; flex-direction: column; }
    .icon { width: 80px; height: 80px; font-size: 40px; margin: 20px 0 0; }
}

// ========================================== 
// 3. script.js 
// ========================================== 
function showMessage() {
    const message = document.getElementById("message");
    message.textContent = "Welcome to VCET! Have a great learning experience.";
}
function contactMessage() {
    const message = document.getElementById("contactMessage");
    message.textContent = "Thank you for your interest in VCET.";
}
function validateEmail() {
    const emailInput = document.getElementById("email");
    const emailMessage = document.getElementById("emailMessage");
    const email = emailInput.value;
    if (email.indexOf("@") === -1 || email.indexOf(".") === -1) {
        alert("Invalid email address. Please include '@' and '.' characters.");
        emailInput.focus();
        emailMessage.textContent = "Please enter a valid email address.";
        return false;
    }
    alert("Email is valid!");
    emailMessage.textContent = "Email is valid!";
    return true;
}
"""
        case "exp7":
            # Code from Experiment 7: DOM background color[cite: 3]
            code = r"""
<!-- ========================================== -->
<!-- 1. index.html -->
<!-- ========================================== -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VCET College Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div class="logo">
            <h1>VCET</h1>
            <p>Vidyavardhini's College of Engineering & Technology</p>
        </div>
        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </nav>
    </header>
    <main>
        <section id="home" class="home">
            <div class="home-text">
                <h2>Welcome to VCET</h2>
                <p>Welcome to Vidyavardhini's College of Engineering & Technology. This website provides basic information about our college.</p>
                <button onclick="showMessage()">Click Here</button>
                <p id="message"></p>
            </div>
            <div class="home-image">
                <img src="https://tse1.mm.bing.net/th/id/OIP.a5sCpjqba4596WcOxZzaHAHaDt?r=0&rs=1&pid=ImgDetMain&o=7&rm=3" alt="VCET College">
            </div>
        </section>
        <section id="about" class="box">
            <div>
                <h2>About VCET</h2>
                <p>VCET provides students with technical knowledge, practical learning and opportunities to improve their skills.</p>
            </div>
            <div class="icon">🎓</div>
        </section>
        <section id="contact" class="box">
            <div>
                <h2>Contact</h2>
                <p>For more information, please contact the college office.</p>
                <button onclick="contactMessage()">Contact Us</button>
                <p id="contactMessage"></p>
                <h3>Validate Your Email</h3>
                <input type="text" id="email" placeholder="Enter your email">
                <br><br>
                <button onclick="validateEmail()">Validate Email</button>
                <p id="emailMessage"></p>
            </div>
            <div class="icon">✉</div>
        </section>
        <section class="color-section">
            <h2>Current Background Color</h2>
            <p id="colorName">lightblue</p>
        </section>
    </main>
    <footer>
        <p>© 2026 VCET College Website</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>

/* ========================================== */
/* 2. style.css */
/* ========================================== */
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: Arial, sans-serif; background-color: lightblue; color: #222; }
header { background-color: #174a7e; color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; }
.logo h1 { font-size: 32px; }
.logo p { font-size: 14px; }
nav a { color: white; text-decoration: none; margin-left: 25px; font-weight: bold; }
nav a:hover { text-decoration: underline; }
main { padding: 40px; }
.home { display: flex; justify-content: space-between; align-items: center; gap: 40px; margin-bottom: 40px; }
.home-text { flex: 1; }
.home-text h2 { color: #174a7e; font-size: 32px; margin-bottom: 15px; }
.home-text p { line-height: 1.6; margin-bottom: 15px; }
.home-image { flex: 1; text-align: center; }
.home-image img { width: 100%; max-width: 500px; border-radius: 10px; }
button { background-color: #174a7e; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-size: 15px; }
button:hover { background-color: #0d355a; }
.box { background-color: white; padding: 30px; margin-bottom: 30px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center; gap: 30px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
.box h2 { color: #174a7e; margin-bottom: 12px; }
.box p { line-height: 1.6; }
.icon { font-size: 50px; }
.box h3 { color: #174a7e; margin-top: 25px; margin-bottom: 10px; }
.box input { width: 280px; padding: 12px; border: 1px solid #ccc; border-radius: 6px; font-size: 16px; }
#message, #contactMessage, #emailMessage { color: #174a7e; font-weight: bold; }
.color-section { background-color: white; text-align: center; padding: 30px; margin-bottom: 30px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
.color-section h2 { color: #174a7e; margin-bottom: 10px; }
#colorName { font-size: 24px; font-weight: bold; color: #174a7e; }
footer { background-color: #174a7e; color: white; text-align: center; padding: 20px; }
@media (max-width: 768px) {
    header { flex-direction: column; text-align: center; gap: 15px; }
    nav a { margin: 0 10px; }
    .home { flex-direction: column; }
    .box { flex-direction: column; text-align: center; }
    .box input { width: 100%; max-width: 280px; }
    main { padding: 20px; }
}

// ========================================== 
// 3. script.js 
// ========================================== 
function showMessage() {
    const message = document.getElementById("message");
    message.textContent = "Welcome to VCET! Have a great learning experience.";
}
function contactMessage() {
    const message = document.getElementById("contactMessage");
    message.textContent = "Thank you for your interest in VCET.";
}
function validateEmail() {
    const emailInput = document.getElementById("email");
    const emailMessage = document.getElementById("emailMessage");
    const email = emailInput.value;
    if (email.indexOf("@") === -1 || email.indexOf(".") === -1) {
        alert("Invalid email address. Please include '@' and '.' characters.");
        emailInput.focus();
        emailMessage.textContent = "Please enter a valid email address.";
        return false;
    }
    alert("Email is valid!");
    emailMessage.textContent = "Email is valid!";
    return true;
}

const colors = ["lightblue", "lightgreen", "lightpink", "lightyellow", "lightgray"];
let index = 0;
function changeColor() {
    document.body.style.backgroundColor = colors[index];
    const colorName = document.getElementById("colorName");
    colorName.textContent = colors[index];
    index = (index + 1) % colors.length;
}
setInterval(changeColor, 5000);
"""
        case "exp8":
            # Code from Experiment 8: JS Text animation[cite: 2]
            code = r"""
<!-- ========================================== -->
<!-- 1. index.html -->
<!-- ========================================== -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VCET Query & Feedback Portal</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <div class="circle circle1"></div>
    <div class="circle circle2"></div>
    <div class="circle circle3"></div>
    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="particle p5"></div>
    <div class="ring"></div>
    <div class="notification">
        <span class="dot"></span>
        Student Portal
    </div>
    <h1>VCET</h1>
    <p class="subtitle">QUERY & FEEDBACK PORTAL</p>
    <div id="spiral" class="spiral"></div>
    <div id="spiral2" class="spiral"></div>
    <div class="portal-text">
        <div class="card">
            <span class="icon">?</span>
            <span>ASK</span>
        </div>
        <div class="card">
            <span class="icon">↗</span>
            <span>SHARE</span>
        </div>
        <div class="card">
            <span class="icon">✓</span>
            <span>IMPROVE</span>
        </div>
    </div>
    <button onclick="changeText()">EXPLORE PORTAL</button>
    <div class="arrow">↓</div>
</div>
<script src="script.js"></script>
</body>
</html>

/* ========================================== */
/* 2. style.css */
/* ========================================== */
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    height: 100vh;
    display: flex; justify-content: center; align-items: center;
    background: #1b0045; overflow: hidden; font-family: Arial, sans-serif;
}
.container {
    width: 90%; max-width: 850px; height: 480px;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    position: relative; border-radius: 20px;
    background: rgba(255, 255, 255, 0.08);
    box-shadow: 0 0 30px rgba(128, 103, 255, 0.4);
    animation: appear 1.5s ease;
}
@keyframes appear { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }
h1 {
    position: relative; z-index: 5; color: white; font-size: 55px; letter-spacing: 8px;
    animation: glow 2s infinite alternate;
}
@keyframes glow { from { text-shadow: 0 0 5px #8067ff; } to { text-shadow: 0 0 25px #8067ff; } }
.subtitle { color: #c5baff; font-size: 15px; letter-spacing: 4px; margin-top: 5px; animation: slide 1.5s ease; }
@keyframes slide { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }
.spiral { display: flex; align-items: center; gap: 8px; position: absolute; }
@keyframes spiral { from { --angle: 0deg; } to { --angle: 360deg; } }
.character {
    font-size: 30px; font-weight: bold; color: #8067ff; text-transform: uppercase;
    transform: translateY(calc(sin(var(--angle)) * 100px)) scale(calc(cos(var(--angle)) * 0.5 + 0.5));
    animation: spiral 4s linear infinite, characterGlow 1.5s infinite alternate;
}
@keyframes characterGlow { from { text-shadow: 0 0 5px #8067ff; } to { text-shadow: 0 0 20px #b9aaff; } }
.portal-text { position: relative; z-index: 5; display: flex; gap: 20px; margin-top: 160px; }
.portal-text span {
    padding: 10px 20px; color: white; background: rgba(128, 103, 255, 0.2);
    border: 1px solid #8067ff; border-radius: 20px;
    animation: float 2s infinite alternate; transition: 0.3s;
}
.portal-text span:nth-child(2) { animation-delay: 0.3s; }
.portal-text span:nth-child(3) { animation-delay: 0.6s; }
@keyframes float { from { transform: translateY(0); } to { transform: translateY(-8px); } }
.portal-text span:hover { transform: scale(1.1); background: #8067ff; }
button {
    margin-top: 25px; padding: 12px 25px; border: none; border-radius: 25px;
    background: #8067ff; color: white; font-weight: bold; cursor: pointer;
    animation: pulse 2s infinite;
}
@keyframes pulse { 50% { box-shadow: 0 0 20px #8067ff; } }
button:hover { transform: scale(1.08); }
@media (max-width: 600px) {
    h1 { font-size: 40px; }
    .subtitle { font-size: 10px; }
    .character { font-size: 20px; }
    .portal-text { gap: 8px; }
    .portal-text span { padding: 8px 12px; font-size: 12px; }
}

// ========================================== 
// 3. script.js 
// ========================================== 
let isFirefox = typeof InstallTrigger !== 'undefined';
const words = "VCET QUERY & FEEDBACK PORTAL";
let ANGLE = 360;
const ANIMATION_DURATION = 4000;

const animation = () => {
    ANGLE -= 1;
    document.querySelectorAll(".spiral *").forEach((el, i) => {
        const translateY = Math.sin(ANGLE * (Math.PI / 120)) * 100;
        const scale = Math.cos(ANGLE * (Math.PI / 120)) * 0.5 + 0.5;
        const offset = parseInt(el.dataset.offset);
        const delay = i * (ANIMATION_DURATION / 16) - offset;
        setTimeout(() => {
            el.style.transform = `translateY(${translateY}px) scale(${scale})`;
        }, delay);
    });
    requestAnimationFrame(animation);
};

words.split("").forEach((char, i) => {
    const createElement = (offset) => {
        const div = document.createElement("div");
        div.innerText = char;
        div.classList.add("character");
        div.setAttribute("data-offset", offset);
        div.style.animationDelay = `-${i * (ANIMATION_DURATION / 16) - offset}ms`;
        return div;
    };
    document.querySelector("#spiral").append(createElement(0));
    document.querySelector("#spiral2").append(
        createElement((isFirefox ? 1 : -1) * (ANIMATION_DURATION / 2))
    );
});

function changeText() {
    const button = document.querySelector("button");
    button.innerText = "PORTAL OPENED";
    button.style.transform = "scale(1.15)";
    setTimeout(() => {
        button.innerText = "EXPLORE PORTAL";
        button.style.transform = "scale(1)";
    }, 1500);
}

if (isFirefox) {
    animation();
}
"""
        case "exp9":
            # Code from Experiment 9: React Hooks color buttons[cite: 1]
            code = r"""
// ==========================================
// CODE: src/App.jsx
// ==========================================
import { useState } from "react";

function App() {
  const [color, setColor] = useState("");
  
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Choose a Color</h2>
      <button onClick={() => setColor("Red")}>Red SE 1</button>
      <button onClick={() => setColor("Blue")}>Blue SE 2</button>
      <button onClick={() => setColor("Green")}>Green SE 3</button>
      <button onClick={() => setColor("Yellow")}>Yellow VCET</button>
      
      {color && (
        <h3 style={{ color: color }}>
          You have selected {color} color
        </h3>
      )}
    </div>
  );
}

export default App;
"""
        case _:
            code = "# Error: Experiment code not found. Available keys: exp1, exp2, exp3, exp5, exp6, exp7, exp8, exp9."

    return Response(code, mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)