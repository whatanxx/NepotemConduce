let seniorBtn = document.getElementById("senior-btn");
let seniorForm = document.getElementById("form-senior");
let seniorBtnClicked = false;

let voluntaryBtn = document.getElementById("voluntary-btn");
let voluntaryForm = document.getElementById("form-voluntary");
let voluntaryBtnClicked = false;

let registerBtnEl = document.getElementById("register-btns");

// seniorBtn.addEventListener("click", ()=>{
//     voluntaryForm.style.display="";
//     seniorBtnClicked = !seniorBtnClicked;
//     voluntaryBtnClicked = false;
//     console.log(seniorBtnClicked);
    
//     if(seniorBtnClicked == true){
//         seniorForm.style.display="flex";
//         seniorForm.style.flexDirection="column";
//         seniorForm.style.gap="16px"
//         seniorForm.scrollIntoView();
//     }
//     else{
//         seniorForm.style.display="";
        
//     }
// } )

// voluntaryBtn.addEventListener("click", ()=>{
//     voluntaryBtnClicked = !voluntaryBtnClicked;
//     seniorForm.style.display="";
//     seniorBtnClicked = false;
//     console.log(voluntaryBtnClicked);
//     if(voluntaryBtnClicked == true){
//         voluntaryForm.style.display="flex";
//         voluntaryForm.style.flexDirection="column";
//         voluntaryForm.style.gap="16px"
//         voluntaryForm.scrollIntoView();
//     }
//     else{
//         voluntaryForm.style.display="";
        
//     }
// })