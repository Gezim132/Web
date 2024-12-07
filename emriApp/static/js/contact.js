// year
let year = document.getElementById("year")
year.textContent = new Date().getFullYear()

// Form

function validim(event) {
    event.preventDefault()
    let emri = document.getElementById("emri").value
    let mbiemri = document.getElementById("mbiemri").value
    let email = document.getElementById("email").value
    let koment = document.getElementById("koment").value
    let sms = document.getElementById("sms")
    if (emri == "" || mbiemri == "" || email == "" || koment == "") {
        sms.textContent = "Plotesoi te gjitha fushat"
        sms.classList.add('text-danger')
        sms.classList.remove('text-success')
    } else {
        sms.textContent = "Faleminderit!!"
        sms.classList.add('text-success')
        sms.classList.remove('text-danger')
    }
}