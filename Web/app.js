let person = {
    discordTag: "",
    host: false,
    classes: []
};

function exportData(formArrayData)
{
  var formData = new FormData(form);
  
  for (var i of formArrayData) {
    console.log(i + ' ');
  }

  //console.log(Object.fromEntries(formData));
}
function submitCall()
{
    ar = Array.form(document.querySelectorAll("#registrationForm input"));
    exportData(ar);
}


document.addEventListener("submit", submitCall());