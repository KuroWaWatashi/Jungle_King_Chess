from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "yVamTNN7TNRyE8D"

MENU_FONT_PATH = "fonts/Minecraft_Lowercase_&_Uppercase_Font.ttf"
BUTTON_FONT_PATH = "fonts/Minecraft_Font.ttf"

START_LOGO_IMG_PATH = 'img/Jungle_King_Chess_Logo.png'
START_MENU_BG_IMG_PATH = 'img/Jungle_King_Chess_Background_Img.jpg'
STANDARD_MENU_BG_IMG_PATH = 'img/Standard_Menu_Background_Img.jpg'
FACTION_MENU_IMG_PATH = 'img/Green_Terracotta_Background_Texture.png'

def push_menu(menu_route):
    if "menu_stack" not in session:
        session["menu_stack"] = []
    session["menu_stack"].append(menu_route)

@app.route("/return")
def return_to_previous_menu():
    if "menu_stack" in session and len(session["menu_stack"]) > 1:
        session["menu_stack"].pop()
    return redirect(session["menu_stack"][-1])

@app.route('/')
def start_menu():
    push_menu("/")
    return render_template("menu_class.html", favicon_logo_path=url_for('static', filename=START_LOGO_IMG_PATH), favicon_title="Start Menu", menu_bg_img_path=url_for('static', filename=START_MENU_BG_IMG_PATH), title_x_pos="50%", title_y_pos="350px", title_img_scaling_x="550px", title_img_scaling_y="550px",
                           buttons=[
                               {"button_text": "Click To Start!", "url": "/main_menu", "button_x_pos": "50%", "button_y_pos": "65%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "70px"},
                               {"button_text": "Exit", "url": "/exit", "button_x_pos": "50%", "button_y_pos": "90%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "70px"}
                           ])

@app.route("/main_menu")
def main_menu():
    # return send_from_directory(IMAGE_FOLDER, filename)
    return render_template("menu_class.html", favicon_title="Main Menu", menu_bg_img_path=url_for('static', filename=STANDARD_MENU_BG_IMG_PATH), title_x_pos="50%", title_y_pos="-5%", menu_title_input_font_size="100px", menu_title="Main Menu", menu_font_path=url_for('static', filename=MENU_FONT_PATH),
                           buttons=[
                               {"button_text": "Demo Mode", "url": "/faction_selection_menu", "button_x_pos": "50%", "button_y_pos": "18%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"},
                               {"button_text": "Single-Player Mode", "url": "/single_player_difficulty_selection_menu", "button_x_pos": "50%", "button_y_pos": "28%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"},
                               {"button_text": "Multi-Player Mode", "url": "/faction_selection_menu", "button_x_pos": "50%", "button_y_pos": "38%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"},
                               {"button_text": "Review Matches", "url": "/review_matches", "button_x_pos": "50%", "button_y_pos": "48%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"},
                               {"button_text": "Settings", "url": "/settings_menu", "button_x_pos": "50%", "button_y_pos": "58%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"},
                               {"button_text": "Return", "url": "/return", "button_x_pos": "50%", "button_y_pos": "68%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"},
                               {"button_text": "Home", "url": "/home", "button_x_pos": "50%", "button_y_pos": "78%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"},
                               {"button_text": "Quit", "url": "/quit_menu", "button_x_pos": "50%", "button_y_pos": "88%", "button_input_font": BUTTON_FONT_PATH, "button_input_font_size": "40px"}
                           ])

@ app.route("/faction_selection_menu")
def faction_menu():
    pass

@app.route("/demo_mode")
def demo_mode():
    pass

@app.route("/single_player_mode")
def single_player_mode():
    pass

@app.route("/single_player_difficulty_selection_menu")
def single_player_difficulty_selection_menu():
    pass

@app.route("/multi_player_mode")
def multi_player_mode():
    pass

@app.route("/review_matches")
def review_matches():
    pass

@app.route("/settings_menu")
def settings_menu():
    pass

@app.route("/return_menu")
def return_menu():
    pass

@app.route("/home")
def home():
    return redirect(url_for("/"))

if __name__ == "__main__":
    app.run(debug=True)