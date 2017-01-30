$(function(){
      $("#chat_reply").typed({
        strings: ["Hi <br> How can I help you?"],
        typeSpeed: 0
      });
  });

function typeWriter(text,element){
	$(element).typed({
        strings: [text],
        typeSpeed: 0
      });
}