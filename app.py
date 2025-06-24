from bottle import Bottle, route, run, template, request, redirect, response, static_file, HTTPResponse
import sqlite3
import hashlib
import os
import json
from functools import wraps
import stripe

# Initialize the app
app = Bottle()

# Questions database organized by levels
questions_by_level = {
    1: [  # Game 1: The Board Awakens
        {
            "id": 1,
            "question": "WHAT KIND OF GAME IS CHESS?",
            "options": [
                {"text": "A. A THINKING GAME", "correct": True},
                {"text": "B. A DRAMA GAME", "correct": False},
                {"text": "C. A VIDEO GAME LIKE FORTNITE", "correct": False}
            ],
            "explanation": "Chess is a thinking game. It's where all the action happens. It's shaped like a square — with four equal sides."
        },
        {
            "id": 2,
            "question": "WHAT SHAPE IS A CHESSBOARD?",
            "options": [
                {"text": "A. TRIANGLE", "correct": False},
                {"text": "B. RECTANGLE", "correct": False},
                {"text": "C. SQUARE", "correct": True}
            ],
            "explanation": "Let's count the little squares on the board. It might look like a lot, but it's exactly sixty-four."
        },
        {
            "id": 3,
            "question": "HOW MANY SQUARES ARE ON A CHESSBOARD?",
            "options": [
                {"text": "A. SIXTY-FOUR", "correct": True},
                {"text": "B. ONE HUNDRED", "correct": False},
                {"text": "C. EIGHTY-ONE", "correct": False}
            ],
            "explanation": "Take a closer look — see those letters on the bottom and numbers on the side? That's how we name each square. Like A1 or D4."
        },
        {
            "id": 4,
            "question": "WHAT HELPS NAME THE SQUARES LIKE D5?",
            "options": [
                {"text": "A. LETTERS AND NUMBERS", "correct": True},
                {"text": "B. COLORS", "correct": False},
                {"text": "C. SHAPES", "correct": False}
            ],
            "explanation": "When you set up your board, make sure the square in the bottom-right corner is a light one. That's how you know your board is facing the right way."
        },
        {
            "id": 5,
            "question": "WHICH SQUARE SHOULD BE IN THE BOTTOM RIGHT CORNER WHEN YOU SET UP THE BOARD?",
            "options": [
                {"text": "A. A1", "correct": False},
                {"text": "B. H1", "correct": True},
                {"text": "C. A8", "correct": False}
            ],
            "explanation": "One last thing. The rows going sideways? They're called ranks. The lines going up and down? Those are called files."
        },
        {
            "id": 6,
            "question": "WHAT DO WE CALL THE ROWS AND COLUMNS OF THE BOARD?",
            "options": [
                {"text": "A. RANKS AND FILES", "correct": True},
                {"text": "B. SQUARES AND LINES", "correct": False},
                {"text": "C. POINTS AND PATHS", "correct": False}
            ],
            "explanation": "That's it for the board! Now you know all about it."
        }
    ],
    2: [  # Game 2: Meet the Chess Pieces
        {
            "id": 7,
            "question": "HOW MANY PIECES DOES EACH PLAYER START WITH?",
            "options": [
                {"text": "A. SIX", "correct": False},
                {"text": "B. TEN", "correct": False},
                {"text": "C. SIXTEEN", "correct": True}
            ],
            "explanation": "Each player has sixteen pieces. Let's start with the King. He wears a crown and moves one square in any direction. But he's slow — and very, very important."
        },
        {
            "id": 8,
            "question": "WHICH PIECE WEARS A CROWN AND MOVES ONLY ONE SQUARE AT A TIME?",
            "options": [
                {"text": "A. QUEEN", "correct": False},
                {"text": "B. KING", "correct": True},
                {"text": "C. BISHOP", "correct": False}
            ],
            "explanation": "Next up is the Queen. She's the strongest piece on the board. She can move in any direction — as far as she wants."
        },
        {
            "id": 9,
            "question": "WHICH PIECE IS THE MOST POWERFUL AND CAN MOVE IN ANY DIRECTION?",
            "options": [
                {"text": "A. QUEEN", "correct": True},
                {"text": "B. KNIGHT", "correct": False},
                {"text": "C. ROOK", "correct": False}
            ],
            "explanation": "The Rooks stand tall in the corners. They move straight across rows or columns."
        },
        {
            "id": 10,
            "question": "WHICH PIECE MOVES IN STRAIGHT LINES ACROSS THE BOARD?",
            "options": [
                {"text": "A. BISHOP", "correct": False},
                {"text": "B. ROOK", "correct": True},
                {"text": "C. KNIGHT", "correct": False}
            ],
            "explanation": "The Bishops move diagonally — like sliding across the board in a straight slant."
        },
        {
            "id": 11,
            "question": "WHICH PIECE MOVES ONLY ON DIAGONALS?",
            "options": [
                {"text": "A. KNIGHT", "correct": False},
                {"text": "B. BISHOP", "correct": True},
                {"text": "C. KING", "correct": False}
            ],
            "explanation": "Now here comes the Knight. It's shaped like a horse and moves in a very special way — in an L-shape. It's the only one that can jump over others."
        },
        {
            "id": 12,
            "question": "WHICH PIECE MOVES IN AN L-SHAPE AND CAN JUMP OVER OTHER PIECES?",
            "options": [
                {"text": "A. ROOK", "correct": False},
                {"text": "B. QUEEN", "correct": False},
                {"text": "C. KNIGHT", "correct": True}
            ],
            "explanation": "And last but not least — the Pawns. They stand in front and move one step at a time, but they can only capture by going diagonally."
        },
        {
            "id": 13,
            "question": "HOW DO PAWNS MOVE?",
            "options": [
                {"text": "A. ONE SQUARE FORWARD, CAPTURE DIAGONALLY", "correct": True},
                {"text": "B. DIAGONALLY ALL THE TIME", "correct": False},
                {"text": "C. SIDE TO SIDE", "correct": False}
            ],
            "explanation": "That's your whole team! Each piece has its own job, and when they work together — that's when the real magic happens."
        }
    ],
    3: [  # Game 3: Setting Up the Army
        {
            "id": 14,
            "question": "WHICH ROW DO THE PAWNS GO IN WHEN SETTING UP THE BOARD?",
            "options": [
                {"text": "A. FIRST ROW", "correct": False},
                {"text": "B. SECOND ROW", "correct": True},
                {"text": "C. LAST ROW", "correct": False}
            ],
            "explanation": "Let's start from the corners. The rooks go first — they're the tall towers that protect the edges."
        },
        {
            "id": 15,
            "question": "WHICH PIECES ARE PLACED IN THE CORNERS OF THE BOARD?",
            "options": [
                {"text": "A. BISHOPS", "correct": False},
                {"text": "B. KNIGHTS", "correct": False},
                {"text": "C. ROOKS", "correct": True}
            ],
            "explanation": "Next to the rooks, you place the knights — the L-shaped jumpers. Then come the bishops — they love their diagonal paths."
        },
        {
            "id": 16,
            "question": "WHERE SHOULD THE QUEEN BE PLACED?",
            "options": [
                {"text": "A. ON HER OWN COLOR SQUARE", "correct": True},
                {"text": "B. NEXT TO A ROOK", "correct": False},
                {"text": "C. ANYWHERE ON THE BOARD", "correct": False}
            ],
            "explanation": "The king stands on the last remaining square beside the queen."
        },
        {
            "id": 17,
            "question": "HOW SHOULD THE TWO SIDES LOOK AT THE START OF THE GAME?",
            "options": [
                {"text": "A. RANDOM", "correct": False},
                {"text": "B. A MIRROR OF EACH OTHER", "correct": True},
                {"text": "C. COMPLETELY DIFFERENT", "correct": False}
            ],
            "explanation": "And don't forget the golden rule — a white square should be in the bottom right!"
        },
        {
            "id": 18,
            "question": "WHICH SQUARE SHOULD BE IN THE BOTTOM-RIGHT CORNER FROM YOUR POINT OF VIEW?",
            "options": [
                {"text": "A. DARK SQUARE", "correct": False},
                {"text": "B. LIGHT SQUARE", "correct": True},
                {"text": "C. ANY SQUARE", "correct": False}
            ],
            "explanation": "Now you know how to set up the board correctly!"
        }
    ],
    4: [  # Game 4: How to Move and Capture
        {
            "id": 19,
            "question": "WHO MAKES THE FIRST MOVE IN A CHESS GAME?",
            "options": [
                {"text": "A. BLACK", "correct": False},
                {"text": "B. WHITE", "correct": True},
                {"text": "C. ANYONE CAN CHOOSE", "correct": False}
            ],
            "explanation": "You can't move through your own pieces. And you can't land on them either."
        },
        {
            "id": 20,
            "question": "CAN YOU MOVE YOUR PIECE ONTO A SQUARE WITH ONE OF YOUR OWN PIECES?",
            "options": [
                {"text": "A. YES", "correct": False},
                {"text": "B. NO", "correct": True},
                {"text": "C. ONLY PAWNS CAN", "correct": False}
            ],
            "explanation": "If the square has an opponent's piece, you can take it — that's called capturing. When you capture, you remove their piece and put yours in its place."
        },
        {
            "id": 21,
            "question": "WHAT HAPPENS WHEN YOU CAPTURE A PIECE?",
            "options": [
                {"text": "A. YOU PUSH IT OFF THE BOARD", "correct": False},
                {"text": "B. YOU LAND ON ITS SQUARE AND REMOVE IT", "correct": True},
                {"text": "C. YOU JUMP OVER IT LIKE IN CHECKERS", "correct": False}
            ],
            "explanation": "Let's talk about pawns. They usually move one square forward. But on their very first move, they can move two."
        },
        {
            "id": 22,
            "question": "HOW FAR CAN A PAWN MOVE ON ITS VERY FIRST TURN?",
            "options": [
                {"text": "A. ONE SQUARE ONLY", "correct": False},
                {"text": "B. TWO SQUARES ONLY", "correct": False},
                {"text": "C. ONE OR TWO SQUARES", "correct": True}
            ],
            "explanation": "But pawns can't capture straight ahead. They only capture diagonally, one square to the left or right."
        },
        {
            "id": 23,
            "question": "HOW DO PAWNS CAPTURE?",
            "options": [
                {"text": "A. FORWARD", "correct": False},
                {"text": "B. SIDEWAYS", "correct": False},
                {"text": "C. DIAGONALLY", "correct": True}
            ],
            "explanation": "Every piece has its own rules for movement — and learning them is the first step to winning."
        }
    ],
    5: [  # Game 5: Check, Checkmate, and Stalemate
        {
            "id": 24,
            "question": "WHAT IS IT CALLED WHEN YOUR KING IS UNDER ATTACK?",
            "options": [
                {"text": "A. CHECK", "correct": True},
                {"text": "B. CHECKMATE", "correct": False},
                {"text": "C. STALEMATE", "correct": False}
            ],
            "explanation": "There are only three ways to escape check: Move your king. Block the check with another piece. Or capture the piece that's attacking your king."
        },
        {
            "id": 25,
            "question": "WHICH OF THESE IS NOT A WAY TO GET OUT OF CHECK?",
            "options": [
                {"text": "A. MOVE YOUR KING", "correct": False},
                {"text": "B. BLOCK THE CHECK", "correct": False},
                {"text": "C. IGNORE IT AND KEEP ATTACKING", "correct": True}
            ],
            "explanation": "If your king is in check and there's no way out, that's called checkmate — and the game is over."
        },
        {
            "id": 26,
            "question": "WHAT IS CHECKMATE?",
            "options": [
                {"text": "A. WHEN THE KING IS TRAPPED AND THE GAME ENDS", "correct": True},
                {"text": "B. WHEN YOU CAPTURE THE QUEEN", "correct": False},
                {"text": "C. WHEN BOTH PLAYERS TIE", "correct": False}
            ],
            "explanation": "But sometimes the king isn't in check — and there are no legal moves left. That's called a stalemate. And guess what? That means a draw. Nobody wins."
        },
        {
            "id": 27,
            "question": "WHAT IS A STALEMATE IN CHESS?",
            "options": [
                {"text": "A. WHEN BOTH KINGS ARE GONE", "correct": False},
                {"text": "B. WHEN THE KING ISN'T IN CHECK, BUT HAS NO LEGAL MOVES", "correct": True},
                {"text": "C. WHEN THE PLAYERS GET BORED", "correct": False}
            ],
            "explanation": "Remember — check means danger, checkmate ends the game, and stalemate means it's a tie."
        },
        {
            "id": 28,
            "question": "WHAT'S THE DIFFERENCE BETWEEN CHECK AND CHECKMATE?",
            "options": [
                {"text": "A. CHECKMATE IS STRONGER — IT ENDS THE GAME", "correct": True},
                {"text": "B. THEY ARE THE SAME", "correct": False},
                {"text": "C. CHECKMATE IS JUST A WARNING", "correct": False}
            ],
            "explanation": "Congratulations! You've learned the basics of chess. Now you're ready to play!"
        }
    ]
}

# Track user progress - making this a global variable
user_progress = {
    "completed_levels": [],
    "current_level": 1,
    "current_question": 1
}

# Authentication helper function
def is_logged_in():
    # Check if user has a valid session cookie
    user_email = request.get_cookie('user_email', secret='your_secret_key')
    return user_email is not None

# Authentication decorator
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_logged_in():
            # Not logged in, redirect to login page
            return redirect('/login')
        # User is logged in, proceed to the route handler
        return func(*args, **kwargs)
    return wrapper

# Database helper functions
def get_db_connection():
    conn = sqlite3.connect('pepo.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

# Create tables if they don't exist
def init_db():
    conn = get_db_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        parent_name TEXT NOT NULL,
        child_name TEXT NOT NULL,
        child_age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS user_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        completed_levels TEXT NOT NULL DEFAULT '[]',
        current_level INTEGER NOT NULL DEFAULT 1,
        current_question INTEGER NOT NULL DEFAULT 1,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')

    conn.commit()
    conn.close()

# Get user progress from database
def get_user_progress():
    if not is_logged_in():
        return {
            "completed_levels": [],
            "current_level": 1,
            "current_question": 1
        }

    user_email = request.get_cookie('user_email', secret='your_secret_key')
    conn = get_db_connection()

    # Get user ID
    user = conn.execute('SELECT id FROM users WHERE email = ?', (user_email,)).fetchone()

    if not user:
        conn.close()
        return {
            "completed_levels": [],
            "current_level": 1,
            "current_question": 1
        }

    # Get progress
    progress = conn.execute(
        'SELECT completed_levels, current_level, current_question FROM user_progress WHERE user_id = ?',
        (user['id'],)
    ).fetchone()

    if not progress:
        # Create new progress entry
        conn.execute(
            'INSERT INTO user_progress (user_id, completed_levels, current_level, current_question) VALUES (?, ?, ?, ?)',
            (user['id'], '[]', 1, 1)
        )
        conn.commit()
        conn.close()
        return {
            "completed_levels": [],
            "current_level": 1,
            "current_question": 1
        }

    conn.close()

    # Parse completed_levels from JSON string to list
    completed_levels = json.loads(progress['completed_levels'])

    return {
        "completed_levels": completed_levels,
        "current_level": progress['current_level'],
        "current_question": progress['current_question']
    }

# Save user progress to database
def save_user_progress(progress):
    if not is_logged_in():
        return

    user_email = request.get_cookie('user_email', secret='your_secret_key')
    conn = get_db_connection()

    # Get user ID
    user = conn.execute('SELECT id FROM users WHERE email = ?', (user_email,)).fetchone()

    if not user:
        conn.close()
        return

    # Convert completed_levels list to JSON string
    completed_levels_json = json.dumps(progress['completed_levels'])

    # Update progress
    conn.execute(
        '''
        UPDATE user_progress
        SET completed_levels = ?, current_level = ?, current_question = ?
        WHERE user_id = ?
        ''',
        (
            completed_levels_json,
            progress['current_level'],
            progress['current_question'],
            user['id']
        )
    )

    conn.commit()
    conn.close()

# Serve static files
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

@app.route('/')
def index():
    return template('index', l=is_logged_in())


@app.route('/select_curriculum')
def select_prize():
    return template('select_curriculum', l=is_logged_in())

@app.route('/select_prize')
def select_prize():
    return template('select_prize', l=is_logged_in())

@app.route('/select_toy')
@app.route('/select_toy/<context>')
def select_toy(context='signup'):
    # context can be 'signup' or 'parent_request'
    return template('select_toy', context=context, l=is_logged_in())


@app.route('/signup')
def signup():
    # Check if already logged in
    user_email = request.get_cookie('user_email', secret='your_secret_key')
    if user_email:
        # User is already logged in, redirect to roadmap
        return redirect('/game')

    # Not logged in, show signup page
    return template('signup', l=is_logged_in())

@app.route('/process_signup', method='POST')
def process_signup():
    # Get form data
    parent_name = request.forms.get('parent_name')
    child_name = request.forms.get('child_name')
    age = request.forms.get('age')
    email = request.forms.get('email')
    password = request.forms.get('password')

    # Hash the password for security (in production, use better hashing with salt)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to database
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO users (parent_name, child_name, child_age, email, password) VALUES (?, ?, ?, ?, ?)',
            (parent_name, child_name, age, email, hashed_password)
        )

        # Get the user ID
        user_id = cursor.lastrowid

        # Create progress entry
        cursor.execute(
            'INSERT INTO user_progress (user_id, completed_levels, current_level, current_question) VALUES (?, ?, ?, ?)',
            (user_id, '[]', 1, 1)
        )

        conn.commit()

        # Set a session cookie (simple approach)
        response.set_cookie('user_email', email, path='/', secret='your_secret_key')
        return redirect('/')
    except sqlite3.IntegrityError:
        # Email already exists
        return template('signup', error="email already registered", l=is_logged_in())
    finally:
        conn.close()

# Login routes
@app.route('/login')
def login():
    if is_logged_in():
        return redirect('/')
    return template('login', l=is_logged_in())

@app.route('/process_login', method='POST')
def process_login():
    email = request.forms.get('email')
    password = request.forms.get('password')

    # Hash the password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db_connection()
    user = conn.execute(
        'SELECT * FROM users WHERE email = ? AND password = ?',
        (email, hashed_password)
    ).fetchone()
    conn.close()

    if user:
        # Set a session cookie
        response.set_cookie('user_email', email, path='/', secret='your_secret_key')
        return redirect('/')
    else:
        return template('login', error="invalid email or password", l=is_logged_in())

@app.route('/logout')
def logout():
    response.delete_cookie('user_email')
    return redirect('/login')

@app.route('/parent_request')
def parent_request():
    return template('parent_request')

@app.route('/parent_portal')
def parent_portal():
    return template('parent_portal')

@app.route('/roadmap')
def roadmap():
    return template('roadmap', progress=user_progress)

@app.route('/game_title/<level:int>')
def game_title(level):
    titles = {
        1: "THE BOARD AWAKENS",
        2: "MEET THE CHESS PIECES",
        3: "SETTING UP THE ARMY",
        4: "HOW TO MOVE AND CAPTURE",
        5: "CHECK, CHECKMATE, AND STALEMATE"
    }

    if level not in titles:
        redirect('/')

    return template('game_title', level=level, title=titles[level])

@app.route('/intro/<level:int>')
def game_intro(level):
    intros = {
        1: "HELLO, LITTLE CHESS PLAYERS! I'M YOUR GUIDE FOR TODAY, AND WE'RE ABOUT TO EXPLORE THE WORLD OF CHESS.",
        2: "NOW THAT WE KNOW THE BOARD, LET'S MEET THE STARS OF THE GAME — THE CHESS PIECES!",
        3: "NOW THAT YOU KNOW THE CHESS PIECES, IT'S TIME TO LEARN WHERE THEY STAND AT THE START OF THE GAME.",
        4: "LET'S LEARN HOW TO PLAY. EACH TURN, YOU MOVE JUST ONE PIECE — EXCEPT WHEN CASTLING (WE'LL TALK ABOUT THAT LATER).",
        5: "THE KING IS THE MOST IMPORTANT PIECE ON THE BOARD. IF YOU LOSE YOUR KING, THE GAME IS OVER. SO YOU MUST PROTECT HIM AT ALL COSTS."
    }

    if level not in intros:
        redirect('/')

    # Redirect to first lesson instead of intro template
    return redirect(f'/lesson/{level}/1')

# Add lessons content before quiz
lessons = {
    1: [
        "Hello, little champions! Welcome to your first chess lesson. Chess is a fun thinking game and is about making smart moves.",
        "Let me introduce you to the stars of the chess world. Meet the king, he wears the tall crown and comes with a cross.",
        "Lets meet the Queen. She wears a princess crown.",
        "Pawns are the little soldiers with the round tops.",
        "The Knight looks like a little horse.",
        "The Bishop looks like it is wearing a little hat and is tall and thin.",
        "The Rook looks like a small castle and stand in the corners."
    ],
    2: [
        "Let's set up the board before we play. There are two colors in chess, white and black, One player uses white pieces and the other player uses black pieces.",
        "Now let's start placing the pieces. First, we place the pawns. All the pawns line up together in one row. They go on the second line of your chessboard.",
        "Let's place the rooks. Each player has two rooks. The rooks go in the corners of the board.",
        "Now we place the knights. Each knight goes next to a rook. One knight stands next to the left rook. One knight stands next to the right rook.",
        "Now we place the bishops. Each bishop goes next to a knight. There are two bishops, one on each side.",
        "Now let's place the queen. The queen goes in the middle. She always goes on her own color. White queen on a white square. Black queen on a black square.",
        "The last piece is the king. The king always stands right next to the queen."
    ],
    3: [
        "Let's learn how to set up your chess army correctly.",
        "Let's start from the corners. The rooks go first — they're the tall towers that protect the edges.",
        "Next to the rooks, you place the knights — the L-shaped jumpers. Then come the bishops — they love their diagonal paths.",
        "The king stands on the last remaining square beside the queen.",
        "And don't forget the golden rule — a white square should be in the bottom right!"
    ],
    4: [
        "Let's learn how the pieces move and capture in chess.",
        "You can't move through your own pieces. And you can't land on them either.",
        "If the square has an opponent's piece, you can take it — that's called capturing. When you capture, you remove their piece and put yours in its place.",
        "Let's talk about pawns. They usually move one square forward. But on their very first move, they can move two.",
        "But pawns can't capture straight ahead. They only capture diagonally, one square to the left or right."
    ],
    5: [
        "The king is the most important piece on the board. If you lose your king, the game is over.",
        "There are only three ways to escape check: Move your king. Block the check with another piece. Or capture the piece that's attacking your king.",
        "If your king is in check and there's no way out, that's called checkmate — and the game is over.",
        "But sometimes the king isn't in check — and there are no legal moves left. That's called a stalemate. And guess what? That means a draw. Nobody wins.",
        "Remember — check means danger, checkmate ends the game, and stalemate means it's a tie."
    ]
}

@app.route('/lesson/<level:int>/<lesson_num:int>')
def lesson(level, lesson_num):
    # Check if level exists
    if level not in lessons:
        redirect('/')
    
    # Get lesson content for this level
    level_lessons = lessons[level]
    
    # Check if lesson index is valid (1-based indexing for URL)
    lesson_index = lesson_num - 1
    if lesson_index < 0 or lesson_index >= len(level_lessons):
        # If lesson doesn't exist, go to first lesson of level
        redirect(f'/lesson/{level}/1')
    
    # Get lesson content
    lesson_content = level_lessons[lesson_index]
    
    # After each lesson, go directly to the corresponding quiz question
    next_url = f'/game/{level}/{lesson_num}'
    
    return template('lesson',
                   lesson_content=lesson_content,
                   level=level,
                   lesson_num=lesson_num,
                   next_url=next_url,
                   is_last_lesson=True)  # Always true since we're going to quiz next

@app.route('/game/<level:int>/<question_index:int>')
def game(level, question_index):
    # Check if level exists
    if level not in questions_by_level:
        redirect('/')

    # Convert to zero-based index
    question_index = int(question_index) - 1

    # Check if question index is valid
    level_questions = questions_by_level[level]
    if question_index < 0 or question_index >= len(level_questions):
        # If question doesn't exist, go to first question of level
        redirect(f'/game/{level}/1')

    question = level_questions[question_index]

    # Update current progress
    user_progress["current_level"] = level
    user_progress["current_question"] = question_index + 1

    # Check if it's the last question in level
    is_last_question = question_index == len(level_questions) - 1

    # If this is the last question in the level, finish the level
    # Otherwise, go to the next lesson
    next_lesson_num = question_index + 2  # +1 for 0-based index, +1 to go to next
    
    return template('game',
                   question=question,
                   level=level,
                   question_index=question_index + 1,
                   is_last_question=is_last_question)

@app.route('/check_answer', method='POST')
def check_answer():
    selected_option = int(request.forms.get('option'))
    level = int(request.forms.get('level'))
    question_index = int(request.forms.get('question_index')) - 1

    # Get question from level and index
    level_questions = questions_by_level[level]
    if question_index < 0 or question_index >= len(level_questions):
        return json.dumps({'error': 'Question not found'})

    question = level_questions[question_index]
    correct = question['options'][selected_option]['correct']

    response.content_type = 'application/json'
    return json.dumps({
        'correct': correct,
        'selected': selected_option,
        'correct_index': next((i for i, opt in enumerate(question['options']) if opt['correct']), 0)
    })

@app.route('/complete_level/<level:int>')
def complete_level(level):
    level = int(level)

    # Mark level as completed if not already
    if level not in user_progress["completed_levels"]:
        user_progress["completed_levels"].append(level)

    # Unlock next level if available
    if level < max(questions_by_level.keys()):
        user_progress["current_level"] = level + 1

    # Debug print to console
    print(f"Completed level {level}. Progress: {user_progress}")

    redirect('/roadmap')

@app.route('/spin')
def spin():
    return template('spin')

@app.route('/start')
def start():
    return template('start')

@app.route('/process_start', method='POST')
def process_start():
    # Get form data
    name = request.forms.get('name')
    email = request.forms.get('email')

    print("start!!!!", name, email)

    return redirect('/giftbox')

@app.route('/giftbox')
def giftbox():
    return template('giftbox')

# Initialize the database when the app starts
init_db()

# Run the application
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
