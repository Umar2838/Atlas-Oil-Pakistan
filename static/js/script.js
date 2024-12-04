document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById('submit-btn');

    submitButton.addEventListener('click', function (e) {
        e.preventDefault();  // Prevent the default form submission
        
        const code = document.getElementById('contact').value;

        if (code.length == 5) {
    
            alert('Code submitted: ' + code);
            document.querySelector('form').submit();  
        } else {
            alert('Please enter a 5-digit code.');
        }
    });
});