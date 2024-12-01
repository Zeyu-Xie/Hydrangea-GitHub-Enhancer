// Configuration
const config = {
    'maxWaitingTime': 65535,
};

// Functions
const getFileType = (fileName, isDir) => {
    
    if (isDir) {
        return "FOLDER"
    }
    
//    const spec = ["DOCKERFILE", "LICENSE", "MAKEFILE"]
    const spec = ["DOCKERFILE"]
    if (fileName.toUpperCase() in spec) {
        return fileName
    }
    
    return (fileName.split('.').pop().toUpperCase() || '')
}

// Scripts
const prettifyIcons = () => {
    const _table = document.querySelector("[aria-labelledby='folders-and-files']");
    const _tbody = _table.getElementsByTagName('tbody')[0];
    const _tr_list = Array.from(_tbody.getElementsByTagName('tr')).slice(1, -1);
    const _svg_list = Array.from(_tr_list).map(tr => tr.getElementsByTagName('svg')[0])
    const _svg_list_ex = Array.from(_tr_list).map(tr => tr.getElementsByTagName('svg')[1])
    const _a_list = Array.from(_tr_list).map(tr => tr.getElementsByTagName('a')[0]);
    
    const fileNum = _tr_list.length
    const iconClassList = _svg_list.map(svg => svg.className.baseVal);
    const isDirList = iconClassList.map(item => item === 'icon-directory' ? true : false);
    const fileNameList = _a_list.map(a => a.innerText);
    const fileTypeList = [...Array(fileNum)].map((_, i) => getFileType(fileNameList[i], isDirList[i]));
    
    for(let i=0; i<fileNum; i++) {
        const fileType = getFileType(fileNameList[i], isDirList[i])
        if (fileType in config['iconsSVG']) {
            _svg_list[i].innerHTML = config['iconsSVG'][fileType]
            _svg_list_ex[i].innerHTML = config['iconsSVG'][fileType]
        }
    }
}

// Load icons data
chrome.runtime.sendMessage({ action: 'getIconsData' }, (response) => {
    if (response.success) {
        config["iconsSVG"] = response.data
        console.log("Successfully fetched icons SVG data.")
    } else {
        console.error("ERROR", response.error);
    }
});

// Main
window.addEventListener('load', ()=>{
    
    const intervalId = setInterval(prettifyIcons, 100);
    setTimeout(()=>{
        clearInterval(intervalId)
    }, config['maxWaitingTime'])
});
