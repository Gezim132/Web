

let heartChange = document.getElementsByClassName('fa-heart')

// console.log(heartChange)
// function heart() {

//     heartChange.classList.toggle("fa-solid")
// }

for (let i = 0; i <= heartChange.length - 1; i++) {
    heartChange[i].addEventListener('click', function () {
        heartChange[i].classList.toggle("fa-solid")
    })
}

// year
let year = document.getElementById("year")
year.textContent = new Date().getFullYear()