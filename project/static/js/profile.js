const form = document.querySelector("#form");
const inputs = document.querySelectorAll(".inputs");
const buttons = document.querySelectorAll(".buttons");
const submitBtns = document.querySelectorAll(".submit");

form.addEventListener("keydown", (event) => {
  if (event.key === "enter") {
    event.preventDefault();
  }
});

buttons.forEach((btn, idx) => {
  btn.addEventListener("click", (target) => {
    target.preventDefault();

    inputs[idx].disabled = false;
    submitBtns[idx].style.display = "block";
    btn.style.display = "none";
  });
});

submitBtns.forEach((btn, idx) => {
  btn.addEventListener("click", (event) => {
    event.preventDefault();

    inputs[idx].disabled = true;
    buttons[idx].style.display = "block";
    btn.style.display = "none";
  });
});
