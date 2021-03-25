function checkPrediction(callbackFunc) {
	$.get('/predict_one_hand', function(data) {
		setTimeout(function() {
			callbackFunc(data);
		}, 7000);
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
        
        /*
        let meaning = document.getElementById("meaning")
        let right = document.getElementById("right")
        */
        
       
        
        
        checkPrediction(function(data){
        	document.getElementById("answer").innerHTML = data;
        	if (document.getElementById("meaning").innerHTML == data) {
        		alert("1");
        		document.getElementById("right").innerHTML = "정답입니다!";
        	}
        	else
        		alert("2");
        	alert("3");
        });
        




    });

});





