
$(".dump").on("click", function(){
xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  var a, today;
  if (xhttp.readyState === 4 && xhttp.status === 200) {
    a = document.createElement('a');
    a.href = window.URL.createObjectURL(xhttp.response);
    today = new Date();
    a.download = "users_" + today.toDateString().split(" ").join("_") + ".xls";
    a.style.display = 'none';
    document.body.appendChild(a);
    return a.click();
  }
};
xhttp.open("GET", "/dump", true);
xhttp.setRequestHeader("Content-Type", "application/json");
xhttp.responseType = 'blob';
xhttp.send();
}
);