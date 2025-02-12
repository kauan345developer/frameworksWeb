const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
const img = new Image();
img.src = "https://placehold.co/400";
let x, y;

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    x = (canvas.width - 400) / 2;  // 400 é a largura da imagem
    y = (canvas.height - 400) / 2; // 400 é a altura da imagem
    if (img.complete) {
        ctx.drawImage(img, x, y);
    }
}

window.addEventListener('resize', resizeCanvas);
resizeCanvas();

img.onload = () => {
    ctx.drawImage(img, x, y);
};

document.addEventListener("keydown", (event) => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (event.key === "ArrowRight") {
        x += 10;
    } else if (event.key === "ArrowLeft") {
        x -= 10;
    } else if (event.key === "ArrowUp") {
        y -= 10;
    } else if (event.key === "ArrowDown") {
        y += 10;
    }
    ctx.drawImage(img, x, y);
});
