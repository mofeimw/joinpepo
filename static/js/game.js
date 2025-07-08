function playAudio(audioPath, screenIdentifier) {
  console.log('Attempting to play audio:', audioPath);

  // Update audio state if we have a screen identifier
  if (screenIdentifier) {
    audioState.currentScreen = screenIdentifier;
  }

  const audioElement = document.getElementById('narration');
  if (!audioElement) {
    console.error('Audio element not found');
    return;
  }

  const audioSource = audioElement.querySelector('source');
  if (!audioSource) {
    console.error('Audio source element not found');
    return;
  }

  // Update the source
  audioSource.src = `/static/audio/${audioPath}`;

  // Reset and reload audio
  audioElement.pause();
  audioElement.load();

  // Try to play audio
  const playPromise = audioElement.play();

  if (playPromise !== undefined) {
    playPromise.then(() => {
      // Audio played successfully
      console.log('Audio playing successfully:', audioPath);
      if (screenIdentifier) {
        audioState.isPlaying = true;
      }
    }).catch(error => {
      // Audio failed to play
      console.error('Audio play failed:', error);
      console.log('Try clicking the play button to hear the audio');
    });
  }
}


document.addEventListener('DOMContentLoaded', function() {
  const options = document.querySelectorAll('.option-btn');
  const nextBtn = document.getElementById('next');
  let selectedIndex = null;
  let answerCorrect = false;

  // Grab curriculum, level, and questionIndex from the URL
  // e.g. "/chess/game/2/3" → ["", "chess", "game", "2", "3"]
  const parts = window.location.pathname.split('/');
  const [, curriculum, /*game*/, level, questionIndex] = parts;

  // Handle option selection
  options.forEach(opt => {
    opt.addEventListener('click', () => {
      if (answerCorrect) return;
      options.forEach(o => o.classList.remove('selected', 'correct'));
      opt.classList.add('selected');
      selectedIndex = parseInt(opt.dataset.index, 10);
    });
  });


  // Function to check answer; intercepts click in capture phase
  async function checkAnswer(e) {
    if (answerCorrect) return;
    e.preventDefault();
    e.stopImmediatePropagation();

    if (selectedIndex === null) {
      alert('Please select an option first');
      return;
    }

    try {
      const resp = await fetch(`/${curriculum}/check_answer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        // Use the parsed `level` and `questionIndex` from the URL
        body: `option=${selectedIndex}&level=${level}&question_index=${questionIndex}`
      });
      const result = await resp.json();

      if (result.correct) {
        options[selectedIndex].classList.add('correct');
        answerCorrect = true;
        nextBtn.removeEventListener('click', checkAnswer, true);
        playAudio('correct.mp3', '');

        document.getElementById('mascot').src = '/static/images/avatar/correct.gif';
      } else {
        playAudio('wrong.mp3', '');
        options[selectedIndex].classList.add('incorrect');
      }
    } catch (err) {
      console.error('Error checking answer:', err);
    }
  }

  // Attach in capture phase to block inline onclick until correct
  nextBtn.addEventListener('click', checkAnswer, true);
});

