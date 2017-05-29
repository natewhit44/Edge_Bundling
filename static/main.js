function showGraph(){
    var dataset = $("input[name=dataset]:checked").val();
    var graphtype = $("input[name=graphtype]:checked").val();

    console.log(JSON.stringify({dataset: dataset, graphtype: graphtype}));

    $.get({
        url: "/api/graph",
        method: "GET",
        data: {
            dataset: dataset,
            graphtype: graphtype
        },
        success: function(res){
            alert("Response: " + res)  
        },
        error: function(e){
            console.error(e);
        }
    });
}