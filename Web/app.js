

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

form.addEventListener('submit', function(event) {
  event.preventDefault() // prevents the form from autosubmitting
  let discordTag = document.getElementsByName("discord-name").value;
  let host = document.getElementsByName("host").value;

  data = [];
  data.push(discordTag);
  data.push(host)
  exportData(data);
})