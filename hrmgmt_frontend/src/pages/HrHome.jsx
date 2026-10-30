function HrHome(){
    let currentUser=localStorage.getItem("currentUser")
    let navigate=useNavigate()
    let handleLogout=(e)=>{
        localStorage.removeItem("currentUser")
        navigate("/login")
    }

    return(
        <div>
            <h1>HR Home page called</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    )

}

export default HrHome