const inputs  = document.querySelectorAll(".input-fields")
const toggle_btn  = document.querySelectorAll(".toogle")
const main  = document.querySelectorAll(".main")
const bullets = document.querySelectorAll(".bullets span")
const images  = document.querySelectorAll(".images")

inputs.forEach((inp) => {
    inp.addEventListener("focus", () => {
        inp.classList.add("active");
    });
    inp.addEventListener("blur", () => {
        if (inp.value != "") return;
        inp.classList.remove("active");
    });
});

toggle_btn.forEach((btn) => {
    btn.addEventListener("click", () => {
        main.classList.toggle("sign-up-mode");
    });
});

function moveSlider() {
    let index = this.dataset.value;

    let currentImage = document.querySelector(`.img-${index}`);
    images.forEach((img) => img.classList.remove("show"));
    currentImage.classList.add("show");

    const textSlider = document.querySelector("text-group");
    textSlider.style.tansform = `translateY(${-(index - 1) *2.2}rem)`;

    bullets.forEach((bullet) => bullet.classList.remove("active"));
    this.classList.add("active");
}

bullets.forEach((bull) => {
    bull.addEventListener("click",moveSlider);
});
