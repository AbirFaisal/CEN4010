
window.changeTooltip = function(e) {
    var val = e.value.toFixed(1), speed;
    if (val < 80) speed = "COOLING";
    else speed = "HEATING";
    return "<div>" + speed + "<div>" + "<b>" + val + "<b>"
  }
  
  $("#inner-slider").roundSlider({
    step: "0.1",
    min: "60",
    max: "90",
    sliderType: "min-range",
    radius: 100,
    value: 20,
    startAngle: "315",
    endAngle: "225",
    tooltipFormat: "changeTooltip",
    editableTooltip: false,
    
    svgMode: true,
  
    create: function() {
      var that = this;
      var btn1 = $("<button id='sub'>&#9660</button>");
      var btn2 = $("<button id='add'>&#9650</button>");
      this.innerContainer.append(btn1);
      this.innerContainer.append(btn2);
      btn1.click(function() {
        that.setValue(that.options.value - 0.1);
      });
      btn2.click(function() {
        that.setValue(that.options.value + 0.1);
      });
    }
  });