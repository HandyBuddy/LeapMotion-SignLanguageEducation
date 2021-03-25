function checkPrediction(callbackFunc) {
	$.get('/predict_two_hand', function(data) {
		callbackFunc(data);
        });

}

  





$(window).on('load',function()
{

    $( "#button" ).click(function()
    {
        document.getElementById("answer").innerHTML = "입력 중 ...";
        document.getElementById("answer").style.fontSize = "40px";
        document.getElementById("answer").style.position = "relative";
        document.getElementById("answer").style.top = "-1430px";

        
        checkPrediction(function(data){
        	document.getElementById("answer").innerHTML = data;

        });


    });

});





