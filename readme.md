---
title: "Data Tyding & Reporting - Assignment 1"
author: "Elianne Mora"
date: "February 4, 2020"
output: html_document
---
For this assignment we have reated a GitHub repository containing two files: pie-chart.html and the present one (readme.md).

The first file, using the javascript library d3.js, contains a pie-chart drawn by taking data from an 'input' tag. 


```{r, echo=FALSE}
<html>
    
<head>
  <meta charset="utf-8"/>
  <title>Pie Chart</title>
<!-- Load d3.js -->
  <script src="https://d3js.org/d3.v4.js"></script>
  
  <style>
    input {
     width:400;
     }
  </style>
</head>

<body>

<input id="array" value={"a":10,"b":25,"c":35,"d":5,"e":25} onChange="makePC()">
    
<!-- Create a div where the graph will take place -->
  <div id="my_dataviz"></div>
</body>
    
<script>

function makePC() {

// set the dimensions and margins of the graph
var width = 450
    height = 450
    margin = 40

// The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
var radius = Math.min(width, height) / 2 - margin

d3.select("#my_dataviz").html("")

// append the svg object to the div called 'my_dataviz'
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

// Create dummy data
var data = {a: 9, b: 20, c:30, d:8, e:12}

//document.getElementById("array").value = JSON.stringify(data)

var data=JSON.parse(document.getElementById("array").value);

// set the color scale
var color = d3.scaleOrdinal()
  .domain(data)
  .range(["#69b3a2", "slateblue", "pink", "darkgreen", "yellow"])

// Compute the position of each group on the pie:
var pie = d3.pie()
  .value(function(d) {return d.value; })
var data_ready = pie(d3.entries(data))

// Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
svg
  .selectAll('whatever')
  .data(data_ready)
  .enter()
  .append('path')
  .attr('d', d3.arc()
    .innerRadius(0)
    .outerRadius(radius)
  )
  .attr('fill', function(d){ return(color(d.data.key)) })
  .attr("stroke", "black")
  .style("stroke-width", "2px")
  .style("opacity", 0.7)
}

makePC()

</script>

</html>
```
