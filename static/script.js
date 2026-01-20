const display = document.querySelector(".display");
const buttons = document.querySelectorAll(".buttons button");

buttons.forEach(button => {
    button.addEventListener("click", () => {
        const value = button.innerText;

        // Prevent accidental submit
        if (value === "=") {
            return;
        }

        // Clear display
        if (value === "C") {
            display.value = "";
            return;
        }

        // Delete last character
        if (value === "DEL") {
            display.value = display.value.slice(0, -1);
            return;
        }

        // Prevent multiple operators in a row
        const lastChar = display.value.slice(-1);
        const operators = ["+", "-", "*", "/"];

        if (operators.includes(value) && operators.includes(lastChar)) {
            return;
        }

        // Append value
        display.value += value;
    });
});
