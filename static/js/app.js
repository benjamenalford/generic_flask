console.log("app.js loaded");

d3.json("/api").then(data => {
    console.log('this is data loaded from the api. ');
    console.log(data);
    data.forEach(element => {
        console.log(element)
    });


})