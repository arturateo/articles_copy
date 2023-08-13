async function makeRequest(url, method = 'GET') {
    let response = await fetch(url, {"method": method});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response
        console.log(error)
        throw error;
    }
}

async function allLike() {
    let response = await fetch(`http://127.0.0.1:8000/like_view/`)
    let likes = await response.json();
    putLike(likes)
}

async function onClick(event) {
    event.preventDefault()
    let button = event.target
    let url
    if (button.id === 'btn_likes'){
        button.id = 'btn_unlikes'
        url = `/like_add/` + button.dataset.id
    }
    else{
        button.id = 'btn_likes'
        url = `/like_delete/` + button.dataset.id
    }

    let likes = await makeRequest(url);
    console.log(likes)
    putLike(likes)

}

async function putLike(likes) {
    let like_numbers
    for (let [key, value] of Object.entries(likes.article)){
        console.log(value)
        key ++
        like_numbers = document.querySelectorAll('#like_number')
        for (let like_number of like_numbers){
            let number = like_number.dataset.id
            if (key.toString() === number){
                like_number.innerText = value[`${key}`]
            }
        }
    }
}

allLike()
