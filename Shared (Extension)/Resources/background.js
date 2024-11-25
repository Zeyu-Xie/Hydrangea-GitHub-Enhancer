browser.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("Received request: ", request);
    
    if (request.greeting === "hello")
        return Promise.resolve({ farewell: "goodbye" });
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'getIconsData') {
        fetch(chrome.runtime.getURL('data/icons.json'))
        .then(response => response.json())
        .then(data => {
            sendResponse({ success: true, data: data });
        })
        .catch(error => {
            sendResponse({ success: false, error: error });
        });
        return true;
    }
});
