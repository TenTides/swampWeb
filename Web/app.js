<<<<<<< Updated upstream
// const spawner = require['child_process'].spawn;
=======
// import{python} from 'python-shell'
>>>>>>> Stashed changes
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

function sendData(username) {
  var hostname= window.location.hostname;
  fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      username: username,
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log(data)
  })
  .catch(error => {
    console.log(error)
  });
}

form.addEventListener('submit', function(event) {
  data = [];
  event.preventDefault() // prevents the form from autosubmitting

  var discordTag = document.getElementById("discord-name").value;
  console.log(discordTag);
  data.push(discordTag);

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
<<<<<<< Updated upstream

  pythonArrayExport(['johndoe#111','Yes']);
=======
  
  console.log(data);
  sendData(discordTag);
>>>>>>> Stashed changes
})

// function pythonArrayExport(data)
// {
//   const python_process = spawner('python',['./sheetManager.py', JSON.stringify(data)])
// }

<<<<<<< Updated upstream

// python_process.stdout.on('data', (data) => {
//   console.log['Data recieved from python script:', JSON.parse(data.toString())];
// })
=======
// PythonShell.sh(
//   sheetManager.py,
//   null,
//   function (err) {
//     if (err) throw err;
//     console.log('finish');
//   }
// )
>>>>>>> Stashed changes
