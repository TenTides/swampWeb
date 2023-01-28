var form = document.getElementById("registrationForm");

// let person = {
//     discordTag: "",
//     host: false,
//     classes: []
// };

// function exportData(formArrayData)
// {  
//   for (var i of formArrayData) {
//     console.log(i + ' ');
//   }

//   //console.log(Object.fromEntries(formData));
// }

form.addEventListener('submit', function(event) {
  data = [];
  event.preventDefault() // prevents the form from autosubmitting

  var discordTag = document.getElementById("discord-name").value;
  console.log(discordTag);

  // we see which of the two is checked and print its value 
  var hostYes = document.getElementById("host-yes").checked;
  var hostNo = document.getElementById("host-no").checked;
  if (hostYes == true){
    console.log(document.getElementById("host-yes").value);
    data.push(hostYes);
  } else  {
    console.log(document.getElementById("host-no").value)
    data.push(hostNo);
  }
 
  pythonArrayExport(data);
})

function pythonArrayExport(data)
{
  const spawner = require['child_process'].spawner
  const python_process = spawner('python',['./sheetManager.py',JSON.stringify(data)])
}