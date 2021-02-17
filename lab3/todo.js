var list = document.querySelector('ul');
list.addEventListener('click', function(chek) {
  if (chek.target.tagName === 'LI') {
    chek.target.classList.toggle('checked');
  }
}, false);

function newElement() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("newtodo").value;
  if (inputValue === '') {
    alert("Missing text");
  } else {
      var t = document.createTextNode(inputValue);
      li.appendChild(t);
    document.getElementById("listoftodo").appendChild(li);
  }
  document.getElementById("newtodo").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("delete");
  span.className = "delete";
  span.appendChild(txt);
  li.appendChild(span);

  var dlt = document.getElementsByClassName("delete");
  var i;
  for (i = 0; i < dlt.length; i++) {
    dlt[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}