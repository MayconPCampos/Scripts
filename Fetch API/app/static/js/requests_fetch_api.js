// Requisições usando fetch API

// post request
function post_entry() {
    var password = document.getElementById("password")
    var user = document.getElementById("user")
    var entry = {
        user: user.value,
        password: password.value
    }
    fetch(`${window.origin}/post-message`,{
        method: "POST",
         body: JSON.stringify(entry),
         headers: new Headers({"content-type": "application/json"
        })
    })
    .then(function(response){
        if (response.status !== 200) {
            console.log(`Error ${response.status}`)
        }
    })
}

// Get request
function get_entry() {
    var name = document.getElementById("name");
    var message = document.getElementById("message");
    var entry = {
        name: name.value,
        message: message.value
    };
    var url = new URL(`${window.origin}/get-message`)
    var params = entry
    url.search = new URLSearchParams(params).toString();
    fetch(url).then(function(response){
        if (response.status !== 200){
            console.log(`Error ${response.status}`)
        }
    })
}