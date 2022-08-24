var para={
    "id": 8,
    "email": "777@gmail.com",
    "password": "testpassword8",
    "first_name": "FirstName 8",
    "last_name": "LastName 8",
    "mobile_no": "33333333338",
    "date_of_joining": "03-08-2021"
}
//no logic here
fetch("https://localhost:3001/staff",{
    method:"post",
    headers:{
        "Accept":"application/json,text/plain, */*",
        "Content-Type":"application/json" 
    },
    body:JSON.stringify(para)
})
.then((repsonse)=response.json())
.then((data)=>console.log(data)) //printing data to console
.catch((error)=>console.log(error))