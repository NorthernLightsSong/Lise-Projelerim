const dot = document.getElementById("dot");

setInterval(() => {
    dot.style.animation = "changeColor 1s linear infinite";
    setTimeout(() => {
        dot.style.animation = "";
    }, 4000); // Her 4 saniyede bir renk değişikliği yap
}, 8000); // Her 8 saniyede bir animasyonu yeniden başlat

document.getElementById("login-button").addEventListener("click", () => {
    // Burada giriş işlemlerini gerçekleştirebilirsiniz.
    window.location.href = "html/home_page.html",alert("Giriş işlemi Başarılı."); // Yönlendirilecek sayfanın adını buraya ekleyin;
});
