
    var given_name = document.getElementById("exampleInputFirstName");
    var family_name = document.getElementById("exampleInputLastName");
    var age = document.getElementById("exampleInputAge");
    var height = document.getElementById("exampleInputHeight");
    var pet_name =document.getElementById("exampleInputPetName");
    // var button =document.getElementById("submit");
    var form = document.getElementById("details")

    // button.onclick=function(){
    form.onsubmit = function(e){
        e.preventDefault();
        // console.log(given_name.value.substring(0,1));
        // console.log(family_name.value.substring(0,1));
        // console.log(age.value);
        // console.log(height.value);
        // console.log(pet_name.value);
        if(given_name.value.substring(0,1)===family_name.value.substring(0,1)&&age.value>20&&age.value<30&&height.value>=170&&pet_name.value.substring(pet_name.value.length - 1)==="y"){
            console.log("welcome spy");
           }else{
               console.log("nothing to see here!");
           }
        
       // console.log(given_name.value);
    };
     

