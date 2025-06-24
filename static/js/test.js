// Main game state
const gameState = {
    level: 1,
    question: 1,
    progress: {
        completed_levels: []
    },
    isLoggedIn: false
};

// Scene templates
const scenes = {
    // Home scene
    home: function() {
        return `
            <div class="home-container">
                <h1>CHESS LEARNING GAME</h1>
                <button onclick="loadScene('roadmap')">START NOW</button>
            </div>
        `;
    },

    // Roadmap scene
    roadmap: function() {
        const allCompleted = gameState.progress.completed_levels.length === 5;
        let presentHtml = '';

        if (allCompleted) {
            presentHtml = `<div class="present unlocked" onclick="loadScene('select_toy')">?</div>`;
        } else {
            presentHtml = `<div class="present locked">?</div>`;
        }

        let levelsHtml = '';
        for (let level = 5; level >= 1; level--) {
            const isUnlocked = level === 1 || gameState.progress.completed_levels.includes(level-1);
            const isCompleted = gameState.progress.completed_levels.includes(level);

            if (isCompleted) {
                levelsHtml += `<div class="level completed" onclick="loadScene('game_title', ${level})">
                    ${level}</div>`;
            } else if (isUnlocked) {
                levelsHtml += `<div class="level" onclick="loadScene('game_title', ${level})">
                    ${level}</div>`;
            } else {
                levelsHtml += `<div class="level locked">${level}</div>`;
            }
        }

        return `
            <div class="game-container">
                <div class="character">
                    <div class="character-box"></div>
                    <div class="speech">LET'S PLAY A GAME OF CHESS</div>
                </div>
                <div class="roadmap">
                    ${presentHtml}
                    ${levelsHtml}
                </div>
            </div>
            <div class="homepage-btn" onclick="loadScene('home')">homepage</div>
        `;
    },

    // Game title scene (first intro slide)
    game_title: function(level) {
        const titles = {
            1: "THE BOARD AWAKENS",
            2: "MEET THE CHESS PIECES",
            3: "SETTING UP THE ARMY",
            4: "HOW TO MOVE AND CAPTURE",
            5: "CHECK, CHECKMATE, AND STALEMATE"
        };

        return `
            <div class="intro-container">
                <h1>GAME ${level}: ${titles[level]}</h1>
                <div class="intro-content">
                    <div class="character-section">
                        <div class="character-box"></div>
                    </div>
                    <div class="board-section">
                        <div class="chess-board-placeholder"></div>
                    </div>
                </div>
                <button class="start-game-button" onclick="loadScene('intro', ${level})">
                    CONTINUE
                </button>
                <div class="homepage-btn" onclick="loadScene('home')">homepage</div>
            </div>
        `;
    },

    // Second intro slide
    intro: function(level) {
        const intros = {
            1: "HELLO, LITTLE CHESS PLAYERS! I'M YOUR GUIDE FOR TODAY, AND WE'RE ABOUT TO EXPLORE THE WORLD OF CHESS.",
            2: "NOW THAT WE KNOW THE BOARD, LET'S MEET THE STARS OF THE GAME — THE CHESS PIECES!",
            3: "NOW THAT YOU KNOW THE CHESS PIECES, IT'S TIME TO LEARN WHERE THEY STAND AT THE START OF THE GAME.",
            4: "LET'S LEARN HOW TO PLAY. EACH TURN, YOU MOVE JUST ONE PIECE — EXCEPT WHEN CASTLING (WE'LL TALK ABOUT THAT LATER).",
            5: "THE KING IS THE MOST IMPORTANT PIECE ON THE BOARD. IF YOU LOSE YOUR KING, THE GAME IS OVER. SO YOU MUST PROTECT HIM AT ALL COSTS."
        };

        return `
            <div class="intro-container">
                <div class="intro-content-text">
                    <div class="character-section">
                        <div class="character-box"></div>
                        <div class="intro-text">
                            ${intros[level]}
                        </div>
                    </div>
                    <div class="board-section">
                        <div class="chess-board-placeholder"></div>
                    </div>
                </div>
                <button class="start-game-button" onclick="loadScene('question', ${level}, 1)">
                    START GAME
                </button>
                <div class="homepage-btn" onclick="loadScene('home')">homepage</div>
            </div>
        `;
    },

    // Question scene
    question: function(level, question) {
        // This is a placeholder - you would need to add your actual questions and options
        return `
            <div class="game-container">
                <h2>Level ${level} - Question ${question}</h2>
                <div class="question-content">
                    <p>This is question ${question} of level ${level}.</p>
                    <div class="options">
                        <button onclick="checkAnswer(${level}, ${question}, 'A')">Option A</button>
                        <button onclick="checkAnswer(${level}, ${question}, 'B')">Option B</button>
                        <button onclick="checkAnswer(${level}, ${question}, 'C')">Option C</button>
                    </div>
                </div>
                <div class="homepage-btn" onclick="loadScene('home')">homepage</div>
            </div>
        `;
    },

    // Add more scenes as needed (select_toy, login, etc.)
};

// Function to load a scene
function loadScene(sceneName, param1, param2) {
    const sceneContainer = document.getElementById('current-scene');

    // Update game state based on scene
    if (sceneName === 'game_title') {
        gameState.level = param1;
    } else if (sceneName === 'question') {
        gameState.level = param1;
        gameState.question = param2;
    }

    // Render the scene template
    if (scenes[sceneName]) {
        sceneContainer.innerHTML = scenes[sceneName](param1, param2);

        // Play the appropriate audio for this scene
        playSceneAudio(sceneName, param1, param2);
    } else {
        console.error('Scene not found:', sceneName);
    }
}

// Function to play audio for a scene
function playSceneAudio(sceneName, param1, param2) {
    const audioElement = document.getElementById('narration');
    const audioSource = document.getElementById('audio-source');
    let audioPath = '';

    // Determine audio path based on scene
    if (sceneName === 'game_title') {
        audioPath = `/static/audio/${param1}/intro.mp3`;
    } else if (sceneName === 'intro') {
        audioPath = `/static/audio/${param1}/intro2.mp3`;
    } else if (sceneName === 'question') {
        audioPath = `/static/audio/${param1}/${param2}.mp3`;
    } else {
        // No audio for this scene
        return;
    }

    // Set audio source and play
    audioSource.src = audioPath;
    audioElement.load();

    // Play audio (this should work because it's triggered by user interaction)
    const playPromise = audioElement.play();

    // Handle any potential errors
    if (playPromise !== undefined) {
        playPromise.catch(error => {
            console.error('Audio play failed:', error);
        });
    }
}

// Function to check answers
function checkAnswer(level, question, selectedOption) {
    // This is where you would implement answer checking logic
    // For now, let's just move to the next question

    // If this was the last question in the level
    if (question >= 5) { // Assuming 5 questions per level
        // Mark level as completed
        if (!gameState.progress.completed_levels.includes(level)) {
            gameState.progress.completed_levels.push(level);
        }

        // Go back to roadmap
        loadScene('roadmap');
    } else {
        // Go to next question
        loadScene('question', level, question + 1);
    }
}

// Initialize the game
document.addEventListener('DOMContentLoaded', function() {
    // Start with the home screen
    loadScene('home');

    // Check login status (you would implement this)
    checkLoginStatus();
});

// Function to check login status
function checkLoginStatus() {
    // This would check cookies or localStorage for login info
    // For now, just setting a default
    gameState.isLoggedIn = false;
}
