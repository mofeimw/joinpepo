curriculums = {
    "chess": {
        "title": "Chess Curriculum",
        "lessons": [
            {
                "title": "Meet the Chess Pieces",
                "units": [
                    {
                        "lessonText": """Hello, little champions!

Welcome to your first chess lesson. Chess is a fun thinking game and is about making smart moves.""",
                        "quiz": {
                            "question": "Let me ask you something first: Do you know what this is?",
                            "options": [
                                {"text": "A. A chessboard", "correct": True},
                                {"text": "B. A square board", "correct": False},
                                {"text": "C. A Video game",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": """Let me introduce you to the stars of the chess world.
Meet the king, he wears the tall crown and comes with a cross""",
                        "quiz": {
                            "question": "Do you know what piece this is?",
                            "options": [
                                {"text": "A. Queen",  "correct": False},
                                {"text": "B. King",   "correct": True},
                                {"text": "C. Knight", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Lets meet the Queen. She wears a princess crown.",
                        "quiz": {
                            "question": "Do you know what piece this is?",
                            "options": [
                                {"text": "A. Rook",  "correct": False},
                                {"text": "B. Queen", "correct": True},
                                {"text": "C. Pawn",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Pawns are the little soldiers with the round tops.",
                        "quiz": {
                            "question": "Do you know what piece this is?",
                            "options": [
                                {"text": "A. King",  "correct": False},
                                {"text": "B. Pawn",  "correct": True},
                                {"text": "C. Queen", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Knight looks like a little horse.",
                        "quiz": {
                            "question": "What piece is this?",
                            "options": [
                                {"text": "A. Knight", "correct": True},
                                {"text": "B. Bishop", "correct": False},
                                {"text": "C. Rook",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Bishop looks like it is wearing a little hat and is tall and thin.",
                        "quiz": {
                            "question": "Do you know what piece this is?",
                            "options": [
                                {"text": "A. Bishop", "correct": True},
                                {"text": "B. Rook",   "correct": False},
                                {"text": "C. Knight", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Rook looks like a small castle and stand in the corners",
                        "quiz": {
                            "question": "Do you know what piece this is?",
                            "options": [
                                {"text": "A. Knight", "correct": False},
                                {"text": "B. Rook",   "correct": True},
                                {"text": "C. Pawn",   "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Where do the Pieces Go?",
                "units": [
                    {
                        "lessonText": """Let’s set up the board before we play.
There are two colors in chess, white and black,
One player uses white pieces and the other player uses black pieces.""",
                        "quiz": {
                            "question": "How many different colors of chess pieces are there?",
                            "options": [
                                {"text": "A. One",   "correct": False},
                                {"text": "B. Two",   "correct": True},
                                {"text": "C. Three", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Now let’s start placing the pieces. First, we place the pawns. All the pawns line up together in one row. They go on the second line of your chessboard",
                        "quiz": {
                            "question": "In what line do all the pawns line up?",
                            "options": [
                                {"text": "A. Line 1", "correct": False},
                                {"text": "B. Line 2", "correct": True},
                                {"text": "C. Line 3", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Let’s place the rooks. Each player has two rooks. The rooks go in the corners of the board.",
                        "quiz": {
                            "question": "Where does the rook go?",
                            "options": [
                                {"text": "A. Corner",            "correct": True},
                                {"text": "B. Middle",            "correct": False},
                                {"text": "C. Next to the King", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Now we place the knights. Each knight goes next to a rook. One knight stands next to the left rook. One knight stands next to the right rook.",
                        "quiz": {
                            "question": "Where does the knight go?",
                            "options": [
                                {"text": "A. Middle",             "correct": False},
                                {"text": "B. Next to the pawn",   "correct": False},
                                {"text": "C. Next to the rook",   "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Now we place the bishops. Each bishop goes next to a knight. There are two bishops, one on each side.",
                        "quiz": {
                            "question": "Where does the bishop go?",
                            "options": [
                                {"text": "A. Next to the knight", "correct": True},
                                {"text": "B. In front of the pawn", "correct": False},
                                {"text": "C. On a corner",         "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Now let’s place the queen. The queen goes in the middle. She always goes on her own color. White queen on a white square. Black queen on a black square.",
                        "quiz": {
                            "question": "Where does the queen go?",
                            "options": [
                                {"text": "A. On her own color", "correct": True},
                                {"text": "B. On a dark square", "correct": False},
                                {"text": "C. Next to a pawn",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The last piece is the king. The king always stands right next to the queen.",
                        "quiz": {
                            "question": "Where does the king go?",
                            "options": [
                                {"text": "A. In the corner",            "correct": False},
                                {"text": "B. Next to the queen",       "correct": True},
                                {"text": "C. On a black square",       "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "How to Move and Capture",
                "units": [
                    {
                        "lessonText": """Hello again, little champions!
Now that you’ve met the chessboard and the pieces, it’s time for some fun…

Today, we learn how each piece moves like a superhero on a mission

Let's start with the pawn.
It moves up only.
On its first move, it can go one up or two up. Just like in the picture below

But after that, it can only move 1 step up at a time.""",
                        "quiz": {
                            "question": "How many steps can a pawn move on its first turn?",
                            "options": [
                                {"text": "A. One",        "correct": False},
                                {"text": "B. Two",        "correct": False},
                                {"text": "C. One or Two", "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": """Now let's look at the rook. It moves in straight lines like up, down, left, or right.
And it can go as far as it wants in those directions.""",
                        "quiz": {
                            "question": "How does the rook move?",
                            "options": [
                                {"text": "A. In circles",          "correct": False},
                                {"text": "B. In straight lines",   "correct": True},
                                {"text": "C. Diagonally",          "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": """Lets talk about our little horse, the knight. Just like a horse, it can jump over others.
It moves like a letter L-shape. Two steps in one direction, then one step sideways.""",
                        "quiz": {
                            "question": "What shape does the knight move in?",
                            "options": [
                                {"text": "A. A circle",       "correct": False},
                                {"text": "B. An L-shape",     "correct": True},
                                {"text": "C. A straight line","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": """Let's talk about our friend Bishop, who always moves sideways.
It can go as far as it wants, but like a slanty line.""",
                        "quiz": {
                            "question": "How does the bishop move?",
                            "options": [
                                {"text": "A. In straight lines", "correct": False},
                                {"text": "B. Side ways",         "correct": True},
                                {"text": "C. In an L-shape",    "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": """The queen is the strongest piece on the board, and that means the queen can move wherever she wants as far as she wants. Up, down, left, right and even sideways like bishop…. but it can’t jump like a knight.""",
                        "quiz": {
                            "question": "How does the queen move?",
                            "options": [
                                {"text": "A. Up, down, left, and right", "correct": True},
                                {"text": "B. Only straight",            "correct": False},
                                {"text": "C. Only diagonal",            "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Now let's talk about the last piece is The King. The king also moves like a queen, but only he can move one square in any direction, like up, down, left, or right, and sideways",
                        "quiz": {
                            "question": "How many steps can the king move at a time?",
                            "options": [
                                {"text": "A. One",                "correct": True},
                                {"text": "B. Two",                "correct": False},
                                {"text": "C. As many as he wants", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Now it's time to learn how to play chess. First, we start off with how to capture enemy pieces. Capturing means your piece lands on a square with an enemy piece and takes its place. You then remove the enemy piece from the board.",
                        "quiz": {
                            "question": "What does it mean to capture a piece?",
                            "options": [
                                {"text": "A. Take the enemy piece off the board", "correct": True},
                                {"text": "B. Say hello to it",                    "correct": False},
                                {"text": "C. Jump over it and keep going",        "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Every piece captures the same way it moves. A rook captures in straight lines. A bishop captures diagonally. A knight jumps to capture!",
                        "quiz": {
                            "question": "How does a rook capture?",
                            "options": [
                                {"text": "A. In a circle",      "correct": False},
                                {"text": "B. Diagonally",       "correct": False},
                                {"text": "C. In straight lines","correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Every piece captures the same way it moves. A rook captures in straight lines. A bishop captures diagonally. A knight jumps to capture!",
                        "quiz": {
                            "question": "How does a Knight capture?",
                            "options": [
                                {"text": "A. Jumps",              "correct": True},
                                {"text": "B. Diagonally",         "correct": False},
                                {"text": "C. In straight lines",  "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Setting Up the Board",
                "units": [
                    {
                        "lessonText": "Place the board so that a white square is in each player’s right-hand corner.",
                        "quiz": {
                            "question": "Which corner should be white?",
                            "options": [
                                {"text": "A. Left corner", "correct": False},
                                {"text": "B. Right corner","correct": True},
                                {"text": "C. Any corner",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "On the back row the order is Rook, Knight, Bishop, Queen, King, and our second Bishop, our second Knight and our second Rook.",
                        "quiz": {
                            "question": "What sits between the two Knights?",
                            "options": [
                                {"text": "A. A Bishop",                "correct": False},
                                {"text": "B. The Queen and the King","correct": True},
                                {"text": "C. Two Pawns",              "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Queen always starts on her own color. White Queen on white. Black Queen on black.",
                        "quiz": {
                            "question": "Where does the White Queen begin?",
                            "options": [
                                {"text": "A. A dark square",                     "correct": False},
                                {"text": "B. A white square",                    "correct": True},
                                {"text": "C. Any square next to the King",       "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "All eight Pawns stand in a straight line in front of the other pieces.",
                        "quiz": {
                            "question": "How many white Pawns begin the game?",
                            "options": [
                                {"text": "A. Six",  "correct": False},
                                {"text": "B. Eight","correct": True},
                                {"text": "C. Ten",  "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Special Rules",
                "units": [
                    {
                        "lessonText": "Castling is a team move. The King steps two squares toward a Rook, and the Rook hops next to the King. Both pieces must be unmoved, and nothing sits between them.",
                        "quiz": {
                            "question": "When are you allowed to castle?",
                            "options": [
                                {"text": "A. After the King has moved once",                              "correct": False},
                                {"text": "B. When pieces sit between the King and the Rook",         "correct": False},
                                {"text": "C. When both King and Rook have never moved, and the path is clear","correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Pawn Promotion is a reward. When a Pawn reaches the other side, it can become a Queen, Rook, Bishop, or Knight.",
                        "quiz": {
                            "question": "Which piece can a Pawn NOT turn into?",
                            "options": [
                                {"text": "A. Queen", "correct": False},
                                {"text": "B. Knight","correct": False},
                                {"text": "C. King",  "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "En Passant is a sneaky pawn capture. If an enemy Pawn dashes two squares and lands beside your Pawn, you may capture it as if it moved only one square. You must do this right away.",
                        "quiz": {
                            "question": "When can you use En Passant?",
                            "options": [
                                {"text": "A. Any time after the double step", "correct": False},
                                {"text": "B. Only on your very next move",   "correct": True},
                                {"text": "C. Only with Knights",             "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Check, Checkmate, and Good Sportsmanship",
                "units": [
                    {
                        "lessonText": "Check means your King is under attack. You must move the block or capture to escape.",
                        "quiz": {
                            "question": "If your King is in check, you may…",
                            "options": [
                                {"text": "A. Ignore it",     "correct": False},
                                {"text": "B. Move the block or capture the attacker", "correct": True},
                                {"text": "C. Move any random piece",                "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Checkmate means the King is in check and cannot escape. The game ends right away.",
                        "quiz": {
                            "question": "What does Checkmate mean?",
                            "options": [
                                {"text": "A. A tie",              "correct": False},
                                {"text": "B. The game continues", "correct": False},
                                {"text": "C. The King has no safe move", "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Stalemate means it is your turn and you have no legal move but you are not in check. The result is a draw.",
                        "quiz": {
                            "question": "Stalemate results in…",
                            "options": [
                                {"text": "A. A win for White", "correct": False},
                                {"text": "B. A draw",        "correct": True},
                                {"text": "C. A win for Black","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Good sports always shake hands and say good game after the last move.",
                        "quiz": {
                            "question": "Why shake hands after a game?",
                            "options": [
                                {"text": "A. To show respect",      "correct": True},
                                {"text": "B. To scare your opponent","correct": False},
                                {"text": "C. To restart the clock", "correct": False}
                            ]
                        }
                    }
                ]
            }
        ]
    },
    "space": {
        "title": "Space Curriculum",
        "lessons": [
            {
                "title": "Intro to Space",
                "units": [
                    {
                        "lessonText": "The Sun is a giant glowing star in the middle of our solar system.",
                        "quiz": {
                            "question": "What is the Sun?",
                            "options": [
                                {"text": "A. A planet",   "correct": False},
                                {"text": "B. A star",     "correct": True},
                                {"text": "C. A moon",     "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Sun gives Earth light and warmth. Without it we would be chilly and dark.",
                        "quiz": {
                            "question": "What does the Sun give us?",
                            "options": [
                                {"text": "A. Ice",             "correct": False},
                                {"text": "B. Light and heat", "correct": True},
                                {"text": "C. Rain",            "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Moon is a big, round rock that travels around Earth.",
                        "quiz": {
                            "question": "What does the Moon orbit?",
                            "options": [
                                {"text": "A. Mars",     "correct": False},
                                {"text": "B. The Sun",  "correct": False},
                                {"text": "C. Earth",    "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Moon shines because it reflects the Sun’s light.",
                        "quiz": {
                            "question": "Why can we see the Moon shine?",
                            "options": [
                                {"text": "A. It has its own light", "correct": False},
                                {"text": "B. It reflects sunlight", "correct": True},
                                {"text": "C. It is made of cheese", "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Day and Night Spin",
                "units": [
                    {
                        "lessonText": "Earth spins like a top. One full turn every 24 hours is called a rotation.",
                        "quiz": {
                            "question": "What do we call Earth’s spin?",
                            "options": [
                                {"text": "A. Rotation",  "correct": True},
                                {"text": "B. Vacation",  "correct": False},
                                {"text": "C. Explosion", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "When your side of Earth faces the Sun it is day.",
                        "quiz": {
                            "question": "What makes daytime?",
                            "options": [
                                {"text": "A. Clouds",        "correct": False},
                                {"text": "B. Facing the Sun","correct": True},
                                {"text": "C. Moonlight",     "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "When your side turns away from the Sun it is night.",
                        "quiz": {
                            "question": "Why is it night?",
                            "options": [
                                {"text": "A. We face away from the Sun", "correct": True},
                                {"text": "B. The Sun turns off",         "correct": False},
                                {"text": "C. Stars block the light",      "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Sunrise happens when Earth turns and the Sun peeks over the horizon.",
                        "quiz": {
                            "question": "What is sunrise?",
                            "options": [
                                {"text": "A. The Sun moving closer",              "correct": False},
                                {"text": "B. Earth turning to face the Sun",       "correct": True},
                                {"text": "C. A giant flashlight",                 "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Rocky Planet Parade 🪨🪐",
                "units": [
                    {
                        "lessonText": "Mercury is the closest planet to the Sun. It is small hot and speedy.",
                        "quiz": {
                            "question": "Which planet orbits closest to the Sun?",
                            "options": [
                                {"text": "A. Mercury", "correct": True},
                                {"text": "B. Earth",   "correct": False},
                                {"text": "C. Neptune", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Venus is Earth’s neighbor and is covered by thick hot clouds.",
                        "quiz": {
                            "question": "Which planet has thick super-hot clouds?",
                            "options": [
                                {"text": "A. Venus",  "correct": True},
                                {"text": "B. Mars",   "correct": False},
                                {"text": "C. Jupiter","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Earth is the only planet we know with liquid water and plenty of life.",
                        "quiz": {
                            "question": "What makes Earth special?",
                            "options": [
                                {"text": "A. It is purple",               "correct": False},
                                {"text": "B. It has water and life",    "correct": True},
                                {"text": "C. It is the biggest planet", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Mars is called the Red Planet because of its rusty soil.",
                        "quiz": {
                            "question": "Why does Mars look red?",
                            "options": [
                                {"text": "A. Red flowers grow there", "correct": False},
                                {"text": "B. Rusty soil",             "correct": True},
                                {"text": "C. It is on fire",          "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Giant Planet Adventure 🌬️💫",
                "units": [
                    {
                        "lessonText": "Jupiter is the largest planet and has a huge storm called the Great Red Spot.",
                        "quiz": {
                            "question": "Which planet has the Great Red Spot?",
                            "options": [
                                {"text": "A. Saturn", "correct": False},
                                {"text": "B. Jupiter","correct": True},
                                {"text": "C. Uranus", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Saturn is famous for bright rings made of ice and rock.",
                        "quiz": {
                            "question": "What makes Saturn easy to spot?",
                            "options": [
                                {"text": "A. Bright rings", "correct": True},
                                {"text": "B. Green oceans", "correct": False},
                                {"text": "C. A big hat",    "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Uranus spins on its side like a rolling ball.",
                        "quiz": {
                            "question": "Which planet rolls on its side?",
                            "options": [
                                {"text": "A. Neptune","correct": False},
                                {"text": "B. Uranus", "correct": True},
                                {"text": "C. Mercury","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Neptune is deep blue and has very strong winds.",
                        "quiz": {
                            "question": "Which planet is known for super-fast winds?",
                            "options": [
                                {"text": "A. Mars",    "correct": False},
                                {"text": "B. Neptune","correct": True},
                                {"text": "C. Venus",  "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Shooting Stars and Rockets 🚀🌠",
                "units": [
                    {
                        "lessonText": "A meteor is a space rock that burns bright as it zips through the sky. People call it a shooting star.",
                        "quiz": {
                            "question": "What do we often call a meteor in the sky?",
                            "options": [
                                {"text": "A. Shooting star","correct": True},
                                {"text": "B. Flying fish",   "correct": False},
                                {"text": "C. Moon pebble",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Astronauts ride rockets to leave Earth’s gravity and explore space.",
                        "quiz": {
                            "question": "What vehicle blasts astronauts into space?",
                            "options": [
                                {"text": "A. Submarine","correct": False},
                                {"text": "B. Rocket",   "correct": True},
                                {"text": "C. Bicycle",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Space suits give astronauts air to breathe and keep them safe in the vacuum of space.",
                        "quiz": {
                            "question": "Why do astronauts wear space suits?",
                            "options": [
                                {"text": "A. For style",              "correct": False},
                                {"text": "B. To breathe and stay safe","correct": True},
                                {"text": "C. To keep snacks handy",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Telescopes help us see far-away stars and galaxies.",
                        "quiz": {
                            "question": "What tool lets us see distant space objects?",
                            "options": [
                                {"text": "A. Microscope", "correct": False},
                                {"text": "B. Telescope",  "correct": True},
                                {"text": "C. Paintbrush", "correct": False}
                            ]
                        }
                    }
                ]
            }
        ]
    },
    "science": {
        "title": "Science Curriculum",
        "lessons": [
            {
                "title": "What Is Matter 🔎",
                "units": [
                    {
                        "lessonText": "Matter is anything you can touch, see, smell, or taste.",
                        "quiz": {
                            "question": "What word means anything you can touch or see",
                            "options": [
                                {"text": "A. Music", "correct": False},
                                {"text": "B. Matter", "correct": True},
                                {"text": "C. Magic",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Matter has mass. Mass means it weighs something.",
                        "quiz": {
                            "question": "If something has mass is it matter",
                            "options": [
                                {"text": "A. Yes",   "correct": True},
                                {"text": "B. No",    "correct": False},
                                {"text": "C. Maybe", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Matter takes up space even if you cannot see it. Scientists call that space volume.",
                        "quiz": {
                            "question": "Does air take up space",
                            "options": [
                                {"text": "A. Yes",            "correct": True},
                                {"text": "B. No",             "correct": False},
                                {"text": "C. Only on windy days", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "There are 3 everyday states of matter. They are solids liquids and gases.",
                        "quiz": {
                            "question": "Which is not one of the 3 common states of matter",
                            "options": [
                                {"text": "A. Solid",  "correct": False},
                                {"text": "B. Liquid", "correct": False},
                                {"text": "C. Music",  "correct": True}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Super Solids 🧱",
                "units": [
                    {
                        "lessonText": "A solid keeps its own shape like a rock or a wooden block.",
                        "quiz": {
                            "question": "Which item keeps the same shape by itself",
                            "options": [
                                {"text": "A. Water", "correct": False},
                                {"text": "B. Rock",  "correct": True},
                                {"text": "C. Juice", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Particles in solids are packed very tightly and hardly move.",
                        "quiz": {
                            "question": "Are solid particles close together",
                            "options": [
                                {"text": "A. Yes",        "correct": True},
                                {"text": "B. No",         "correct": False},
                                {"text": "C. Only at night", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Some solids feel hard like stone and some feel soft like clay.",
                        "quiz": {
                            "question": "Is clay a hard or soft solid",
                            "options": [
                                {"text": "A. Hard",        "correct": False},
                                {"text": "B. Soft",        "correct": True},
                                {"text": "C. Both at once","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "If you cut a solid each piece is still a solid and still keeps its shape.",
                        "quiz": {
                            "question": "After cutting a chocolate bar the pieces are still",
                            "options": [
                                {"text": "A. Liquids", "correct": False},
                                {"text": "B. Solids",  "correct": True},
                                {"text": "C. Gases",   "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Lively Liquids 💧",
                "units": [
                    {
                        "lessonText": "A liquid takes the shape of its container. Milk becomes bowl shaped in a bowl.",
                        "quiz": {
                            "question": "Milk in a bowl is a",
                            "options": [
                                {"text": "A. Solid", "correct": False},
                                {"text": "B. Liquid","correct": True},
                                {"text": "C. Gas",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Liquids can flow and you can pour them from one cup to another.",
                        "quiz": {
                            "question": "Can you pour a liquid",
                            "options": [
                                {"text": "A. Yes",       "correct": True},
                                {"text": "B. No",        "correct": False},
                                {"text": "C. Only water","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Liquids have a top surface that stays level and flat.",
                        "quiz": {
                            "question": "What part of juice stays flat in a cup",
                            "options": [
                                {"text": "A. Bottom",       "correct": False},
                                {"text": "B. Top surface",  "correct": True},
                                {"text": "C. Middle bubbles","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Liquid particles touch each other but they can slide around easily.",
                        "quiz": {
                            "question": "Do liquid particles slide past one another",
                            "options": [
                                {"text": "A. Yes",              "correct": True},
                                {"text": "B. No",               "correct": False},
                                {"text": "C. Only in hot weather","correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Giggly Gases 🌬️",
                "units": [
                    {
                        "lessonText": "A gas spreads out to fill any space. Air fills every corner of a balloon.",
                        "quiz": {
                            "question": "What happens to air in a balloon",
                            "options": [
                                {"text": "A. Fills the balloon", "correct": True},
                                {"text": "B. Stays in one corner","correct": False},
                                {"text": "C. Sinks to the bottom","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Gases can be squeezed into tanks. Scientists say the gas is compressed.",
                        "quiz": {
                            "question": "Can air be squished into a tank",
                            "options": [
                                {"text": "A. Yes",         "correct": True},
                                {"text": "B. No",          "correct": False},
                                {"text": "C. Only helium","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Many gases are invisible. You breathe oxygen even though you cannot see it.",
                        "quiz": {
                            "question": "Can you usually see oxygen gas",
                            "options": [
                                {"text": "A. Yes",             "correct": False},
                                {"text": "B. No",              "correct": True},
                                {"text": "C. Only with goggles","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Gas particles are far apart and zoom around very quickly.",
                        "quiz": {
                            "question": "Are gas particles close together or far apart",
                            "options": [
                                {"text": "A. Close",     "correct": False},
                                {"text": "B. Far apart", "correct": True},
                                {"text": "C. They do not move", "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Changing States 🔄",
                "units": [
                    {
                        "lessonText": "Melting happens when a solid warms up and turns into a liquid. Ice becomes water.",
                        "quiz": {
                            "question": "When ice cream melts it becomes a",
                            "options": [
                                {"text": "A. Gas",    "correct": False},
                                {"text": "B. Liquid","correct": True},
                                {"text": "C. Rock",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Freezing happens when a liquid cools down and turns into a solid. Water becomes ice.",
                        "quiz": {
                            "question": "What word do we use for water that turned solid",
                            "options": [
                                {"text": "A. Steam", "correct": False},
                                {"text": "B. Ice",   "correct": True},
                                {"text": "C. Milk",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Evaporation happens when a liquid warms up and turns into a gas. Puddles disappear on a sunny day.",
                        "quiz": {
                            "question": "When water on the sidewalk disappears it has",
                            "options": [
                                {"text": "A. Melted",     "correct": False},
                                {"text": "B. Evaporated","correct": True},
                                {"text": "C. Frozen",    "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Condensation happens when a gas cools down and turns back into a liquid. Steam can change into tiny water drops.",
                        "quiz": {
                            "question": "Water drops on a cold soda can come from",
                            "options": [
                                {"text": "A. Condensation","correct": True},
                                {"text": "B. Freezing",    "correct": False},
                                {"text": "C. Melting",     "correct": False}
                            ]
                        }
                    }
                ]
            }
        ]
    },
    "biology": {
        "title": "Biology Curriculum",
        "lessons": [
            {
                "title": "What Is Biology?",
                "units": [
                    {
                        "lessonText": "Biology is the science of living things. That means people, animals, plants, and even tiny bugs!",
                        "quiz": {
                            "question": "What does biology study?",
                            "options": [
                                {"text": "A. Living things", "correct": True},
                                {"text": "B. Toys",          "correct": False},
                                {"text": "C. Rocks",         "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "If something can eat, grow, breathe, or move on its own, it’s alive.",
                        "quiz": {
                            "question": "What can living things do?",
                            "options": [
                                {"text": "A. Fly always",       "correct": False},
                                {"text": "B. Glow in the dark", "correct": False},
                                {"text": "C. Eat and grow",     "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Biologists are scientists who explore how living things work.",
                        "quiz": {
                            "question": "Who studies living things?",
                            "options": [
                                {"text": "A. Astronauts",   "correct": False},
                                {"text": "B. Biologists",   "correct": True},
                                {"text": "C. Detectives",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Learning biology helps us understand our body and the world around us.",
                        "quiz": {
                            "question": "Why is biology helpful?",
                            "options": [
                                {"text": "A. It helps us sleep",                "correct": False},
                                {"text": "B. It teaches us magic",              "correct": False},
                                {"text": "C. It helps us know our body",        "correct": True}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Meet Your Body!",
                "units": [
                    {
                        "lessonText": "Your body has many parts that work together like a team.",
                        "quiz": {
                            "question": "What does your body act like?",
                            "options": [
                                {"text": "A. A team",     "correct": True},
                                {"text": "B. A puzzle",   "correct": False},
                                {"text": "C. A robot",    "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Your skeleton is made of bones that hold you up and keep you strong.",
                        "quiz": {
                            "question": "What holds you up?",
                            "options": [
                                {"text": "A. Muscles", "correct": False},
                                {"text": "B. Bones",   "correct": True},
                                {"text": "C. String",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Muscles help you move, run, jump, and hug your friends.",
                        "quiz": {
                            "question": "What do muscles help you do?",
                            "options": [
                                {"text": "A. Read",  "correct": False},
                                {"text": "B. Think", "correct": False},
                                {"text": "C. Move",  "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Your skin covers your body and keeps it safe from germs.",
                        "quiz": {
                            "question": "What keeps germs out?",
                            "options": [
                                {"text": "A. Hair",  "correct": False},
                                {"text": "B. Skin",  "correct": True},
                                {"text": "C. Socks", "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "How We Breathe and Eat",
                "units": [
                    {
                        "lessonText": "Your lungs help you breathe in air and give your body oxygen.",
                        "quiz": {
                            "question": "What do lungs help you do?",
                            "options": [
                                {"text": "A. Eat",     "correct": False},
                                {"text": "B. Breathe", "correct": True},
                                {"text": "C. Dance",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Your heart pumps blood that carries oxygen all around your body.",
                        "quiz": {
                            "question": "What does your heart pump?",
                            "options": [
                                {"text": "A. Water", "correct": False},
                                {"text": "B. Food",  "correct": False},
                                {"text": "C. Blood", "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Your stomach helps break down food to give you energy.",
                        "quiz": {
                            "question": "Where does food get broken down?",
                            "options": [
                                {"text": "A. Feet",    "correct": False},
                                {"text": "B. Stomach","correct": True},
                                {"text": "C. Brain",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Eating healthy foods like fruits and veggies helps your body grow.",
                        "quiz": {
                            "question": "What helps your body grow?",
                            "options": [
                                {"text": "A. Candy",            "correct": False},
                                {"text": "B. Chips",            "correct": False},
                                {"text": "C. Fruits and veggies","correct": True}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "The Five Senses",
                "units": [
                    {
                        "lessonText": "You use your eyes to see colors, shapes, and light.",
                        "quiz": {
                            "question": "What do you use to see?",
                            "options": [
                                {"text": "A. Nose", "correct": False},
                                {"text": "B. Eyes", "correct": True},
                                {"text": "C. Hands","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Your ears help you hear sounds like music and voices.",
                        "quiz": {
                            "question": "What do ears help you do?",
                            "options": [
                                {"text": "A. Smell", "correct": False},
                                {"text": "B. Hear",  "correct": True},
                                {"text": "C. Touch","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Your nose smells yummy food or stinky socks!",
                        "quiz": {
                            "question": "What do you smell with?",
                            "options": [
                                {"text": "A. Eyes",  "correct": False},
                                {"text": "B. Mouth", "correct": False},
                                {"text": "C. Nose",  "correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Your skin feels if something is hot, cold, soft, or rough.",
                        "quiz": {
                            "question": "How do you feel about things?",
                            "options": [
                                {"text": "A. Skin",  "correct": True},
                                {"text": "B. Teeth", "correct": False},
                                {"text": "C. Eyes",  "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Stay Healthy and Strong",
                "units": [
                    {
                        "lessonText": "Sleeping at night gives your body time to rest and grow.",
                        "quiz": {
                            "question": "Why do we sleep?",
                            "options": [
                                {"text": "A. To be bored",       "correct": False},
                                {"text": "B. To grow and rest", "correct": True},
                                {"text": "C. To watch TV",      "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Drinking water keeps your body cool and your brain happy.",
                        "quiz": {
                            "question": "What keeps your brain happy?",
                            "options": [
                                {"text": "A. Water",    "correct": True},
                                {"text": "B. Soda",     "correct": False},
                                {"text": "C. Ice cream","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Washing your hands keeps away germs and sickness.",
                        "quiz": {
                            "question": "How do you keep germs away?",
                            "options": [
                                {"text": "A. Jumping",     "correct": False},
                                {"text": "B. Sleeping",    "correct": False},
                                {"text": "C. Washing hands","correct": True}
                            ]
                        }
                    },
                    {
                        "lessonText": "Moving your body by running or dancing makes you strong and fast.",
                        "quiz": {
                            "question": "What helps you get strong?",
                            "options": [
                                {"text": "A. Drawing", "correct": False},
                                {"text": "B. Moving",  "correct": True},
                                {"text": "C. Sitting", "correct": False}
                            ]
                        }
                    }
                ]
            }
        ]
    },
    "geography": {
        "title": "Geography Curriculum",
        "lessons": [
            {
                "title": "Intro to Geography",
                "units": [
                    {
                        "lessonText": "Geography is the study of Earth, its land, water, weather, and people!",
                        "quiz": {
                            "question": "What does geography study?",
                            "options": [
                                {"text": "A. Earth and people", "correct": True},
                                {"text": "B. Video games",      "correct": False},
                                {"text": "C. Candy",            "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Maps help geographers find where places are. A map is like a treasure guide!",
                        "quiz": {
                            "question": "What tool shows where places are?",
                            "options": [
                                {"text": "A. Flashlight", "correct": False},
                                {"text": "B. Map",        "correct": True},
                                {"text": "C. Spoon",      "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Some places are hot and sunny, while others are cold and snowy. That’s part of geography too!",
                        "quiz": {
                            "question": "Which of these is part of geography?",
                            "options": [
                                {"text": "A. Weather",        "correct": True},
                                {"text": "B. Pizza toppings","correct": False},
                                {"text": "C. Magic tricks",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "We all live somewhere on Earth. Learning geography helps you understand the world around you!",
                        "quiz": {
                            "question": "Why should we learn geography?",
                            "options": [
                                {"text": "A. To know more about the world", "correct": True},
                                {"text": "B. To eat more snacks",          "correct": False},
                                {"text": "C. To jump higher",              "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Land and Water 🌊⛰️",
                "units": [
                    {
                        "lessonText": "Our Earth has big oceans full of water and large pieces of land called continents.",
                        "quiz": {
                            "question": "What do we call the big water areas on Earth?",
                            "options": [
                                {"text": "A. Oceans",    "correct": True},
                                {"text": "B. Parks",     "correct": False},
                                {"text": "C. Ice cream", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "There are 7 continents on Earth. That’s like 7 huge land puzzles!",
                        "quiz": {
                            "question": "How many continents are there?",
                            "options": [
                                {"text": "A. 7",  "correct": True},
                                {"text": "B. 3",  "correct": False},
                                {"text": "C. 12", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Rivers are like watery roads that move through land. Lakes are water that stays in one spot.",
                        "quiz": {
                            "question": "What moves like a road through land?",
                            "options": [
                                {"text": "A. River",  "correct": True},
                                {"text": "B. Balloon","correct": False},
                                {"text": "C. Hill",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Mountains are tall, rocky land that reaches up high into the sky!",
                        "quiz": {
                            "question": "What is very tall and rocky?",
                            "options": [
                                {"text": "A. Mountain", "correct": True},
                                {"text": "B. Beach",    "correct": False},
                                {"text": "C. Bowl",     "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Weather and Climate ☀️❄️",
                "units": [
                    {
                        "lessonText": "Weather changes every day; it could be sunny, rainy, or windy.",
                        "quiz": {
                            "question": "What changes every day?",
                            "options": [
                                {"text": "A. Weather", "correct": True},
                                {"text": "B. Homework","correct": False},
                                {"text": "C. Cookies", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Climate is what the weather is like in one place most of the time.",
                        "quiz": {
                            "question": "What tells us the usual weather in a place?",
                            "options": [
                                {"text": "A. Climate","correct": True},
                                {"text": "B. Clock",  "correct": False},
                                {"text": "C. Shoes",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Some places are always hot and dry like deserts. Others are cold and snowy like the Arctic.",
                        "quiz": {
                            "question": "Which place is hot and dry?",
                            "options": [
                                {"text": "A. Desert",     "correct": True},
                                {"text": "B. Ocean",      "correct": False},
                                {"text": "C. Playground","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Geographers study weather and climate to help people stay safe and grow food.",
                        "quiz": {
                            "question": "Why do geographers study weather?",
                            "options": [
                                {"text": "A. To keep people safe","correct": True},
                                {"text": "B. To sing songs",      "correct": False},
                                {"text": "C. To ride scooters",   "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "The 7 Continents 🌎",
                "units": [
                    {
                        "lessonText": "Let's talk about the continents again. Remember, continents are big land on Earth divided all over the globe.",
                        "quiz": {
                            "question": "What are the big land areas on Earth called?",
                            "options": [
                                {"text": "A. Continents","correct": True},
                                {"text": "B. Cookies",   "correct": False},
                                {"text": "C. Clouds",    "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The 7 continents are: Asia, Africa, North America, South America, Antarctica, Europe, and Australia.",
                        "quiz": {
                            "question": "Which of these is a continent?",
                            "options": [
                                {"text": "A. Africa",    "correct": True},
                                {"text": "B. Chocolate", "correct": False},
                                {"text": "C. Backyard",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Asia is the biggest continent. Australia is the smallest!",
                        "quiz": {
                            "question": "Which continent is the smallest?",
                            "options": [
                                {"text": "A. Australia","correct": True},
                                {"text": "B. Asia",     "correct": False},
                                {"text": "C. Africa",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Each continent has its own people, animals, weather, and fun places to explore.",
                        "quiz": {
                            "question": "What makes each continent special?",
                            "options": [
                                {"text": "A. People and animals","correct": True},
                                {"text": "B. Toys and games",      "correct": False},
                                {"text": "C. Shoes and socks",    "correct": False}
                            ]
                        }
                    }
                ]
            }
        ]
    },
    "history": {
        "title": "History Curriculum",
        "lessons": [
            {
                "title": "First People",
                "units": [
                    {
                        "lessonText": "Long ago, the land was home to Native American families.",
                        "quiz": {
                            "question": "Who lived here first?",
                            "options": [
                                {"text": "A. Native Americans", "correct": True},
                                {"text": "B. Pilgrims",          "correct": False},
                                {"text": "C. Robots",            "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Each tribe had its own homes, clothes, and games.",
                        "quiz": {
                            "question": "Did every tribe live the same way?",
                            "options": [
                                {"text": "A. Yes all the same",       "correct": False},
                                {"text": "B. No each was different",   "correct": True},
                                {"text": "C. They had spaceships",     "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Many tribes grew corn and shared it at mealtimes.",
                        "quiz": {
                            "question": "Which picture shows corn?",
                            "options": [
                                {"text": "A. Corn",   "correct": True},
                                {"text": "B. Pizza",  "correct": False},
                                {"text": "C. Donuts", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "They thanked nature and took only what they needed.",
                        "quiz": {
                            "question": "How did Native Americans treat nature?",
                            "options": [
                                {"text": "A. Threw trash",     "correct": False},
                                {"text": "B. Respected nature", "correct": True},
                                {"text": "C. Cut every tree",   "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Pilgrims and Colonies",
                "units": [
                    {
                        "lessonText": "About 400 years ago, Pilgrims sailed on a ship named Mayflower.",
                        "quiz": {
                            "question": "What was the Pilgrims' ship named?",
                            "options": [
                                {"text": "A. Mayflower", "correct": True},
                                {"text": "B. Starship",  "correct": False},
                                {"text": "C. Speedboat","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Pilgrims and Native friends shared a big meal called Thanksgiving.",
                        "quiz": {
                            "question": "Which holiday remembers that meal?",
                            "options": [
                                {"text": "A. Thanksgiving", "correct": True},
                                {"text": "B. Halloween",    "correct": False},
                                {"text": "C. Flag Day",     "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Soon 13 little colonies lined the east coast.",
                        "quiz": {
                            "question": "How many colonies were there?",
                            "options": [
                                {"text": "A. 13", "correct": True},
                                {"text": "B. 3",  "correct": False},
                                {"text": "C. 100","correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The King of Britain made the rules for those colonies.",
                        "quiz": {
                            "question": "Who was the boss of the colonies then?",
                            "options": [
                                {"text": "A. King of Britain",   "correct": True},
                                {"text": "B. President Lincoln", "correct": False},
                                {"text": "C. Santa",             "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "America Says We Are Free",
                "units": [
                    {
                        "lessonText": "Colonists grew angry about paying unfair taxes.",
                        "quiz": {
                            "question": "What upset the colonists?",
                            "options": [
                                {"text": "A. Unfair taxes", "correct": True},
                                {"text": "B. Too many toys","correct": False},
                                {"text": "C. No snow",      "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "On July 4, 1776, leaders signed the Declaration of Independence.",
                        "quiz": {
                            "question": "What is another name for July 4?",
                            "options": [
                                {"text": "A. Independence Day", "correct": True},
                                {"text": "B. Pizza Day",        "correct": False},
                                {"text": "C. Monday",           "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "George Washington led the soldiers who fought for freedom.",
                        "quiz": {
                            "question": "Who was the main general?",
                            "options": [
                                {"text": "A. George Washington", "correct": True},
                                {"text": "B. Abraham Lincoln",   "correct": False},
                                {"text": "C. Spider-Man",        "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "After the victory, the colonies became the United States.",
                        "quiz": {
                            "question": "What country was born?",
                            "options": [
                                {"text": "A. United States",          "correct": True},
                                {"text": "B. United Kingdom",         "correct": False},
                                {"text": "C. United Dinosaurs",       "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "North and South Split",
                "units": [
                    {
                        "lessonText": "Many years later, the North and South argued about slavery.",
                        "quiz": {
                            "question": "What big issue split them?",
                            "options": [
                                {"text": "A. Slavery",         "correct": True},
                                {"text": "B. Ice cream flavors","correct": False},
                                {"text": "C. Music style",     "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The fight turned into a war called the Civil War.",
                        "quiz": {
                            "question": "What was the war called?",
                            "options": [
                                {"text": "A. Civil War",     "correct": True},
                                {"text": "B. Military Fight","correct": False},
                                {"text": "C. Cookie Battle", "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "Abraham Lincoln was the President and wanted the country to stay together.",
                        "quiz": {
                            "question": "Who was the President then?",
                            "options": [
                                {"text": "A. Abraham Lincoln",   "correct": True},
                                {"text": "B. George Washington", "correct": False},
                                {"text": "C. Iron Man",           "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The North won. Slavery ended, and the states stayed united.",
                        "quiz": {
                            "question": "What happened after the war?",
                            "options": [
                                {"text": "A. Slavery ended and states united", "correct": True},
                                {"text": "B. Slavery stayed",                  "correct": False},
                                {"text": "C. Dinosaurs returned",             "correct": False}
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Symbols of America",
                "units": [
                    {
                        "lessonText": "The flag has 50 stars. Each star stands for 1 state.",
                        "quiz": {
                            "question": "The stars stand for",
                            "options": [
                                {"text": "A. States",    "correct": True},
                                {"text": "B. Presidents","correct": False},
                                {"text": "C. Planets",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Bald Eagle is the national bird and shows strength.",
                        "quiz": {
                            "question": "What does the Bald Eagle represent?",
                            "options": [
                                {"text": "A. Strength",   "correct": True},
                                {"text": "B. Money",      "correct": False},
                                {"text": "C. Education",  "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Statue of Liberty welcomes visitors to New York Harbor.",
                        "quiz": {
                            "question": "Where is the Statue of Liberty?",
                            "options": [
                                {"text": "A. New York Harbor", "correct": True},
                                {"text": "B. Grand Canyon",    "correct": False},
                                {"text": "C. Mount Everest",   "correct": False}
                            ]
                        }
                    },
                    {
                        "lessonText": "The Constitution is our big rulebook and protects rights like free speech.",
                        "quiz": {
                            "question": "Which paper protects free speech?",
                            "options": [
                                {"text": "A. Constitution",   "correct": True},
                                {"text": "B. Cookbook",       "correct": False},
                                {"text": "C. Phone manual",   "correct": False}
                            ]
                        }
                    }
                ]
            }
        ]
    }
}



import os
import requests

# ─── Configuration ────────────────────────────────────────────────────────────
API_KEY = "sk_fcd065b9a90e7a08380364df0d3ebb4b6d3e8d71652b71b2"
VOICE_ID = "jBpfuIE2acCO8z3wKNLl"  # replace with your chosen voice ID

# ─── Eleven Labs TTS helper ────────────────────────────────────────────────────
def synthesize_and_save(text: str, path: str):
    """
    Call Eleven Labs TTS on `text` and write the resulting MP3 to `path`.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }

    resp = requests.post(url, json=payload, headers=headers)
    if resp.status_code != 200:
        print(f"❌ Error {resp.status_code} for text: {text[:30]}…")
        print(resp.json())
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(resp.content)
    print(f"✅ Wrote {path}")

# ─── Main processing ──────────────────────────────────────────────────────────
def generate_all_audio(curriculums: dict):
    for curriculum_key, curriculum in curriculums.items():
        base_dir = os.path.join('.', curriculum_key)
        for lesson_idx, lesson in enumerate(curriculum['lessons'], start=1):
            lesson_dir = os.path.join(base_dir, str(lesson_idx))
            for unit_idx, unit in enumerate(lesson['units'], start=1):
                # 1) lesson text
                out_lesson = os.path.join(lesson_dir, f"unit{unit_idx}_lesson.mp3")
                if os.path.exists(out_lesson):
                    print(f"⏭️ Skip {out_lesson}, already exists")
                else:
                    synthesize_and_save(unit['lessonText'], out_lesson)

                # 2) quiz question
                out_q = os.path.join(lesson_dir, f"unit{unit_idx}_question.mp3")
                if os.path.exists(out_q):
                    print(f"⏭️ Skip {out_q}, already exists")
                else:
                    synthesize_and_save(unit['quiz']['question'], out_q)

                # 3) each answer option, numbered 1,2,3…
                for opt_idx, option in enumerate(unit['quiz']['options'], start=1):
                    out_opt = os.path.join(lesson_dir, f"unit{unit_idx}_option{opt_idx}.mp3")
                    if os.path.exists(out_opt):
                        print(f"⏭️ Skip {out_opt}, already exists")
                    else:
                        synthesize_and_save(option['text'], out_opt)

if __name__ == "__main__":
    # assume `curriculums` is already defined or imported
    generate_all_audio(curriculums)
