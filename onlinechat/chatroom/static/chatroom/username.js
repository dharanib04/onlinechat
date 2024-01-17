document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("#submit").addEventListener("click", function (event) {
    const newName = document.getElementById("newusername").value;
    const regex = "/^[]+$/";
    const password = document.getElementById("password").value;
    if (
      newName == "" ||
      password == "" ||
      password == null ||
      newName == null
    ) {
      event.preventDefault();
      document.getElementById("error").innerHTML = "Please enter all fields";
    } else if (!newName.match(regex)) {
      event.preventDefault();
      document.getElementById("error").innerHTML =
        "Please enter a valid unsername";
    }
  });
});
