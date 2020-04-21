function getInputValue(){
    // Selecting the input element and get its value 
    var inputVal = document.getElementById("bells").value;
    var bellsCount = inputVal.toString();
    
    var url = "/bells/"+bellsCount;
    window.location = url;

}