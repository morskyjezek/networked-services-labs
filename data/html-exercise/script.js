function myalert()
{
    var myvariable = document.getElementById("saysomething").value;
    if (myvariable > "") {
        window.alert(myvariable);
    } else {
        window.alert("You did not say anything!");
    }
}
