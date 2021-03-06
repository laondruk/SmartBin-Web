let button = document.getElementById("OpenButton");

function sleep(ms) {
  const wakeUpTime = Date.now() + ms;
  while (Date.now() < wakeUpTime) {}
}

const lockDoor = async() => {
    let body = {}
    body["open"] = true

    console.log(JSON.stringify(body))
    const response = await fetch('api/door', {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'}
    });
    var res_json = await response.json()
    res_json = JSON.parse(res_json)
    await console.log(res_json)
    await redirect(res_json)
}

function redirect(response) {
    console.log(response)
    console.log(response["Result"])
    if (response["Result"] == "tutorial") {
        window.location.href = "/tutorial"
    } else if (response["Result"] == "feedback") {
        window.location.href = "/feedback?ID=" + String(response["ID"])
    }
}
