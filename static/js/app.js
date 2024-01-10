console.log("app.js loaded");

d3.json("/api").then(data => {
    console.log('this is data loaded from the api. ');
    console.log(data);
    //loop through the array, if there is one
    data.forEach(element => {
        console.log(element)
    });
})