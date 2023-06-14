// Funkcja do pokazywania okna koszyka
function pokazOknoKoszyka() {
    // Pokaż overlay
    let overlay = document.getElementById('overlay');
    overlay.style.display = 'block';

    // Pokaż okno koszyka
    let oknoKoszyka = document.getElementById('okno-koszyka');
    oknoKoszyka.style.display = 'block';

    // Wyświetl zawartość koszyka
    pokazKoszyk();
}

// Funkcja do ukrywania okna koszyka
function schowajOknoKoszyka() {
    // Schowaj overlay
    let overlay = document.getElementById('overlay');
    overlay.style.display = 'none';

    // Schowaj okno koszyka
    let oknoKoszyka = document.getElementById('okno-koszyka');
    oknoKoszyka.style.display = 'none';
}

function dodajDoKoszyka(nazwa, id) {
    // Sprawdź, czy w magazynie (localStorage) jest już zapisany koszyk
    let koszyk = JSON.parse(localStorage.getItem('koszyk')) || [];

    // Sprawdź, czy produkt już istnieje w koszyku
    let istnieje = false;
    koszyk.forEach(function (produkt) {
        if (produkt.id === id) {
            istnieje = true;
            produkt.ilosc += 1; // Zwiększ ilość produktu
        }
    });

    // Jeśli produkt nie istnieje w koszyku, dodaj go jako nowy
    if (!istnieje) {
        koszyk.push({ nazwa: nazwa, id: id, ilosc: 1 });
    }

    // Zapisz zaktualizowany koszyk w magazynie (localStorage)
    localStorage.setItem('koszyk', JSON.stringify(koszyk));

    // Odśwież zawartość koszyka
    pokazKoszyk();
}

function zmienIlosc(id, ilosc) {
    // Sprawdź, czy w magazynie (localStorage) jest już zapisany koszyk
    let koszyk = JSON.parse(localStorage.getItem('koszyk')) || [];

    // Znajdź produkt o podanym id
    let indeks = koszyk.findIndex(function (produkt) {
        return produkt.id === id;
    });

    // Jeżeli ilość wynosi 0, usuń produkt z koszyka
    if (ilosc === 0 && indeks !== -1) {
        koszyk.splice(indeks, 1);
    } else if (ilosc > 0) {
        // Jeżeli ilość jest większa od 0, zaktualizuj ilość
        if (indeks !== -1) {
            koszyk[indeks].ilosc = ilosc;
        } else {
            // Jeżeli produkt nie istnieje w koszyku, dodaj go z podaną ilością
            koszyk.push({ id: id, ilosc: ilosc });
        }
    }

    // Zapisz zaktualizowany koszyk w magazynie (localStorage)
    localStorage.setItem('koszyk', JSON.stringify(koszyk));

    // Odśwież zawartość koszyka
    pokazKoszyk();
}

function pokazKoszyk() {
    // Sprawdź, czy w magazynie (localStorage) jest już zapisany koszyk
    let koszyk = JSON.parse(localStorage.getItem('koszyk')) || [];

    // Wyczyść listę koszyka
    let koszykElement = document.getElementById('koszyk');
    koszykElement.innerHTML = '';

    // Wyświetl każdy produkt z koszyka
    koszyk.forEach(function (produkt) {
        let li = document.createElement('li');
        li.dataset.id = produkt.id; // Przechowaj identyfikator produktu w atrybucie data-id

        let img = document.createElement('img');
        img.src = 'Produkty/' + produkt.id + '.png'; // Generuj nazwę pliku obrazu na podstawie identyfikatora
        img.alt = produkt.nazwa;
        img.width = 50;
        li.appendChild(img);

        let nazwa = document.createElement('span');
        nazwa.textContent = produkt.nazwa;
        li.appendChild(nazwa);

        let iloscContainer = document.createElement('div');
        iloscContainer.classList.add('ilosc-container');

        let minusButton = document.createElement('button');
        minusButton.textContent = '-';
        minusButton.onclick = function () {
            let aktualnaIlosc = parseInt(iloscInput.value) || 0;
            let nowaIlosc = Math.max(aktualnaIlosc - 1, 0);
            zmienIlosc(produkt.id, nowaIlosc);
        };
        iloscContainer.appendChild(minusButton);

        let iloscInput = document.createElement('input');
        iloscInput.type = 'number';
        iloscInput.min = 0;
        iloscInput.max = 99;
        iloscInput.value = produkt.ilosc;
        iloscInput.onchange = function () {
            let nowaIlosc = parseInt(iloscInput.value) || 0;
            zmienIlosc(produkt.id, nowaIlosc);
        };
        iloscContainer.appendChild(iloscInput);

        let plusButton = document.createElement('button');
        plusButton.textContent = '+';
        plusButton.onclick = function () {
            let aktualnaIlosc = parseInt(iloscInput.value) || 0;
            let nowaIlosc = Math.min(aktualnaIlosc + 1, 99);
            zmienIlosc(produkt.id, nowaIlosc);
        };
        iloscContainer.appendChild(plusButton);

        li.appendChild(iloscContainer);

        let usunButton = document.createElement('button');
        usunButton.textContent = 'X';
        usunButton.onclick = function () {
            zmienIlosc(produkt.id, 0);
        };
        li.appendChild(usunButton);

        koszykElement.appendChild(li);
    });
}

// Funkcja do usuwania produktu z koszyka
function usunZKoszyka(id) {
    // Sprawdź, czy w magazynie (localStorage) jest już zapisany koszyk
    let koszyk = JSON.parse(localStorage.getItem('koszyk')) || [];

    // Usuń produkt z koszyka
    koszyk = koszyk.filter(function (produkt) {
        return produkt.id !== id;
    });

    // Zapisz zaktualizowany koszyk w magazynie (localStorage)
    localStorage.setItem('koszyk', JSON.stringify(koszyk));

    // Odśwież zawartość koszyka
    pokazKoszyk();
}


function wyczyscKoszyk() {
    // Wyczyść magazyn (localStorage)
    localStorage.removeItem('koszyk');

    // Odśwież zawartość koszyka
    pokazKoszyk();

}
window.addEventListener("scroll", function() {
    var fale = document.getElementById("fale");
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    fale.style.bottom = (-scrollTop) + "px";

});

