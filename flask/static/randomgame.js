function checkPrediction(callbackFunc) {
	$.get('/predict_one_hand', function(data) {
		callbackFunc(data);
        });

}


$(window).on('load', function()
{
    //바로 쓰기
    const words = ["처음", "취미", "무엇(무슨, 어디, 어떤)", "좋다", "강아지", "요즘", "먹다(밥)", "가다", "아프다", "기침하다", "병", "있다", "충분하다", "또", "오다", "예", "이틀 후(모레)"]
    let count=0;
    let selected = words[Math.floor(Math.random()*words.length)];
    document.getElementById("recognization").innerHTML = selected;
    document.getElementById("recognization").style.fontSize = "120px";
    document.getElementById("count").style.fontSize="35px";
    document.getElementById("process").style.fontSize="35px";
    
    checkPrediction(function(data){
    	document.getElementById("correct").innerHTML = "인식된 수화는 '" + data + "' 입니다!";
    	document.getElementById("correct").style.fontSize = "35px";
    	document.getElementById("process").innerHTML = "";
    	
    	if (data == selected) {
    		count+=1;
    		document.getElementById("count").innerHTML = "⭕맞춘 개수는 " + count + "개 입니다.⭕";
    	}
    	else 
    		document.getElementById("count").innerHTML = "⭕맞춘 개수는 " + count + "개 입니다.⭕";
    });
    
    $( "#button1" ).click(function()
    {
    	document.getElementById("process").innerHTML = "(인식중입니다.)";
    	document.getElementById("correct").innerHTML = "";
    	
        checkPrediction(function(data){
        	document.getElementById("process").innerHTML = "";
    		document.getElementById("correct").innerHTML = "인식된 수화는 '" + data + "' 입니다!";
    		if (data == selected) {
    			count+=1;
    			document.getElementById("count").innerHTML = "⭕맞춘 개수는 " + count + "개 입니다.⭕";
    		}
    		else 
    			document.getElementById("count").innerHTML = "⭕맞춘 개수는 " + count + "개 입니다.⭕";
        });
    });
    
    $( "#button2" ).click(function()
    {
        selected = words[Math.floor(Math.random()*words.length)]
        document.getElementById("recognization").innerHTML = selected;
        document.getElementById("recognization").style.fontSize = "120px";
        document.getElementById("correct").innerHTML = "";
        document.getElementById("process").innerHTML = "(인식중입니다.)";
        
        checkPrediction(function(data){
        	document.getElementById("process").innerHTML = "";
    		document.getElementById("correct").innerHTML = "인식된 수화는 '" + data + "' 입니다!";
    		if (data == selected) {
    			count+=1;
    			document.getElementById("count").innerHTML = "⭕맞춘 개수는 " + count + "개 입니다.⭕";
    		}
    		else 
    			document.getElementById("count").innerHTML = "⭕맞춘 개수는 " + count + "개 입니다.⭕";
        });
    });


    
});





