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
    putLikeArticle(likes)
    putLikeComment(likes)
}

async function onClick(event) {
    event.preventDefault()
    let button = event.target
    let url

    if (button.id === 'btn_likes') {
        button.id = 'btn_unlikes'
        url = `/${button.dataset.name}_like_add/` + button.dataset.id
    } else {
        button.id = 'btn_likes'
        url = `/${button.dataset.name}_like_delete/` + button.dataset.id
    }
    let likes = await makeRequest(url);
    putLikeArticle(likes)
    putLikeComment(likes)
}

async function putLikeArticle(likes) {
    let like_numbers
    let dict
    dict = likes['article']
    like_numbers = document.querySelectorAll('#like_a_number')

    for (let [key, value] of Object.entries(dict)) {
        key++
        for (let like_number of like_numbers) {
            let number = like_number.dataset.id
            if (key.toString() === number) {
                like_number.innerHTML = value[`${key}`] + '<i class="bi bi-hand-thumbs-up"></i>'
            }
        }
    }
}

async function putLikeComment(likes) {
    let like_numbers
    let dict
    dict = likes['comment']
    like_numbers = document.querySelectorAll('#like_c_number')

    for (let [key, value] of Object.entries(dict)) {
        key++
        for (let like_number of like_numbers) {
            let number = like_number.dataset.id
            if (key.toString() === number) {
                like_number.innerHTML = value[`${key}`] + '<i class="bi bi-hand-thumbs-up"></i>'
            }
        }
    }
}

allLike()

window.addEventListener('load', onClick)