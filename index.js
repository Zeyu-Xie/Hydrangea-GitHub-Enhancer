let username = '';

const _repo_lists = document.getElementById("repo_lists")

fetch("./config.json").then(config => config.json()).then(config => {
    username = config.username
}).then(async () => {

    var finished = false
    var round = 1

    while (!finished) {
        await fetch(`https://api.github.com/users/${username}/repos?type=public&per_page=50&page=${round++}`)
            .then(data => data.json())
            .then(data => {
                if (data.length < 1) {
                    finished = true
                }
                data.forEach(item => {
                    const _repo_item = document.createElement("tr")
                    _repo_item.innerHTML = `
                    <td><a href="${item.html_url}">${item.name}</a></td>
                    <td><a href="${item.homepage}">Link</a></td>
                    <td onclick="navigator.clipboard.writeText('${item.git_url}')">Copy</td>
                    <td onclick="navigator.clipboard.writeText('${item.ssh_url}')">Copy</td>
                `
                    _repo_lists.appendChild(_repo_item)
                })
            }).catch(err_ => {
                console.log("ERROR" + err_)
            })
    }


}).catch(err => {
    console.log("ERROR", err)
})