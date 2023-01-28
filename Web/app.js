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
  var host = document.getElementById("host").value;
  console.log(host);

  // data = [];
  // data.push(discordTag);
  // data.push(host)
  // exportData(data);
})