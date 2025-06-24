/**
 * audio.js - Handles audio playback for educational game
 */

// Initialize once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Find the audio element
    const audioElement = document.getElementById('narration');

    // If there's no audio element on this page, exit
    if (!audioElement) return;

    // Create a play button that will appear if autoplay fails
    const playButton = document.createElement('button');
    playButton.innerHTML = '🔊 Play Audio';
    playButton.className = 'audio-play-btn';
    playButton.style.display = 'none'; // Hide initially

    // Insert the button after the audio element
    audioElement.parentNode.insertBefore(playButton, audioElement.nextSibling);

    // Create a loading indicator
    const loadingIndicator = document.createElement('div');
    loadingIndicator.innerHTML = 'Loading Audio...';
    loadingIndicator.className = 'audio-loading';
    loadingIndicator.style.display = 'block';

    // Insert the loading indicator before the audio element
    audioElement.parentNode.insertBefore(loadingIndicator, audioElement);

    // Function to attempt autoplay
    function attemptAutoplay() {
        // Hide loading indicator
        loadingIndicator.style.display = 'none';

        // Promise to attempt autoplay
        const playPromise = audioElement.play();

        // Handle the promise
        if (playPromise !== undefined) {
            playPromise.then(_ => {
                // Autoplay started successfully
                console.log('Autoplay successful');
                playButton.style.display = 'none';
                audioElement.style.display = 'block';
            })
            .catch(error => {
                // Autoplay was prevented
                console.log('Autoplay prevented:', error);
                // Show the play button since autoplay failed
                playButton.style.display = 'block';
                // Hide the audio controls until user initiates playback
                audioElement.style.display = 'none';
            });
        }
    }

    // Check if the audio is ready to play
    if (audioElement.readyState >= 2) {
        // Audio is loaded enough to play
        attemptAutoplay();
    } else {
        // Wait for audio to be loaded enough
        audioElement.addEventListener('canplay', attemptAutoplay);
    }

    // Handle click on the play button
    playButton.addEventListener('click', function() {
        audioElement.play()
            .then(() => {
                // Playback started
                playButton.style.display = 'none';
                audioElement.style.display = 'block';
            })
            .catch(error => {
                console.error('Playback failed even after user interaction:', error);
            });
    });

    // Optional: Add event for when audio finishes playing
    audioElement.addEventListener('ended', function() {
        console.log('Audio playback completed');
        // You could auto-advance to next slide here if desired
        // window.location.href = nextPageUrl;
    });

    // Optional: Add keyboard shortcut (spacebar) to play/pause
    document.addEventListener('keydown', function(event) {
        // Check if spacebar was pressed and we're not in an input field
        if (event.code === 'Space' && document.activeElement.tagName !== 'INPUT' &&
            document.activeElement.tagName !== 'TEXTAREA') {
            event.preventDefault(); // Prevent page scrolling

            if (audioElement.paused) {
                audioElement.play();
            } else {
                audioElement.pause();
            }
        }
    });
});

// Function to manually play audio from other scripts or onclick events
function playAudio() {
    const audioElement = document.getElementById('narration');
    if (audioElement) {
        audioElement.play()
            .then(() => {
                // Playback started
                const playButton = document.querySelector('.audio-play-btn');
                if (playButton) playButton.style.display = 'none';
                audioElement.style.display = 'block';
            })
            .catch(error => {
                console.error('Playback failed:', error);
            });
    }
}
