let totalSeconds = 60 * 60; // 1 hour

    function updateTimer() {
        let minutes = Math.floor(totalSeconds / 60);
        let seconds = totalSeconds % 60;

        document.getElementById('timer').textContent = `${minutes}m ${seconds}s`;

        if (totalSeconds <= 0) {
            clearInterval(timerInterval);
            alert("Time is up! Submitting the form.");
            document.getElementById('quizForm').submit();  // Make sure your form has id="quizForm"
        }

        totalSeconds--;
    }

    const timerInterval = setInterval(updateTimer, 1000);