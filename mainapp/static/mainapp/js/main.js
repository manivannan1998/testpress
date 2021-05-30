function publishResult(){
    const math=document.getElementById("math").value;
    const sci=document.getElementById("sci").value;

    let total=parseFloat(math)+ parseFloat(sci);
    document.getElementById("sum").innerHTML="The Total is :"+ total;
    let percentage=(total*100)/200;
    document.getElementById("percentage").innerHTML="The Percentage is :"+ percentage;    

    if (percentage>=90) {
        document.getElementById("grade").innerHTML="You Are Passed In A+ Grade";
    }
    else if (percentage>=80) {
        document.getElementById("grade").innerHTML="You Are Passed In A Grade";
    }
    else if (percentage>=70) {
        document.getElementById("grade").innerHTML="You Are Passed In B+ Grade";
    }
    else if (percentage>=60) {
        document.getElementById("grade").innerHTML="You Are Passed In B Grade";
    }
    else if (percentage>=50) {
        document.getElementById("grade").innerHTML="You Are Passed In C+ Grade";
    }
    else if (percentage>=40) {
        document.getElementById("grade").innerHTML="You Are Passed In C Grade";
    }
    else if (percentage>=35) {
        document.getElementById("grade").innerHTML="You Are Passed In D Grade";
    }
    else{
        document.getElementById("grade").innerHTML="You Are Fail";
    }

}
