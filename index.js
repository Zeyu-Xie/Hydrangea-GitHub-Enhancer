let username = '';

const _repo_lists = document.getElementById("repo_lists")

fetch("./config.json").then(config => config.json()).then(config => {
    username = config.username
}).then(() => {
    fetch(`https://api.github.com/users/${username}/repos?type=public`)
        .then(data => data.json())
        .then(data => {
            data.forEach(item => {
                const _repo_item = document.createElement("li")
                _repo_item.innerHTML = `<a href="${item.owner.html_url + "/" + item.name}">${item.name}</a>`
                _repo_lists.appendChild(_repo_item)
            });
        }).catch(err_ => {
            console.log("ERROR" + err_)
        })
}).catch(err => {
    console.log("ERROR", err)
})