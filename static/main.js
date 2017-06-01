function initGraph(error, graph, graphtype) {
    if (error) {
        throw error;
    }

    // Unhide graph panel
    document.getElementById("graph-panel").setAttribute("style", "display: block;");

    // Clear graph
    document.getElementById("svg").innerHTML = "";

    var min_x = Number.MAX_VALUE;//
    var max_x = 0;
    var min_y = Number.MAX_VALUE;
    var max_y = 0;

    for(var i = 0; i < graph.node_data.length; i++){
        var node = graph.node_data[i];
        min_x = Math.min(min_x, node.x);
        max_x = Math.max(max_x, node.x);
        min_y = Math.min(min_y, node.y);
        max_y = Math.max(max_y, node.y);
    }

    var new_scale_x = d3.scaleLinear().domain([min_x, max_x]).range([700, 50]);
    var new_scale_y = d3.scaleLinear().domain([min_y, max_y]).range([580, 50]);

    for (var i = 0; i < graph.node_data.length; i++) {
        graph.node_data[i].x = new_scale_x(graph.node_data[i].x);
        graph.node_data[i].y = new_scale_y(graph.node_data[i].y);
    }

    var svg = d3.select("#svg").append("svg")
        .attr("width", 720)
        .attr("height", 600);

    svg = svg.append('g');
    svg.append('rect').attr({ 'fill': '#111155', 'width': 720, 'height': 600 });
    svg.attr('transform', 'translate(20, 20)');

    var d3line = d3.line()
        .x(function (d) { return d.x; })
        .y(function (d) { return d.y; })
        .curve(d3.curveLinear);

    switch(graphtype){
        case 'normal':
            // Run the FDEB algorithm using default values on the data
            var fbundling = d3.ForceEdgeBundling()
                .nodes(graph.node_data)
                .edges(graph.edge_data)
                .step_size(0.0) // set step size low to effectively disable edge bundling
                .compatibility_threshold(1.0); // set threshold high to effectively disable edge bundling

            var results = fbundling();

            break;
        case 'bundled':
            // Run the FDEB algorithm using default values on the data
            var fbundling = d3.ForceEdgeBundling()
                .nodes(graph.node_data)
                .edges(graph.edge_data)
                .step_size(0.2)
                .compatibility_threshold(0.4);

            var results = fbundling();

            break;
        default:
            console.error('Bad graph type: ' + graphtype);
    }

    // plot the data
    for (var i = 0; i < results.length; i++) {
        svg.append("path").attr("d", d3line(results[i]))
            .style("stroke-width", 0.5)
            .style("stroke", "#ff2222")
            .style("fill", "none")
            .style('stroke-opacity', 0.15);
    }

    // draw nodes
    svg.selectAll('.node')
        .data(d3.entries(graph.node_data))
        .enter()
        .append('circle')
        .classed('node', true);
        //.attr({ 'r': 2, 'fill': '#ffee00' })
        //.attr('cx', function (d) { return d.value.x; })
        //.attr('cy', function (d) { return d.value.y; });
}

/* --- onclick functions --- */

function populateGraph() {
    var dataset = $("input[name=dataset]:checked").val();
    var graphtype = $("input[name=graphtype]:checked").val();

    console.log(JSON.stringify({ dataset: dataset, graphtype: graphtype }));

    $.get({
        url: "/api/graph",
        method: "GET",
        data: {
            dataset: dataset
        },
        success: function (res) {
            console.log(res);
            initGraph(null, res, graphtype);
        },
        error: function (e) {
            console.error(e);
            alert(e.responseText);
        }
    });
}