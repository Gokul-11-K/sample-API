function saveText() {

    let message = document.getElementById("message").value;
    fetch("http://127.0.0.1:5000/save", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            content: message
        })
    })

    .then(response => response.json())

    .then(data => {
        document.getElementById("result").innerText =
            data.message;
    })

    .catch(error => {
        console.error("Error:", error);
            alert("API connection failed")
    });
}