function ready(){
    document.getElementById("divPaso2").style.display = "none"
    document.getElementById("divPaso3").style.display = "none"
}

function paso1(){
    var caudal = document.getElementById("caudal").value
    if(caudal >= 5){
        alert(caudal)
        document.getElementById("divPaso2").style.display = "block"
    } else{
        alert("Error: Valor menor a 5")
        ready()
    }

}
    //let a = document.getElementById("divPaso2")
    //a.style.display = "none"
