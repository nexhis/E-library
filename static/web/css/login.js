function validate()
{
    var username=document.getElementById("username").value;
    var paassword=document.getElementById("password").value;
if(username=="user"&&paassword=="admin"){
alert("LOGIN SUCCCESSFUL");
return false;
}
else{
    alert("LOGIN FAILED : PASSWORD IS INCORRECT");
}
}