let person = {
    discordTag: "",
    host: false,
    classes: []
};

function exportData(formArrayData)
{  
  for (var i of formArrayData) {
    console.log(i + ' ');
  }

  //console.log(Object.fromEntries(formData));
}
function submitCall()
{
    ar = document.querySelectorAll("#registrationForm input");
    exportData(ar);
}

document.addEventListener("submit", submitCall());