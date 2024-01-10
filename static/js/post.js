
console.log("post.js loaded")
let submit = d3.select("#submit");

submit.on("click", () => {
    let data = d3.select("#data");
    let moreData = d3.select("#data2");
    let response = d3.select("#response");

    payload = {}
    //get the value of the input fields
    payload.whatever = data.node().value
    payload.hoobastank = moreData.node().value
    d3.text("/get_data", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "data=" + JSON.stringify(payload) // add it to the http header as a json string
    }).then(data => {
        //display the data in div 'response'
        response.text(data);
        //log the data
        console.log('this is what the response from flask was')
        console.log(data);
    });
});
