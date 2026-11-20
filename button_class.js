let current_index = null;
let buttons = document.querySelectorAll(".menu-button_text");
let keyboard_selection = false;

function update_selection() {
    buttons.forEach((button, index) => {
        if (index === current_index) {
            button.classList.add("selected");
        } else {
            button.classList.remove("selected");
        }
    });
}

function arrow_keys_event(event) {
    if (event.key === "ArrowUp") {
        keyboard_selection = true;
        if (current_index === null) {
            current_index = 0;
        } else {
            current_index = (current_index - 1 + buttons.length) % buttons.length;
        }
    } else if (event.key === "ArrowDown") {
        keyboard_selection = true;
        if (current_index === null) {
            current_index = 0;
        } else {
            current_index = (current_index + 1) % buttons.length;
        }
    } else if (event.key === "Enter" && current_index !== null) {
        buttons[current_index].click();
    }
    update_selection();
}

buttons.forEach((button, index) => {
    button.addEventListener("mouseenter", () => {
        if (keyboard_selection) {
            keyboard_selection = false;
            current_index = null;
            update_selection();
        }
    });
})

update_selection();