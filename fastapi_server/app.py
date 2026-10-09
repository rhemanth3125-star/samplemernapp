from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    stuname: str
    studept: str
    stuusername: str
    stupassword: str
    stuage: int
    stumarks: float

app = FastAPI()
@app.get("/getstudents")
def get_students():
    return "Get List of students"

@app.post("/addstudent")
def add_student(stud: Student):
    return "Add a new student"
@app.put("/updatestudent")
def update_student():               
    return "Update student details"
@app.delete("/deletestudent")
def delete_student():
    return "Delete a student"   
@app.get("/getparticularstudent/{id}")
def get_particular_student(id: int):
    return {"userid": id}
@app.get("/filterstudents")
def filter_students(dept: str, marks: int):
    return {"department": dept, "marks": marks}  