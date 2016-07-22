var i=0; 

function increment()
{
    i +=1;                        
}


function removeElement(parentDiv, childDiv){
 

     if (childDiv == parentDiv) {
          alert("The parent div cannot be removed.");
     }
     else if (document.getElementById(childDiv)) {     
          var child = document.getElementById(childDiv);
          var parent = document.getElementById(parentDiv);
          parent.removeChild(child);
     }
     else {
          alert("Child div has already been removed or does not exist.");
          return false;
     }
}


 /* 
 ----------------------------------------------------------------------------
 
 functions that will be called upon, when user click on the Name text field
 
 ---------------------------------------------------------------------------
 */
function nameFunction()
{
var r=document.createElement('span');
var y = document.createElement("INPUT");
y.setAttribute("type", "text");
y.setAttribute("placeholder","Name");
var g = document.createElement("IMG");
g.setAttribute("src", "delete.png");
increment(); 
y.setAttribute("Name","textelement_"+i);
r.appendChild(y);
g.setAttribute("onclick", "removeElement('myForm','id_"+ i +"')");
r.appendChild(g);
r.setAttribute("id", "id_"+i);
document.getElementById("myForm").appendChild(r);
}
