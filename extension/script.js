document.addEventListener('DOMContentLoaded', function() {
   document.getElementById('checkButton').addEventListener('click', function() {
       var url = document.getElementById('url').value;
       if (url.trim() === '') {
           alert('Please enter a URL');
           return;
       }

       // Send POST request to server
       fetch('https://phishing-detection-rrta.onrender.com/predict', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json'
           },
           body: JSON.stringify({
               url: url
           })
       })
       .then(response => response.json())
       .then(data => {
           // Display the result in the output div
           document.getElementById('output').innerHTML = `
               <p>Result: ${data.result}</p>
               <p>Phishing Probability: ${data.phishingProbability}</p>
           `;
       })
       .catch(error => {
           console.error('Error checking URL:', error);
           document.getElementById('output').innerHTML = 'Error checking URL';
       });
   });
});
