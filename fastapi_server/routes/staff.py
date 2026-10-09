from fastapi import APIRouter

staff_router= APIRouter(prefix="/staff")

@staff_router.get("/getStaffs")
def getSstaffs():
    return "get staff method called"
@staff_router.post("/addstaff")
def addstaff():
    return "add staff method called"