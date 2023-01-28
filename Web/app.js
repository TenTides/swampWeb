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
    discordTag = document.getElementsByName("discord-name");
    host = document.getElementsByName("host");
    data = [];
    data.push(discordTag);
    data.push(host)
    exportData(data);
}

document.addEventListener("submit", submitCall());