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
  event.preventDefault() // prevents the form from autosubmitting
  var discordTag = document.getElementById("discord-name").value;
  console.log(discordTag);

  // we see which of the two is checked and print its value 
  var hostYes = document.getElementById("host-yes").checked;
  var hostNo = document.getElementById("host-no").checked;
  if (hostYes == true){
    console.log(document.getElementById("host-yes").value);
  } else  {
    console.log(document.getElementById("host-no").value)
  }

  // data = [];
  // data.push(discordTag);
  // data.push(host)
  // exportData(data);
})