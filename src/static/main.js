//Javascript classique
function Cambio(id1,id2,event) {
	var x = document.getElementById(id1);
	var y = document.getElementById(id2);
	if (x.style.display == "none") {
		x.style.display = "block";
		y.style.display = "none";
	} else {
		x.style.display = "none";
		y.style.display = "block";
	}
}
function myFunction5() {
	var modal = document.getElementById("myModal");
	if (modal.style.display == "none") {
		modal.style.display = "block";
	} else {
		modal.style.display = "none";
	}
}
//jQuery
$(document).ready(function()
	{
		setInterval("horloge()",100); // appeler toutes les 1 secondes
		setInterval("RAM()",50); 
	}
);
function horloge() {
	$.getJSON($SCRIPT_ROOT+'/horloge', {
	}, function horloge(data) {
		$("#temps").text(data.result);
	});
	return false;
};
function RAM() {
	$.getJSON($SCRIPT_ROOT+'/RAM', {
	}, function RAM(data) {
		$("#RAM").text(data.result);
	});
	return false;
};
$(function() {
    $('a#sentiments').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/sentiments', {
        phrase: $('textarea[name="a"]').val()
      }, function(data) {
        $("#result").html(data.result);
		$("#result").css("color",data.color);
      });
      return false;
    });
  });
