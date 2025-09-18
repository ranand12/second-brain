# Python-nvd3 Documentation! — python-nvd3 0.14.2 documentation

Column: http://python-nvd3.readthedocs.io/en/latest/
Processed: No
created on: December 28, 2021 3:03 PM
topics: python, tech-stuff

NVD3 is an attempt to build re-usable charts and chart components for d3.js without taking away the power that d3.js offers you.

Python-NVD3 makes your life easy! You write Python and the library renders JavaScript for you! These graphs can be part of your web application:

> 
> 

Want to try it yourself? Install python-nvd3, enter your python shell and try this quick demo:

```
>>> from nvd3 import pieChart
>>> type = 'pieChart'
>>> chart = pieChart(name=type, color_category='category20c', height=450, width=450)
>>> xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
>>> ydata = [3, 4, 0, 1, 5, 7, 3]
>>> extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
>>> chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
>>> chart.buildcontent()
>>> print chart.htmlcontent

```

This will output the following HTML to render a live chart. The HTML could be stored into a HTML file, used in a Web application, or even used via Ipython Notebook:

```
<div id="pieChart"><svg style="width:450px;height:450px;"></svg></div>
<script>
data_pieChart=[{"values": [{"value": 3, "label": "Orange"},
               {"value": 4, "label": "Banana"},
               {"value": 0, "label": "Pear"},
               {"value": 1, "label": "Kiwi"},
               {"value": 5, "label": "Apple"},
               {"value": 7, "label": "Strawberry"},
               {"value": 3, "label": "Pineapple"}], "key": "Serie 1"}];

nv.addGraph(function() {
    var chart = nv.models.pieChart();
    chart.margin({top: 30, right: 60, bottom: 20, left: 60});
    var datum = data_pieChart[0].values;
            chart.tooltipContent(function(key, y, e, graph) {
                var x = String(key);
                var y =  String(y)  + ' cal';
                tooltip_str = '<center><b>'+x+'</b></center>' + y;
                return tooltip_str;
            });
        chart.showLegend(true);
        chart.showLabels(true);
        chart.donut(false);
    chart
        .x(function(d) { return d.label })
        .y(function(d) { return d.value });
    chart.width(450);
    chart.height(450);
    d3.select('#pieChart svg')
        .datum(datum)
        .transition().duration(500)
        .attr('width', 450)
        .attr('height', 450)
        .call(chart);
});
</script>

```

Check out the class references for dynamic examples and a full list of supported charts!

Excited !? Learn more here: