let button = document.getElementById("OpenButton");
let message = document.getElementById("message");

button.onclick = requestDoor()
ss
function sleep(ms) {
  const wakeUpTime = Date.now() + ms;
  while (Date.now() < wakeUpTime) {}
}

function requestDoor() {
    console.log(JSON.stringify(body))
    const response = await fetch('api/door', {
    });
    setTimeout(() => {
        const response = await fetch('api/door', {
            method: 'GET',
        });
        response = await response.json();
        redirect(response);
    }, 1000);
}

function redirect(response) {
    console.log(response)
    console.log(response["Result"])
    if (response["Result"] == "tutorial") {
        window.location.href = "/tutorial"
    } else if (response["Result"] == "feedback") {
        window.location.href = "/feedback?ID=" + String(response["ID"])
    } else if (response["Result"] == "kicked" && response["Result"] == "waiting") {
        message.textContent = "쓰레기를 넣고 문을 닫아 주세요"
    }
}
