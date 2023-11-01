const films = [
    {
        title: "Tron Efsanesi",
        image: "../img/Tronlegacy.jpg",
        description: "Kült bilgisayar oyunundan uyarlanan ilk filmin ardından, yenilenmiş ve göz kamaştırıcı görsel efektleri arkasına almış, 3D ileri teknoloji macerası TRON Efsanesi'nde, Kevin Flynn'in 27 yaşındaki teknoloji meraklısı oğlu Sam Flynn, babasının ortadan kayboluşunu araştırır ve kendini babasının 25 yıldır yaşadığı Tron'un dijital dünyasında bulur.\nKevin'in sadık arkadaşı Quorra'yla birlikte, baba ve oğul çok fazla gelişmiş ve son derece tehlikeli bir hale gelen, görsel açıdan üst düzey sanal alemde bir ölüm kalım yolculuğuna çıkarlar...",
    },
    {
        title: "Film 2",
        image: "film2.jpg",
        description: "Bu film hakkında kısa bir açıklama...",
    },
    // Daha fazla film ekleyebilirsiniz.
];

const filmList = document.getElementById("film-list");
const filmDetail = document.getElementById("film-detail");
const closeBtn = document.getElementById("close-button");

function showFilmDetail(film) {
    filmDetail.innerHTML = `
    <div class="dot" id="dot">
        <h2>${film.title}</h2>
        <img src="${film.image}" alt="${film.title}">
        <p>${film.description}</p>
    </div>
    `;
    filmDetail.style.display = "block";
}

function closeFilmDetail() {
    filmDetail.style.display = "none";
}

films.forEach((film, index) => {
    const filmCard = document.createElement("div");
    filmCard.classList.add("film-card");
    filmCard.innerHTML = `<h3>${film.title}</h3><img src="${film.image}" alt="${film.title}">`;
    filmCard.addEventListener("click", () => showFilmDetail(films[index]));
    filmList.appendChild(filmCard);
});

closeBtn.addEventListener("click", closeFilmDetail);

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
