/*
//have the para in json format to send to server vis post
var para={
    "id": 3,
    "email": "777@gmail.com",
    "password": "testpassword3",
    "first_name": "FirstName 3",
    "last_name": "LastName 3",
    "mobile_no": "3333333333",
    "date_of_joining": "03-03-2021"
    }
    
//create a new XML http request obj
var req=new XMLHttpRequest()
//open api end point url with open()
req.open("PUT","http://localhost:3001/staff/2")
//set header content type to json
req.setRequestHeader("Content-type","application/json")
//converting para to json string using stringify
req.send(JSON.stringify(para))
//after completing req process, check status
req.onload=getrest 
 

function getrest(){
//create a new XML http request obj
var req=new XMLHttpRequest()
//open api end point url with open()
req.open("GET","http://localhost:3001/staff")
//sending request
req.send();
//after completing req process, check status
req.onload=()=>{
    //checking if successful
    if(req.status===200)
    {//print returned data to console
        console.log(JSON.parse(req.response))
        document.getElementById("restresponse").innerText=req.response
    }
    else
    {console.log("cant contact server")

    }
}
}
//have the para in json format to send to server vis post
var para={
    "email": "999@gmail.com",
    
    }
    
//create a new XML http request obj
var req=new XMLHttpRequest()
//open api end point url with open()
req.open("PUT","http://localhost:3001/staff/2")
//set header content type to json
req.setRequestHeader("Content-type","application/json")
//converting para to json string using stringify
req.send(JSON.stringify(para))
//after completing req process, check status
req.onload=getrest 
 

function getrest(){
//create a new XML http request obj
var req=new XMLHttpRequest()
//open api end point url with open()
req.open("PATCH","http://localhost:3001/staff/2")
//sending request
req.send();
//after completing req process, check status
req.onload=()=>{
    //checking if successful
    if(req.status===200)
    {//print returned data to console
        console.log(JSON.parse(req.response))
        document.getElementById("restresponse").innerText=req.response
    }
    else
    {console.log("cant contact server")

    }
}
}*/

//including a form
function  samplepost(){

var para={
    email:document.getElementById("email").value,
    password:document.getElementById("fname").value,
    first_name:document.getElementById("lname").value,
    last_name:document.getElementById("pwrd").value,
    mobile_no:document.getElementById("mob").value,
    d_o_j:document.getElementById("doj").value,
    }
    
//create a new XML http request obj
var req=new XMLHttpRequest()
//open api end point url with open()
req.open("POST","http://localhost:3001/staff/")
//set header content type to json
req.setRequestHeader("Content-type","application/json")
//converting para to json string using stringify
req.send(JSON.stringify(para))
//after completing req process, check status
//req.onload=getrest 
}

function getrest(){
    //create a new XML http request obj
    var req=new XMLHttpRequest()
    //open api end point url with open()
    req.open("PATCH","http://localhost:3001/staff/2")
    //sending request
    req.send();
    //after completing req process, check status
    req.onload=()=>{
        //checking if successful
        if(req.status===200)
        {//print returned data to console
            console.log(JSON.parse(req.response))
            document.getElementById("restresponse").innerText=req.response
        }
        else
        {console.log("cant contact server")
    
        }
    }
}