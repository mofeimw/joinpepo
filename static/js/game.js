document.addEventListener('DOMContentLoaded', function() {
    const options = document.querySelectorAll('.option');
    const submitButton = document.getElementById('submit-answer');
    const nextButton = document.querySelector('.next-button');
    const explanation = document.querySelector('.explanation');
    let selectedOption = null;
    let answered = false;
    let incorrectAttempts = [];

    // Get current level and question from URL
    const urlParts = window.location.pathname.split('/');
    const level = urlParts[2];
    const questionIndex = urlParts[3];

    options.forEach(option => {
        option.addEventListener('click', function() {
            if (answered) return;

            // Clear previous selection
            options.forEach(opt => opt.classList.remove('selected'));
            
            // Also clear any previous 'incorrect' marking when selecting a new option
            if (!answered) {
                options.forEach(opt => opt.classList.remove('incorrect'));
            }

            // Mark as selected
            this.classList.add('selected');
            selectedOption = parseInt(this.getAttribute('data-index'));

            // We don't check the answer immediately anymore
            // That will happen when the submit button is clicked
        });
    });

    // Add event listener to the submit button
    submitButton.addEventListener('click', function() {
        // Only proceed if an option has been selected and not already answered correctly
        if (selectedOption !== null && !answered) {
            checkAnswer(selectedOption);
        }
    });

    function checkAnswer(optionIndex) {
        fetch('/check_answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `option=${optionIndex}&level=${level}&question_index=${questionIndex}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.correct) {
                answered = true;
                
                // Highlight the selected option as correct
                options[optionIndex].classList.add('correct');
                
                // Show explanation if available
                if (explanation) {
                    explanation.style.display = 'block';
                }
                
                // Show next button and hide submit button only when correct
                nextButton.style.display = 'block';
                submitButton.style.display = 'none';
            } else {
                // Mark this attempt as incorrect
                options[optionIndex].classList.add('incorrect');
                
                // Add to incorrect attempts
                if (!incorrectAttempts.includes(optionIndex)) {
                    incorrectAttempts.push(optionIndex);
                }
                
                // Keep submit button visible for another attempt
                // User can select another option and try again
                submitButton.style.display = 'block';
            }
        });
    }
});
