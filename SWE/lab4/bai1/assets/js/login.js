var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    console.log(username);
    console.log(password);
    if (username == "giangvien" && password == "Abcd1234") {
        alert("Login successfully");
        alert(window.location.pathname);
        location.href = "giangvien.html"; // Redirecting to other page.
        return false;
    } else if (username == "giaovu" && password == "Abcd1234") {
        alert("Login successfully");
        window.location.href = "giaovu.html"; // Redirecting to other page.
        return false;
    } else if (username == "sinhvien" && password == "Abcd1234") {
        alert("Login successfully");
        window.location.href = "sinhvien.html"; // Redirecting to other page.
        return false;
    }
    else {
        attempt--;// Decrementing by one.
        alert("You have left " + attempt + " attempt;");
        // Disabling fields after 3 attempts.
        if (attempt == 0) {
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
            return false;
        }
    }
}