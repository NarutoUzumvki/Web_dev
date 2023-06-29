
<script src="https://code.jquery.com/jquery-3.7.0.js" integrity="sha256-JlqSTELeR4TLqP0OG9dxM7yDPqX1ox/HfgiSLBj8+kM=" crossorigin="anonymous">

    // variables
    function checkInfo () {
        

        var fname=prompt("Enter your First Name : ");
        var lname=prompt("Enter your Last Name : ");
        var age=prompt("Enter your Age : ");
        var height=prompt("Enter your height in cms : ");
        var pname=prompt("Enter your Pet Name : ");
        alert("Thank you For the Info :")

        //four Condition 
        var nameCond=null;
        var ageCond= null;
        var heightCond=null;
        var pNameCond = null ;


        if (fname[0] === lname[0]){
            nameCond = true  
        }
        else{
            nameCond=false 
        }


        if (age > 20 && age < 30 ){
            ageCond = true
        }
        else{
            ageCond=false
        }


        if(height >= 170){
            heightCond = true
        }
        else{
            heightCond=false
        }

        if(pname[pname.length-1]==="y"){
            pNameCond = true 
        }
        else{
            pNameCond=false
        }


        if(nameCond && ageCond && heightCond && pNameCond === true ){
            console.log("Welcome Spy!")
        }
        else{
            console.log("Nothing To Show!")   
        }
        }


</script>
 


 